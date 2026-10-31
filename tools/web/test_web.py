"""Receipt/source/measurement countercases; fixture is copied, never edited in place."""
import importlib.util,json,os,shutil,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('current_browser_gate',Path(__file__).with_name('check.py'));gate=importlib.util.module_from_spec(spec);spec.loader.exec_module(gate)
class AdapterBindingTests(unittest.TestCase):
 def setUp(self):
  spec=importlib.util.spec_from_file_location('prepare_binding_tests',Path(__file__).with_name('prepare.py'));self.prepare=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.prepare)
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.lib=Path(self.tmp.name)/'lib';shutil.copytree(gate.ROOT/'libraries/example',self.lib);self.index=json.loads((self.lib/'library.json').read_text())
 def test_domain_redirect_cannot_silently_use_old_behavior(self):
  p=self.lib/'components/input/component.json';d=json.loads(p.read_text());d['domains']['behavior']='new-behavior.scxml';(p.parent/'new-behavior.scxml').write_bytes((p.parent/'behavior.scxml').read_bytes());p.write_text(json.dumps(d))
  with self.assertRaisesRegex(ValueError,'source layout unsupported'):self.prepare.require_adapter_layout(self.lib,self.index)
 def test_visual_redirect_cannot_silently_use_old_tokens(self):
  p=self.lib/'components/autocomplete/component.json';d=json.loads(p.read_text());d['domains']['visual']['tokens']='../../new-tokens.json';(self.lib/'new-tokens.json').write_bytes((self.lib/'tokens.json').read_bytes());p.write_text(json.dumps(d))
  with self.assertRaisesRegex(ValueError,'visual/rules layout unsupported'):self.prepare.require_adapter_layout(self.lib,self.index)

@unittest.skipUnless(os.environ.get('UI_CONTRACTS_BROWSER_RUN'),'Needs completed fresh browser captures')
class BrowserGateTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.run=Path(self.tmp.name)/'run';shutil.copytree(os.environ['UI_CONTRACTS_BROWSER_RUN'],self.run)
 def change(self,name,fn):
  p=self.run/'captures'/(name+'.json');d=json.loads(p.read_text());fn(d);p.write_text(json.dumps(d))
 def test_current_bound_capture_passes(self):self.assertEqual(gate.check(self.run)['overall'],'PASS_LIMITED')
 def test_missing_case_blocks(self):
  (self.run/'captures/ac-scroll.json').unlink();self.assertEqual(gate.check(self.run)['overall'],'BLOCKED')
 def test_replayed_challenge_fails(self):
  self.change('initial',lambda d:d.update(challenge='previous-run'));self.assertEqual(gate.check(self.run)['overall'],'FAIL')
 def test_tampered_bound_host_fails(self):
  p=self.run/'host.js';p.write_text(p.read_text()+'\n//tamper');self.assertEqual(gate.check(self.run)['overall'],'FAIL')
 def test_scroll_claim_without_geometry_fails(self):
  self.change('ac-scroll',lambda d:d.update(journal=[x for x in d['journal'] if x['type']!='host.measure']));self.assertEqual(gate.check(self.run)['overall'],'FAIL')
 def test_wrong_event_payload_fails(self):
  self.change('ac-commit',lambda d:d['snapshot']['events']['A'][0]['detail'].update(value='label-not-key'));self.assertEqual(gate.check(self.run)['overall'],'FAIL')
 def test_body_focus_fails(self):
  self.change('ac-scroll',lambda d:d['snapshot'].update(focus=''));self.assertEqual(gate.check(self.run)['overall'],'FAIL')
 def test_missing_actual_AX_fails(self):
  self.change('ac-scroll',lambda d:d['payload'].update(ax={'nodes':[]}));self.assertEqual(gate.check(self.run)['overall'],'FAIL')
 def test_synthetic_key_journal_fails(self):
  self.change('ac-scroll',lambda d:[x.update(isTrusted=False) for x in d['journal'] if x['type']=='dom.key']);self.assertEqual(gate.check(self.run)['overall'],'FAIL')
if __name__=='__main__':unittest.main()
