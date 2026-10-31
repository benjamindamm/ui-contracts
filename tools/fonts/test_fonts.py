#!/usr/bin/env python3
"""Positive/negative local-font evidence tests; original library is never changed."""
import hashlib
import json
import shutil
import tempfile
import subprocess
import uuid
import unittest
from pathlib import Path
import check

ROOT=Path(__file__).resolve().parents[2]

class FontsTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.repo=Path(self.tmp.name)
        self.lib=self.repo/'libraries/test-fonts';self.lib.mkdir(parents=True)
        for f in ['library.json','tokens.json','fonts.json']:shutil.copyfile(ROOT/'libraries/example'/f,self.lib/f)
        # This fixture tests fonts only; do not declare copied component paths whose files are absent.
        index=json.loads((self.lib/'library.json').read_text());index['components']={};index.pop('selection',None)
        (self.lib/'library.json').write_text(json.dumps(index))
        shutil.copytree(ROOT/'libraries/example/assets',self.lib/'assets')
        self.manifest=json.loads((self.lib/'fonts.json').read_text())
    def write_manifest(self): (self.lib/'fonts.json').write_text(json.dumps(self.manifest))
    def validate(self):self.write_manifest();return check.validate(self.repo,'test-fonts')
    def test_valid_faces_and_tokens(self):
        r=self.validate();self.assertEqual(r['overall'],'PASS_LIMITED');self.assertFalse(r['release'])
        self.assertEqual([f['ttfMetadata']['weight'] for f in r['faces']],[400,700])
    def test_modified_asset_blocked(self):
        (self.lib/'assets/fonts/Inter-Regular.ttf').write_bytes(b'wrong bytes')
        with self.assertRaises(ValueError):self.validate()
    def test_missing_asset_blocked(self):
        (self.lib/'assets/fonts/Inter-Bold.ttf').unlink()
        with self.assertRaises(OSError):self.validate()
    def test_false_weight_blocked(self):
        self.manifest['families'][0]['faces'][0]['weight']=500
        with self.assertRaises(ValueError):self.validate()
    def test_wrong_runtime_style_blocked(self):
        self.manifest['families'][0]['faces'][0]['openpencilStyle']='Bold'
        with self.assertRaises(ValueError):self.validate()
    def test_false_family_with_matching_token_still_blocked(self):
        self.manifest['families'][0]['family']='Invented';t=json.loads((self.lib/'tokens.json').read_text());t['autocomplete']['fontFamily']['$value']='Invented';(self.lib/'tokens.json').write_text(json.dumps(t))
        with self.assertRaises(ValueError):self.validate()
    def test_family_token_mismatch_blocked(self):
        self.manifest['families'][0]['tokenPaths']=['autocomplete.width']
        with self.assertRaises(ValueError):self.validate()
    def test_wrong_binary_even_with_rehashed_manifest_blocked(self):
        p=self.lib/'assets/fonts/Inter-Regular.ttf';p.write_bytes(b'not a ttf file')
        self.manifest['families'][0]['faces'][0]['assets'][0]['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
        with self.assertRaises(ValueError):self.validate()
    def test_woff2_bad_length_with_current_hash_blocked(self):
        p=self.lib/'assets/fonts/Inter-Regular.woff2';p.write_bytes(p.read_bytes()[:-1])
        self.manifest['families'][0]['faces'][0]['assets'][1]['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
        with self.assertRaises(ValueError):self.validate()
    def test_declared_license_file_missing_blocked(self):
        (self.lib/'assets/fonts/LICENSE.txt').unlink()
        with self.assertRaises(OSError):self.validate()
    def test_no_license_metadata_is_not_a_technical_blocker(self):
        del self.manifest['license'];(self.lib/'assets/fonts/LICENSE.txt').unlink()
        r=self.validate();self.assertEqual(r['overall'],'PASS_LIMITED')
        self.assertEqual(r['licenseEvidence']['status'],'notChecked');self.assertTrue(r['warnings']);self.assertFalse(r['release'])
    def test_external_license_note_does_not_require_a_file(self):
        self.manifest['license']={'status':'unknown','note':'No separate file available for this pilot'}
        r=self.validate();self.assertEqual(r['licenseEvidence']['status'],'notChecked')
        self.assertEqual(r['license']['status'],'unknown')
    def test_present_license_never_establishes_rights_review(self):
        r=self.validate();self.assertEqual(r['licenseEvidence']['status'],'file-present')
        self.assertEqual(r['licenseEvidence']['rightsReview'],'notChecked')
    def test_no_license_does_not_hide_font_corruption(self):
        del self.manifest['license'];(self.lib/'assets/fonts/Inter-Regular.ttf').write_bytes(b'broken')
        with self.assertRaises(ValueError):self.validate()
    def test_library_inspection_without_license_file_still_checks_fonts(self):
        del self.manifest['license'];self.write_manifest();(self.lib/'assets/fonts/LICENSE.txt').unlink()
        code,result=self.inspect_temporary_library(False)
        self.assertEqual(code,2);self.assertEqual(result['overall'],'BLOCKED')
        self.assertEqual(result['fontAssets']['overall'],'PASS_LIMITED')
        self.assertEqual(result['fontAssets']['licenseEvidence']['status'],'notChecked')
    def test_path_escape_blocked(self):
        self.manifest['license']['path']='../../outside'
        with self.assertRaises(ValueError):self.validate()
    def test_symlink_font_blocked(self):
        p=self.lib/'assets/fonts/Inter-Regular.ttf';p.unlink();p.symlink_to(ROOT/'libraries/example/assets/fonts/Inter-Regular.ttf')
        with self.assertRaises(ValueError):self.validate()
    def inspect_temporary_library(self,corrupt):
        name='font-test-'+uuid.uuid4().hex;dest=ROOT/'libraries'/name
        try:
            shutil.copytree(self.lib,dest)
            if corrupt:(dest/'assets/fonts/Inter-Regular.ttf').write_bytes(b'corrupt font')
            proc=subprocess.run(['python3',str(ROOT/'skills/ui-contracts/scripts/contracts.py'),'inspect','--repo',str(ROOT),'--library',name],capture_output=True,text=True)
            return proc.returncode,json.loads(proc.stdout)
        finally:
            if dest.exists():shutil.rmtree(dest)
    def test_library_inspection_integrates_valid_font_check(self):
        code,result=self.inspect_temporary_library(False)
        self.assertEqual(code,2);self.assertEqual(result['overall'],'BLOCKED')
        self.assertEqual(result['fontAssets']['overall'],'PASS_LIMITED');self.assertFalse(result['release'])
    def test_library_inspection_rejects_dangling_copied_component_index(self):
        shutil.copyfile(ROOT/'libraries/example/library.json',self.lib/'library.json')
        code,result=self.inspect_temporary_library(False)
        self.assertEqual(code,1);self.assertEqual(result['overall'],'FAIL')
        self.assertEqual(result['diagnostic']['code'],'COMPONENT_BINDING_INVALID')
        self.assertTrue(any(e['code']=='REFERENCE_MISSING' for e in result['bindings']['errors']))
        self.assertEqual(result['fontAssets']['overall'],'PASS_LIMITED')

    def test_library_inspection_rejects_corrupt_font(self):
        code,result=self.inspect_temporary_library(True)
        self.assertEqual(code,1);self.assertEqual(result['diagnostic']['code'],'FONT_ASSET_CHECK_FAILED')
        self.assertFalse(result['release'])
    def test_duplicate_face_blocked(self):
        self.manifest['families'][0]['faces'].append(self.manifest['families'][0]['faces'][0])
        with self.assertRaises(ValueError):self.validate()

if __name__=='__main__':unittest.main()
