"""Small CLI readback; full evidence is opt-in or written exclusively to a new report."""
import hashlib
import json
from pathlib import Path


def emit(result, repo, output=None, details=False):
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    summary = {key: result[key] for key in ['overall', 'release', 'scope', 'library', 'libraryRevision', 'choice',
               'decisionStatus', 'componentCount', 'targetValidationRequired', 'statusCounts'] if key in result}
    if 'components' in result:
        summary['components'] = {name: value['status'] for name, value in result['components'].items()}
    if 'assessment' in result:
        summary['reason'] = result['assessment'].get('reason')
    if 'diagnostic' in result:
        diagnostic = result['diagnostic']
        if isinstance(diagnostic, dict):
            summary['diagnostic'] = {'code': diagnostic.get('code'), 'detail': str(diagnostic.get('detail', ''))[:500]}
        else:
            summary['diagnostic'] = str(diagnostic)[:500]
    if result.get('errors'):
        summary['errorCount'] = len(result['errors'])
        summary['errors'] = [{key: str(error.get(key, ''))[:200] for key in ['code', 'file', 'detail']} for error in result['errors'][:3]]
    if output:
        path = Path(output).resolve()
        if any(path.is_relative_to(Path(repo).resolve() / name) for name in ['libraries', 'tools', 'skills', 'examples', 'docs/research', 'docs/libraries/frozen']):
            raise ValueError('Report must be outside source/historical directories; use a new temporary file.')
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('x', encoding='utf-8') as file:
            file.write(text)
        summary['report'] = {'path': str(path), 'sha256': hashlib.sha256(text.encode()).hexdigest()}
    else:
        summary['details'] = 'Use --output NEW_FILE for evidence or --details for explicit full readback.'
    print(text if details else json.dumps(summary, ensure_ascii=False, indent=2), end='' if details else '\n')
