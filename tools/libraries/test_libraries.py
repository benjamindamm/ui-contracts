#!/usr/bin/env python3
"""Library isolation, frozen migration, legacy references and CLI selection tests."""
import hashlib
import importlib.util
import json
import shutil
import subprocess
import tempfile
import unittest
import uuid
from pathlib import Path
import manage

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('handoffs', ROOT/'skills/ui-contracts/scripts/handoffs.py')
handoffs = importlib.util.module_from_spec(spec); spec.loader.exec_module(handoffs)

class LibrariesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name).resolve()
    def test_empty_library_has_no_example_components_or_tokens(self):
        manage.create(self.repo,'example'); manage.create(self.repo,'my-app','My App')
        self.assertEqual(json.loads((self.repo/'libraries/my-app/library.json').read_text())['components'],{})
        self.assertEqual(json.loads((self.repo/'libraries/my-app/tokens.json').read_text()),{})
    def test_initializing_second_library_preserves_first(self):
        manage.create(self.repo,'first');first=self.repo/'libraries/first/tokens.json';first.write_text('{"unique":42}')
        manage.create(self.repo,'second');self.assertEqual(first.read_text(),'{"unique":42}')
    def test_existing_library_never_overwritten(self):
        manage.create(self.repo,'first')
        with self.assertRaises(FileExistsError):manage.create(self.repo,'first')
    def test_invalid_ids_rejected(self):
        for name in ['../outside','/tmp/escape','Uppercase','a/b','a_b','']:
            with self.assertRaises(ValueError):manage.create(self.repo,name)
    def test_symlink_library_rejected(self):
        (self.repo/'libraries').mkdir();(self.repo/'libraries/link').symlink_to('/tmp')
        with self.assertRaises(ValueError):manage.describe(self.repo,'link')
    def test_symlink_container_rejected(self):
        (self.repo/'libraries').symlink_to('/tmp')
        with self.assertRaises(ValueError):manage.create(self.repo,'first')
    def test_manifest_refuses_symlink_sources(self):
        manage.create(self.repo,'first');(self.repo/'libraries/first/ref').symlink_to('/tmp')
        with self.assertRaises(ValueError):manage.manifest(self.repo,'first')
    def test_manifest_binds_selected_root(self):
        manage.create(self.repo,'first');manage.create(self.repo,'second')
        m=manage.manifest(self.repo,'first');self.assertEqual(m['root'],'libraries/first')
        self.assertEqual(set(m['files']),{'library.json','tokens.json'})
        self.assertNotEqual(m['revision'],manage.manifest(self.repo,'second')['revision'])
    def test_migration_preserves_all_22_historical_hashes(self):
        frozen=json.loads((ROOT/'tools/design-review/profile.json').read_text())['definitionFiles']
        m=manage.manifest(ROOT,'example');self.assertEqual(m['files'],frozen)
        self.assertEqual(len(m['files']),22)
        self.assertEqual(m['revision'],'1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727')
        self.assertFalse((ROOT/'components').exists())
    def test_legacy_resolver_keeps_hash_verification(self):
        path=ROOT/'libraries/example/tokens.json'
        self.assertEqual(handoffs.resolve(ROOT,'components/tokens.json'),path)
        ref={'path':'components/tokens.json','sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
        self.assertEqual(handoffs.bound(ROOT,ref),path)
        ref['sha256']='0'*64
        with self.assertRaises(handoffs.Invalid):handoffs.bound(ROOT,ref)
    def test_two_libraries_same_relative_name_remain_distinct(self):
        for name in ['one','two']:manage.create(self.repo,name)
        self.assertNotEqual(handoffs.resolve(self.repo,'libraries/one/tokens.json'),handoffs.resolve(self.repo,'libraries/two/tokens.json'))
    def test_legacy_does_not_override_existing_components(self):
        manage.create(self.repo,'example');(self.repo/'components').mkdir()
        self.assertEqual(handoffs.resolve(self.repo,'components/missing.json'),self.repo/'components/missing.json')
    def test_task_cannot_write_another_library(self):
        for name in ['one','two']:manage.create(self.repo,name)
        m=manage.manifest(self.repo,'one');mp=self.repo/'manifest.json';mp.write_text(json.dumps(m))
        sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
        task={'format':'ui-contracts-task/1','taskId':'one-task','revision':1,'role':'builder','phase':'normal',
              'goal':'One library only','scope':'No cross-library writes',
              'definition':{'revision':m['revision'],'manifest':{'path':'manifest.json','sha256':sha(mp)}},
              'sources':[{'id':'one','path':'libraries/one/library.json','sha256':sha(self.repo/'libraries/one/library.json'),'kind':'original','purpose':'Selected library'}],
              'inputs':[],'outputs':['libraries/two'],
              'acceptance':[{'id':'done','required':True,'description':'A built artifact'}]}
        with self.assertRaises(handoffs.Invalid):handoffs.validate_task(self.repo,task)
        task['outputs']=['work/one'];self.assertIn('sources',handoffs.validate_task(self.repo,task))

    def test_cli_has_no_implicit_library(self):
        proc=subprocess.run(['python3',str(ROOT/'tools/libraries/manage.py'),'show'],capture_output=True)
        self.assertNotEqual(proc.returncode,0)
    def test_manifest_cannot_overwrite_sources(self):
        manage.create(self.repo,'first');path=self.repo/'libraries/first/tokens.json';before=path.read_bytes()
        proc=subprocess.run(['python3',str(ROOT/'tools/libraries/manage.py'),'--repo',str(self.repo),'manifest','first','--output',str(path)],capture_output=True)
        self.assertNotEqual(proc.returncode,0);self.assertEqual(path.read_bytes(),before)
    def test_inspect_library_runs_but_never_grants_full_approval(self):
        name='test-'+uuid.uuid4().hex;root=ROOT/'libraries'/name
        try:
            manage.create(ROOT,name)
            proc=subprocess.run(['python3',str(ROOT/'skills/ui-contracts/scripts/contracts.py'),'inspect','--repo',str(ROOT),'--library',name],capture_output=True,text=True)
            self.assertEqual(proc.returncode,2,proc.stderr)
            data=json.loads(proc.stdout);self.assertEqual(data['diagnostic']['code'],'SEMANTIC_PROFILE_UNSUPPORTED')
            self.assertEqual(Path(data['candidate']),root);self.assertFalse(data['release'])
            self.assertTrue(all(str(root) in row['file'] for row in data['artifacts']))
        finally:
            if root.exists():shutil.rmtree(root)
    def test_validate_library_not_misrepresented_as_reference(self):
        proc=subprocess.run(['python3',str(ROOT/'skills/ui-contracts/scripts/contracts.py'),'validate','--repo',str(ROOT),'--library','example'],capture_output=True,text=True)
        self.assertEqual(proc.returncode,2)
        self.assertEqual(json.loads(proc.stdout)['diagnostic']['code'],'LIBRARY_SELECTION_UNSUPPORTED')

if __name__=='__main__':unittest.main()
