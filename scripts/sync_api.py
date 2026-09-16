"""Generate or verify the bundled dxui public contract from a local source checkout."""
import argparse
import collections
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def generate(source):
    raw = subprocess.check_output(
        ['go', 'run', str(ROOT / 'scripts/api-scan.go'), str(source)]
    )
    entries = json.loads(raw)
    commit = subprocess.check_output(
        ['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True
    ).strip()
    dirty = bool(subprocess.check_output(
        ['git', '-C', str(source), 'status', '--porcelain'], text=True
    ).strip())
    groups = collections.defaultdict(list)
    for entry in entries:
        groups[entry['File']].append(entry)
    files = {}
    index = ['# Public API index', '',
             'Search by exact symbol name; open only the relevant reference file.', '',
             'Root entries use package `dxui`; icon entries use `icon` or `catalog`.',
             'Internal icon declarations describe types exposed through public aliases and return values; do not import internal packages.', '']
    for source_file, items in groups.items():
        filename = source_file.replace('/', '--').removesuffix('.go') + '.md'
        lines = [f'# {source_file}', '', 'Exact source declarations and comments. Private fields and function bodies are omitted.', '']
        seen = {}
        for entry in items:
            name = entry['Name']
            anchor = 'api-' + re.sub(r'[^a-z0-9-]', '-', name.lower())
            index.append(f'- `{entry["Package"]}: {name}`: [{source_file}](api/{filename}#{anchor})')
            lines += [f'<a id="{anchor}"></a>', f'## {name}', '',
                      f'Source: `{entry["File"]}:{entry["Line"]}`', '']
            if entry['Doc']:
                lines += ['```text', entry['Doc'].strip(), '```', '']
            code = entry['Code']
            if code and code not in seen:
                lines += ['```go', code, '```', '']
                seen[code] = anchor
            elif code:
                lines += [f'[Shared declaration](#{seen[code]}).', '']
            else:
                lines += ['See the preceding constant block for the exact value and type.', '']
        files[f'references/api/{filename}'] = '\n'.join(lines)
    files['references/api-index.md'] = '\n'.join(index) + '\n'
    files['references/api-snapshot.json'] = json.dumps(entries, ensure_ascii=False, indent=2) + '\n'
    counts = dict(collections.Counter(e['Package'] for e in entries))
    files['references/baseline.json'] = json.dumps(
        {'commit': commit, 'dirty': dirty, 'declarations': len(entries), 'packages': counts}, indent=2
    ) + '\n'
    return files, len(entries)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='Local github.com/dxui-org/dxui checkout')
    parser.add_argument('--check', action='store_true', help='Read-only drift check')
    args = parser.parse_args()
    source = args.source.resolve()
    if 'module github.com/dxui-org/dxui' not in (source / 'go.mod').read_text(encoding='utf-8'):
        parser.error('Source must be a dxui checkout')
    files, count = generate(source)
    expected = {ROOT / name for name in files}
    stale = set((ROOT / 'references/api').glob('*.md')) - expected
    changed = [name for name, content in files.items()
               if not (ROOT / name).exists() or (ROOT / name).read_text(encoding='utf-8') != content]
    if args.check:
        if changed or stale:
            raise SystemExit('API reference drift: ' + ', '.join(changed + [str(p) for p in stale]))
        print(f'Public API matches source: {count} declarations.')
        return
    for name, content in files.items():
        target = ROOT / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
    # Only stale generated Markdown directly inside the dedicated API directory.
    for target in stale:
        if target.resolve().parent != (ROOT / 'references/api').resolve():
            raise SystemExit('Refusing to remove a path outside the generated API directory')
        target.unlink()
    print(f'Generated {count} declarations. Review usage guidance and examples separately.')


if __name__ == '__main__':
    main()
