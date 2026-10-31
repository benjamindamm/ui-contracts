import importlib.util,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('navigation_tests',Path(__file__).with_name('navigation.py'));nav=importlib.util.module_from_spec(spec);spec.loader.exec_module(nav)
class NavigationTests(unittest.TestCase):
 def test_current_active_routes_exist(self):self.assertEqual(nav.scan(ROOT)['overall'],'PASS_LIMITED')
 def test_missing_route_fails(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);(p/'README.md').write_text('[details](docs/missing.md)');self.assertEqual(nav.scan(p,['README.md'])['overall'],'FAIL')
 def test_raw_evidence_is_catalogued_without_becoming_an_entry(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);(p/'README.md').write_text('Start');d=p/'docs/research/studies/example';d.mkdir(parents=True);(d/'README.md').write_text('[preserved old link](does-not-exist)');r=nav.scan(p,['README.md']);self.assertEqual(r['overall'],'PASS_LIMITED');self.assertEqual(r['counts']['5-research-and-evidence'],1);self.assertEqual(r['activeEntries'],['README.md'])
 def test_legacy_generator_cannot_erase_current_index(self):
  p=ROOT/'docs/research/DOCUMENT-INDEX.md';before=p.read_bytes();r=subprocess.run([sys.executable,str(ROOT/'tools/research/build_indexes.py')],capture_output=True);self.assertNotEqual(r.returncode,0);self.assertEqual(p.read_bytes(),before)
 def test_report_cannot_overwrite_existing_evidence(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'existing.json';p.write_text('unchanged');r=subprocess.run([sys.executable,str(ROOT/'tools/research/navigation.py'),'--output',str(p)],capture_output=True);self.assertNotEqual(r.returncode,0);self.assertEqual(p.read_text(),'unchanged')
if __name__=='__main__':unittest.main()
