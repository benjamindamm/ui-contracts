from pathlib import Path
import json,re,collections,hashlib,shutil,zipfile
root=Path('/Users/kcnpxcp/Dev/GitHub/ui-contracts');p=root/'docs/research';s=json.loads((p/'study.json').read_text());h=lambda f:hashlib.sha256(f.read_bytes()).hexdigest();evaluations=s['evaluations'];assert len(evaluations)==416 and len({(e['candidate'],e['requirement'])for e in evaluations})==416
claims={c['id']:c for c in s['claims']};assert len(claims)==len(s['claims'])==543;u=[e for e in evaluations if e['coverage']=='U'];assert len(u)==2 and sum(e['requirement'].startswith('X')for e in u)==2
links=re.findall(r'\[([DRANU])/(C\d+)\]\(CLAIMS.md#c\d+\)',(p/'MATRIX.md').read_text());assert len(links)==416 and collections.Counter(links)==collections.Counter((e['coverage'],e['claim'])for e in evaluations)
open_rows=[l for l in (p/'OPEN-FIELDS.md').read_text().splitlines()if l.startswith(('| P1 |','| P2 |'))];assert len(open_rows)==2;assert {(l.split('|')[2].strip(),l.split('|')[3].strip())for l in open_rows}=={(e['candidate'],e['requirement'])for e in u}
assert sum(t['cases']for t in s['runtime_trials'])==702 and len(s['runtime_trials'])==106
for t in s['runtime_trials']:
 assert(p/t['record']).is_file(),t
 if t.get('additional_record'):assert(p/t['additional_record']).is_file(),t
 if t.get('report'):assert(p/t['report']).is_file(),t
for t in s['runtime_trials'][:102][-7:]:
 record=json.loads((p/t['record']).read_text());assert len(record['cases'])==t['cases'],t
 if t['id']=='P84':assert sum(not c['expectationMet']for c in record['cases'])==2 and t['exit_status']==1
 else:assert all(c['expectationMet']for c in record['cases']),t
for c in s['claims']:assert f"## {c['id']}\n"in(p/'CLAIMS.md').read_text()
for candidate in dict.fromkeys(e['candidate']for e in evaluations):
 ev=[e for e in evaluations if e['candidate']==candidate];counts=collections.Counter(e['coverage']for e in ev);line='| '+candidate+' | '+' | '.join(str(counts[k])for k in 'DRANU')+' |';assert line in(p/'CURRENT-STATUS.md').read_text(),line
plan=json.loads((p/'REMAINDER-PLAN.json').read_text());assert plan['remaining_cells']==2 and len(plan['baseline_cells'])==46 and len(plan['closed_since_baseline'])==44;assert plan['class_counts']=={'a':0,'b':2,'c':0};assert {(c['candidate'],c['requirement'],c['current_claim'])for c in plan['cells']}=={(e['candidate'],e['requirement'],e['claim'])for e in u}
review=json.loads((p/'experiments/2026-10-25/remaining-29-review/results.json').read_text());assert len(review['cells'])==29 and sum(c['coverage_after']=='U'for c in review['cells'])==20;assert review['all_29_have_individual_disposition']
for c in review['cells']:assert h(p/c['evidence_report'])==c['report_sha256']
newmanifests=[]
for name in ['apg-mode-ownership','domain-independence-final','apg-independence','google-independence','openui-independence','op-slider-geometry','css-complement-runtime','uspec-cem-ownership','uspec-api-independence','op-four-masters','layout-final-bindings','ip01-lifecycle','ip01-followup','ip01-static','ip01-browser']:
 d=p/'experiments/2026-10-25'/name;m=json.loads((d/'source-manifest.json').read_text());assert h(p/'METHODS.md')==m['method_sha256']and h(p/'REQUIREMENTS.md')==m['requirements_sha256'];assert not m['original_code_modified']
 for own in m['own_files']:assert h(d/own['file'])==own['sha256'],(name,own)
 for original in m['original_files']:assert h(Path(original['local_provenance_path']))==original['sha256'],(name,original)
 newmanifests.append(name)
# New key claims/source anchors and all local Markdown targets must resolve.
for n in range(115,130):assert f'## S{n}\n'in(p/'SOURCES.md').read_text()
errors=[]
for f in [root/'README.md',root/'TASKS.md',*p.rglob('*.md')]:
 for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',f.read_text()):
  if target.startswith(('http:','https:','#','mailto:')):continue
  target=target.split('#')[0]
  if target and not(f.parent/target).exists():errors.append((str(f.relative_to(root)),target))
assert not errors,errors
assert '2 U-Zellen: 2 Integration und 0 weitere'in(p/'MATRIX.md').read_text()
css=json.loads((p/'experiments/2026-10-25/css-complement-runtime/results.json').read_text());assert len(css['cases'])==27 and all(c['expectationMet']for c in css['cases'])
rest=json.loads((p/'experiments/2026-10-25/css-complement-runtime/remaining-10.json').read_text());assert len(rest['cells'])==10 and rest['independently_investigable']==8 and rest['named_original_clarifications']==2
assert len({(x['candidate'],x['requirement'])for x in rest['cells']})==10
assert {(e['candidate'],e['requirement'],e['claim'])for e in u}=={('Google DESIGN.md','X06','C483'),('OpenUI','X06','C484')}
auto=json.loads((p/'experiments/2026-10-25/autonomous-8-review/results.json').read_text());assert len(auto['cells'])==8 and auto['remaining_u']==2 and auto['new_conditions']==38
for c in auto['cells']:assert h(p/c['report'])==c['report_sha256']
assert sum(t['cases']for t in s['runtime_trials'][:102][-7:])==38
p84=next(t for t in s['runtime_trials']if t['id']=='P84');assert sum(not c['expectationMet']for c in json.loads((p/p84['record']).read_text())['cases'])==2
life=json.loads((p/'experiments/2026-10-25/ip01-lifecycle/results.json').read_text());assert len(life['cases'])==8
assert [c['expectationMet']for c in life['cases']]==[True,True,True,True,True,False,False,True]
assert next(t for t in s['runtime_trials']if t['id']=='P103')['exit_status']==1
for c in life['cases']:assert c['journal'] and c['observed'] and c['cleanup']
sub=next(e['subcases']for e in life['cases'][6]['journal']if e['type']=='failure-subcases');assert len(sub)==2 and all(x['cleanup']for x in sub)
idx=json.loads((p/'INTEGRATION-PROFILE-EVIDENCE.json').read_text())
for e in idx['entries']:assert h(p/e['path'])==e['sha256']
follow=json.loads((p/'experiments/2026-10-25/ip01-followup/variant-results.json').read_text());reg=json.loads((p/'experiments/2026-10-25/ip01-followup/results.json').read_text())
assert len(follow['cases'])==6 and len(reg['cases'])==8 and all(c['expectationMet']for c in follow['cases']+reg['cases'])
assert all(not c['unhandledRejections']for c in follow['cases']+reg['cases'])
assert next(t for t in s['runtime_trials']if t['id']=='P104')['cases']==6
staticdir=p/'experiments/2026-10-25/ip01-static';static=json.loads((staticdir/'results.json').read_text());assert len(static['cases'])==27 and all(c['expectationMet']for c in static['cases'])
baseline={str(f.relative_to(staticdir/'reference')):f.read_text()for f in(staticdir/'reference').rglob('*')if f.is_file()and f.name!='resolved.json'}
htext=lambda text:hashlib.sha256(text.encode()).hexdigest()
for c in static['cases']:
 d=staticdir/'runs'/c['id'];files={**baseline,**json.loads((d/'patch.json').read_text())};lock=json.loads((d/'resolved.json').read_text());assert {name:htext(value)for name,value in sorted(files.items())}==lock['files'];assert htext(json.dumps(lock['files'],sort_keys=True,separators=(',',':')))==lock['revision']
 b=json.loads(files['bindings.json'])
 if c['id']!='ST-12':assert all(htext(files[src['path']])==src['sha256']for src in b['sources'])
 if c['id']=='ST-25':assert c['actual']=='REVISION_MISMATCH'
assert json.loads((staticdir/'runs/ST-01/resolved.json').read_text())['revision']!=json.loads((staticdir/'runs/ST-02/resolved.json').read_text())['revision']
assert len(static['cases'][0]['originalChecks'])==6 and all(x['accepted']for x in static['cases'][0]['originalChecks'])
assert len(static['cases'][0]['visualBindings'])==3
b=json.loads(baseline['bindings.json']);assert h((staticdir/'reference'/b['runtimeCandidate']['adapter']).resolve())==b['runtimeCandidate']['adapterSha256']
manifest=json.loads((staticdir/'source-manifest.json').read_text())
for dep in manifest['research_dependencies']:assert h((staticdir/dep['file']).resolve())==dep['sha256']
browserdir=p/'experiments/2026-10-25/ip01-browser';run=json.loads((browserdir/'results.json').read_text());assert len(run['cases'])==20 and all(c['expectationMet']for c in run['cases'])
manifest=json.loads((browserdir/'host/manifest.json').read_text());assert len({c['sourceRevision']for c in run['cases']})==1 and run['sourceRevision']==manifest['revision']
for file,expected in manifest['files'].items():
 if not file.startswith('vendor/'):assert h(browserdir/'host'/file)==expected
assert htext(json.dumps(manifest['files'],sort_keys=True,separators=(',',':')))==manifest['revision']
for c in run['cases']:assert (browserdir/c['record']).is_file()
last=json.loads((browserdir/'captures/BR-20.json').read_text());assert not last['snapshot']['errors'] and all(a['final']for a in last['snapshot']['actors'])
assert all(last['payload']['hashes'].values())
assert not run['screen_reader_tested'] and not run['real_ime_tested'] and not run['native_platforms_tested']
assert json.loads((browserdir/'shutdown.json').read_text())['test_server_stopped']
assert any(e['event'].get('data',{}).get('reason','').find('label')>=0 for e in json.loads((browserdir/'captures-initial/BR-06.json').read_text())['snapshot']['errors']if 'event'in e)
assert json.loads((browserdir/'captures-before-status-fix/AX-closed.json').read_text())['snapshot']['A']['status']=='Ergebnisse werden geladen.'
# This is a documentation bundle; original binaries, node_modules and generated third-party bundles are not copied.
out=Path('outputs');mirror=out/'ui-contracts';mirror.mkdir(parents=True,exist_ok=True)
for name in ['README.md','TASKS.md']:shutil.copyfile(root/name,mirror/name)
shutil.copytree(root/'docs',mirror/'docs',dirs_exist_ok=True)
with zipfile.ZipFile(out/'UI-Contracts-Dokumentation.zip','w',zipfile.ZIP_DEFLATED)as z:
 for f in sorted(mirror.rglob('*')):
  if f.is_file():z.write(f,'ui-contracts/'+str(f.relative_to(mirror)))
with zipfile.ZipFile(out/'UI-Contracts-Dokumentation.zip')as z:assert z.testzip()is None
report={'evaluations':416,'claims':543,'remaining_u':2,'remaining_integration_u':2,'remaining_other_u':0,'probe_groups':106,'probe_conditions':702,'this_block_baseline_u':29,'this_block_individually_assessed':29,'this_block_new_conditions':26,'this_block_new_groups':10,'this_block_newly_reclassified_cells':9,'this_block_final_positive_expectations_met':24,'this_block_preserved_original_ssr_expectation_failures':2,'this_block_final_expectations_all_met':False,'this_block_own_initial_errors_preserved':True,'baseline_rows_verified':46,'closed_since_baseline_verified':26,'active_queue_rows_verified':20,'independently_investigable_remaining':18,'named_original_clarifications_remaining':2,'relative_link_errors':0,'new_manifests_verified':newmanifests,'original_dependency_inventory_verified':{'openpencil':9941,'zag_ark':7555},'full_four_domain_integration_proven':False,'new_production_component_implemented':False,'native_research_hosts_executed':True,'whole_editor_executed':False,'physical_keyboard_tested':False,'at_tested':False,'commit_created':False,'push_performed':False,'historical_progress_preserved_separately':True}
report.update({'latest_block_baseline_u':20,'latest_block_individually_justified_cells':10,'latest_block_new_conditions':27,'latest_block_new_groups':10,'latest_block_newly_reclassified_cells':10,'latest_block_final_expectations_met':27,'latest_block_final_expectations_all_met':True,'latest_block_actual_original_scxml_executed':True,'latest_block_actual_native_geometry_focus_and_ax':True,'latest_block_original_query42_accepted_before_additional_check':True,'latest_block_clip_remains_valid_css':True,'latest_block_cem_scxml_original_schema_preflight_valid':True,'latest_block_primary_normative_sources_read':True,'active_queue_rows_verified':10,'closed_since_baseline_verified':36,'independently_investigable_remaining':8,'named_original_clarifications_remaining':2})
previous={key.removeprefix('this_block_'):report.pop(key)for key in list(report)if key.startswith('this_block_')}
report['previous_29_cell_block']=previous
report['all_prior_ssr_counterexamples_preserved']=True
for key in list(report):
 if key.startswith('latest_block_'):report.pop(key)
report.update({'latest_block_baseline_u':10,'latest_block_autonomous_cells':8,'latest_block_individually_justified_cells':8,'latest_block_new_conditions':38,'latest_block_new_groups':7,'latest_block_newly_reclassified_cells':8,'latest_block_final_expectations_met':38,'latest_block_final_expectations_all_met':True,'latest_block_initial_scroll_expectation_failure_preserved':True,'original_code_modified':False,'active_queue_rows_verified':2,'closed_since_baseline_verified':44,'independently_investigable_remaining':0,'named_original_clarifications_remaining':2,'authors_contacted':False,'new_product_format_selected':False})
report['ip01_lifecycle']={'cases':8,'expectations_met':6,'expectations_violated':2,'complete_ip_a05_a06_passed':False};report['ip01_followup']={'new_conditions':6,'new_expectations_met':6,'regression_cases':8,'regression_expectations_met':8,'regressions_counted_again':0,'full_ip_gate_passed':False};report['ip01_static']={'new_conditions':27,'expectations_met':27,'all_hash_closures_reconstructed':True,'semantic_negatives_repinned':True,'full_runtime_executed':False};report['ip01_browser']={'conditions':20,'expectations_met':20,'trusted_browser_keyboard':True,'actual_dom_focus_scroll_ax':True,'screen_reader_tested':False,'native_platforms_tested':False,'full_ip_profile_passed':False,'own_initial_failures_preserved':True,'test_server_stopped':True,'round_closed':True};(out/'documentation-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
