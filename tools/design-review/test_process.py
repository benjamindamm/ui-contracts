import copy
import hashlib
import tempfile
import unittest
from pathlib import Path
from check_process import verify

class ProcessTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name);(self.base/'record.txt').write_text('neutral test record')
        self.ref={'path':'record.txt','sha256':hashlib.sha256((self.base/'record.txt').read_bytes()).hexdigest()}
        roles={r:{'model':'test','modelRevision':'test-revision','reasoning':'medium','harnessStepLimit':100,
                  'contextPolicy':'separate-session','initialPrompt':self.ref,'skills':[]} for r in ['builderA','builderB','reviewer']}
        self.data={'runId':'test','definitionRevision':'a'*64,'toolchainLockSha256':'b'*64,'harnessVersion':'test',
                   'comparisonPolicyId':'test-policy','comparisonPolicy':self.ref,'roles':roles,'events':[]}
        for r in roles:
            self.data['events'] += [{'id':r+'-start','kind':'start','actor':r,'at':'2026-10-29T10:00:00Z'},
                                    {'id':r+'-complete','kind':'complete','actor':r,'at':'2026-10-29T10:00:00Z'}]
    def result(self):return verify(self.data,self.base)
    def test_complete(self):self.assertEqual(self.result()['overall'],'METADATA_COMPLETE')
    def test_unknown_model_not_inferred(self):
        self.data['roles']['builderA']['model']=None
        self.assertIn('builderA.model:missing',self.result()['errors'])
    def test_prompt_hash_detects_drift(self):
        (self.base/'record.txt').write_text('new instructions')
        self.assertTrue(any('hash-mismatch' in e for e in self.result()['errors']))
    def stop_resume(self):
        self.data['events'][1:1]=[
          {'id':'stop1','kind':'stop','actor':'builderA','at':'2026-10-29T10:00:00Z','cause':'step-limit','stepsUsed':100,'checkpoint':self.ref},
          {'id':'resume1','kind':'resume','actor':'builderA','at':'2026-10-29T10:00:00Z','stopId':'stop1','sameSession':True,'message':self.ref,'semanticCoaching':False}]
    def test_neutral_continuation(self):
        self.stop_resume();self.assertEqual(self.result()['overall'],'METADATA_COMPLETE')
    def test_coaching_changes_condition(self):
        self.stop_resume();self.data['events'][2]['semanticCoaching']=True
        self.assertTrue(any('changed-prompt-condition' in e for e in self.result()['errors']))
    def test_completion_not_extra_stop(self):
        self.stop_resume();self.data['events'][2]['kind']='complete'
        self.assertIn('unresolved-stop',self.result()['errors'])
    def test_missing_historical_metadata_blocks(self):
        self.assertEqual(verify({'runId':'old'},self.base)['overall'],'BLOCKED')

if __name__=='__main__':unittest.main()
