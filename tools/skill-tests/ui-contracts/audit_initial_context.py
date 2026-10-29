#!/usr/bin/env python3
"""Measure local routing files and synthetic packets; not the model's full request."""
import hashlib
import importlib.util
import json
from pathlib import Path
import test_handoffs as fixtures

ROOT=Path(__file__).resolve().parents[3]
SKILL=ROOT/'skills/ui-contracts'
spec=importlib.util.spec_from_file_location('handoffs',SKILL/'scripts/handoffs.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
fixtures.MODULE=module
case=fixtures.HandoffTests();case.setUp()
try:
    task=case.consumer();path=case.put('plan/build-task.json',task)
    bootstrap={'overall':'BOOTSTRAP_READY','release':False,'bootstrap':module.bootstrap_packet(case.repo,path)}
    expanded={'overall':'CONTEXT_READY','release':False,'context':module.context_packet(case.repo,task)}
    def size(text):return {'characters':len(text),'utf8Bytes':len(text.encode())}
    def wire(value):return json.dumps(value,ensure_ascii=False,indent=2)+'\n'
    files={str(p.relative_to(SKILL)):{**size(p.read_text()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
           for p in sorted(SKILL.rglob('*')) if p.is_file() and '__pycache__' not in p.parts}
    baseline=json.loads((Path(__file__).parent/'initial-context-baseline.json').read_text())
    report={'date':'2026-10-29','scope':'Local file/serialization audit; synthetic builder task, no model invocation or provider request capture.',
      'units':'Unicode characters and UTF-8 bytes; not token counts.',
      'baselineRoutingChain':{'files':['SKILL.md','references/workflow.md','references/handoff-contract.md','references/roles/builder.md'],
         'characters':sum(baseline['files'][s]['chars'] for s in ['SKILL.md','references/workflow.md','references/handoff-contract.md','references/roles/builder.md']),
         'qualification':'Possible eager reading chain, not observed automatic startup.'},
      'skillFiles':files,'syntheticBootstrapFile':size(wire(bootstrap)),
      'syntheticExpandedContextFile':size(wire(expanded)),
      'syntheticTaskFile':size(path.read_text()),
      'nextReads':['Assigned role card','Task file','Only currently needed task sources/inputs and required cross-references'],
      'bootstrapBudget':{'characters':2000,'covers':'Entire helper JSON file with wrapper, indentation and newline; excludes skill, task reads and platform context.'},
      'unknown':['Actual platform/system/developer/tool context size','Actual inherited conversation in previous runs',
                 'Model tokenizer and actual input token counts','Raw HTTP413 request/error payloads'],
      'notProven':['Weaker-model quality improvement','Elimination of provider HTTP413','Actual agent follows the read policy'],
      'officialReference':'https://learn.chatgpt.com/docs/build-skills'}
    out=Path(__file__).parent/'initial-context-audit.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['baselineRoutingChain','syntheticBootstrapFile','syntheticExpandedContextFile','syntheticTaskFile']}))
finally:case.doCleanups()
