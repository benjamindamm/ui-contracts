import importlib.util,shutil,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('thin_context_guard',Path(__file__).with_name('context_guard.py'));guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard)
class ContextTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.repo=Path(self.tmp.name);self.skill=self.repo/'skills/ui-contracts';shutil.copytree(ROOT/'skills/ui-contracts',self.skill,ignore=shutil.ignore_patterns('__pycache__'))
  for n in ['AGENTS.md','CLAUDE.md','GEMINI.md']:shutil.copy2(ROOT/n,self.repo/n)
  # Targets of shared AGENTS links, without loading their file bodies into any model.
  for n in ['docs/README.md','libraries/README.md','docs/research/DOCUMENT-INDEX.md','docs/research/analyses/INITIAL-CONTEXT/ENTRYPOINTS.md']:
   p=self.repo/n;p.parent.mkdir(parents=True,exist_ok=True);p.touch()
 def test_current_compact_routes_pass(self):self.assertEqual(guard.inspect(self.repo,self.skill)['overall'],'PASS_LIMITED')
 def test_growing_core_is_detected(self):
  p=self.skill/'SKILL.md';p.write_text(p.read_text()+'\n'+'x'*3201);self.assertEqual(guard.inspect(self.repo,self.skill)['overall'],'FAIL')
 def test_missing_detail_route_is_detected(self):
  (self.skill/'references/integration-review.md').unlink();self.assertEqual(guard.inspect(self.repo,self.skill)['overall'],'FAIL')
 def test_eager_import_is_detected(self):
  p=self.skill/'SKILL.md';p.write_text(p.read_text()+'\n@references/workflow.md\n');self.assertEqual(guard.inspect(self.repo,self.skill)['overall'],'FAIL')
 def test_inflated_assigned_role_is_detected(self):
  p=self.skill/'references/roles/builder.md';p.write_text('x'*3501);self.assertEqual(guard.inspect(self.repo,self.skill)['overall'],'FAIL')
if __name__=='__main__':unittest.main()
