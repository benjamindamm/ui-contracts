import importlib.util,json,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('project_setup',Path(__file__).with_name('setup.py'));setup=importlib.util.module_from_spec(spec);spec.loader.exec_module(setup)
class SetupTests(unittest.TestCase):
 def test_recipe_exact_locked_set(self):
  lock=json.loads((setup.ROOT/'tools/ux/runtime.lock.json').read_text());urls=json.loads((setup.ROOT/'tools/ux/runtime-artifacts.json').read_text())['urls'];self.assertEqual(set(lock['jars']),set(urls));self.assertTrue(all(u.startswith('https://repo.maven.apache.org/maven2/') for u in urls.values()))
 def test_wrong_download_rejected_without_install(self):
  with tempfile.TemporaryDirectory() as tmp:
   with self.assertRaisesRegex(ValueError,'hash mismatch'):setup.jars(Path(tmp),lambda url:b'bad bytes')
   self.assertFalse(list((Path(tmp)/'jars').glob('*.jar')))
 def test_corrupt_existing_artifact_not_reused(self):
  lock=json.loads((setup.ROOT/'tools/ux/runtime.lock.json').read_text())
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);(p/'jars').mkdir();target=p/'jars'/next(iter(lock['jars']));target.write_bytes(b'corrupt')
   with self.assertRaisesRegex(ValueError,'wrong hash'):setup.jars(p,lambda url:b'bad')
   self.assertEqual(target.read_bytes(),b'corrupt')
if __name__=='__main__':unittest.main()
