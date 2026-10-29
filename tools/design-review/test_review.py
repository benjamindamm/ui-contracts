#!/usr/bin/env python3
"""Regression cases for defects found in AC-R02. No historical file writes."""
import copy
import json
import subprocess
import unittest
from pathlib import Path
import check

class CountercheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tokens = check.load(check.example_root(check.ROOT)/'tokens.json')
        cls.stories = {s['id']:s for s in check.load(check.example_root(check.ROOT)/'autocomplete/stories.json')['stories']}
        cls.rules = check.load(check.example_root(check.ROOT)/'autocomplete/accessibility.rules.json')
        fig = check.ROOT/'examples/autocomplete/reproducibility/run-02/builder-a/autocomplete.fig'
        p = subprocess.run(['node',str(check.HERE/'read-fig.mjs'),str(check.ROOT),str(fig)],capture_output=True,text=True,check=True)
        cls.delivered = json.loads(p.stdout)['nodes']
        cls.valid = copy.deepcopy(cls.delivered)
        by_id = {n['id']:n for n in cls.valid}
        frame = next(n for n in cls.valid if n['name']=='Autocomplete / disabled')
        inp = next(by_id[i] for i in frame['childIds'] if by_id[i]['name']=='input')
        text = next(by_id[i] for i in inp['childIds'] if by_id[i]['type']=='TEXT')
        text['fills'][0]['color'] = {'r':100/255,'g':116/255,'b':139/255,'a':1}

    def assess(self,nodes):
        return check.assess(nodes,self.tokens,self.stories,self.rules)

    def in_case(self,nodes,cid,name):
        by_id = {n['id']:n for n in nodes}
        frame = next(n for n in nodes if n['name']=='Autocomplete / '+cid)
        def walk(n):
            yield n
            for i in n['childIds'] or []:
                yield from walk(by_id[i])
        return next(n for n in walk(frame) if n['name']==name)

    def test_positive_source_correct_placeholder_passes_limited(self):
        r=self.assess(self.valid)
        self.assertEqual(r['overall'],'PASS_LIMITED')
        self.assertFalse(r['release'])
        self.assertTrue(r['notChecked'])

    def test_delivered_placeholder_detected(self):
        self.assertIn('disabled.inputText.color',[x['id'] for x in self.assess(self.delivered)['failures']])

    def test_stroke_weight_counterexample(self):
        ns=copy.deepcopy(self.valid)
        self.in_case(ns,'ready','input')['strokes'][0]['weight']=9
        self.assertIn('ready.input.stroke.weight',[x['id'] for x in self.assess(ns)['failures']])

    def test_second_option_font_counterexample(self):
        ns=copy.deepcopy(self.valid)
        by_id={n['id']:n for n in ns}
        opt=self.in_case(ns,'ready','option hamburg')
        by_id[opt['childIds'][0]]['fontSize']=28
        self.assertTrue(any(x['id'].startswith('ready.text') and x['id'].endswith('fontSize') for x in self.assess(ns)['failures']))

    def test_input_color_usage_not_only_token_membership(self):
        ns=copy.deepcopy(self.valid)
        inp=self.in_case(ns,'loading','input')
        t=next(n for n in ns if n['id']==inp['childIds'][0])
        t['fills'][0]['color']={'r':185/255,'g':28/255,'b':28/255,'a':1}
        self.assertIn('loading.inputText.color',[x['id'] for x in self.assess(ns)['failures']])

    def test_hidden_input_not_accepted_by_name_presence(self):
        ns=copy.deepcopy(self.valid)
        self.in_case(ns,'ready','input')['visible']=False
        self.assertIn('ready.input.visible',[x['id'] for x in self.assess(ns)['failures']])

    def test_locked_text_is_not_editable_pass(self):
        ns=copy.deepcopy(self.valid)
        self.in_case(ns,'ready','label')['locked']=True
        self.assertIn('ready.lockedNodeCount',[x['id'] for x in self.assess(ns)['failures']])

    def test_duplicate_parts_detected(self):
        ns=copy.deepcopy(self.valid)
        x=copy.deepcopy(self.in_case(ns,'ready','input'))
        x.update(id='test-duplicate',childIds=[])
        ns.append(x)
        self.in_case(ns,'ready','Autocomplete / ready')['childIds'].append(x['id'])
        self.assertIn('ready.input.count',[x['id'] for x in self.assess(ns)['failures']])

    def test_pair_does_not_skip_missing_values(self):
        r=check.compare({'a':None},{})
        self.assertEqual(r['matched'],0)
        self.assertEqual(r['compared'],1)

    def test_one_channel_token_drift_visible(self):
        ns=copy.deepcopy(self.valid)
        self.in_case(ns,'closed','input')['strokes'][0]['color']['b']=226/255
        r=self.assess(ns)
        self.assertIn('closed.input.stroke.color',[x['id'] for x in r['warnings']])

    def test_changed_definition_blocks_profile(self):
        profile=copy.deepcopy(check.load(check.HERE/'profile.json'))
        profile['definitionFiles']['tokens.json']='invalid'
        self.assertIn('SOURCE_PROFILE_MISMATCH:tokens.json',check.profile_gate(check.ROOT,profile))

    def test_changed_toolchain_blocks_profile(self):
        profile=copy.deepcopy(check.load(check.HERE/'profile.json'))
        profile['toolchainPackageLockSha256']='invalid'
        self.assertIn('TOOLCHAIN_PROFILE_MISMATCH',check.profile_gate(check.ROOT,profile))

if __name__=='__main__':
    unittest.main()
