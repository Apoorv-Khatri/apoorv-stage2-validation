"""Version stable workbook saves, push, and verify remote HEAD. Never edit workbook."""
from pathlib import Path
import subprocess, json, hashlib, time, sys, io, os, fcntl
from datetime import datetime, timezone
import openpyxl
ROOT = Path(__file__).resolve().parent
BOOK = ROOT / 'cape_stage2_validation.xlsx'
FILES = ['.gitignore', 'README.md', 'CHANGELOG.md', 'cape_stage2_validation.xlsx', 'workbook_snapshot.json', 'version_workbook.py']
os.environ['PATH'] = '/opt/homebrew/bin:/opt/anaconda3/bin:/usr/bin:/bin:/usr/sbin:/sbin:' + os.environ.get('PATH', '')
os.environ['GIT_TERMINAL_PROMPT'] = '0'
def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True, stderr=subprocess.STDOUT, timeout=90).strip()
def snapshot(raw):
    wb = openpyxl.load_workbook(io.BytesIO(raw), data_only=False)
    return {s.title: {c.coordinate: c.value for row in s for c in row if c.value is not None} for s in wb}
def main():
    with (ROOT / '.git' / 'workbook-version.lock').open('w') as lock:
        try: fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError: return
        if (ROOT / '.git' / 'pause-versioning').exists(): return
        reason = sys.argv[1] if len(sys.argv) > 1 else 'Saved Excel changes'
        if reason == 'Saved Excel changes' and time.time() - BOOK.stat().st_mtime < 10:
            print('Save still recent; deferring.'); return
        raw = BOOK.read_bytes()
        current = snapshot(raw)
        # Reject partial/changing saves, and never stage papers or arbitrary new files.
        if BOOK.read_bytes() != raw: print('Workbook changing; deferring.'); return
        oldpath = ROOT / 'workbook_snapshot.json'
        old = json.loads(oldpath.read_text()) if oldpath.exists() else {}
        new = json.loads(json.dumps(current, ensure_ascii=False, default=str))
        changes = []
        for sheet in sorted(set(old) | set(new)):
            a, b = old.get(sheet, {}), new.get(sheet, {})
            for cell in sorted(set(a) | set(b)):
                if a.get(cell) != b.get(cell):
                    changes.append({'sheet': sheet, 'cell': cell, 'before': a.get(cell), 'after': b.get(cell)})
        if git('status', '--porcelain', '--', *FILES):
            oldpath.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
            stamp = datetime.now(timezone.utc).isoformat()
            log = ROOT / 'CHANGELOG.md'
            with log.open('a') as f:
                f.write('\n## ' + stamp + ' — ' + reason.replace('\n', ' ') + '\n\n')
                if not old:
                    f.write('Baseline of the original workbook before the approved OLS split.\n')
                else:
                    f.write(f'{len(changes)} populated-cell value changes. The XLSX also preserves formatting.\n\n')
                    if changes: f.write('```json\n' + json.dumps(changes, ensure_ascii=False, indent=2) + '\n```\n')
            if BOOK.read_bytes() != raw: raise RuntimeError('Workbook changed before staging; retry next cycle')
            git('add', '--', *FILES)
            staged = subprocess.check_output(['git', '-C', str(ROOT), 'show', ':cape_stage2_validation.xlsx'])
            if hashlib.sha256(staged).digest() != hashlib.sha256(raw).digest():
                git('reset', '--', *FILES)
                raise RuntimeError('Workbook changed during staging; deferred')
            staged_files = git('diff', '--cached', '--name-only').splitlines()
            if any(p not in FILES for p in staged_files): raise RuntimeError('Unapproved staged file; refusing commit')
            git('commit', '-m', reason)
        git('push', '-u', 'origin', 'main')
        local = git('rev-parse', 'HEAD')
        remote = git('ls-remote', 'origin', 'refs/heads/main').split()[0]
        if local != remote: raise RuntimeError('Remote HEAD does not match local HEAD')
        print('VERIFIED remote main:', local, flush=True)
if __name__ == '__main__':
    try: main()
    except Exception as e:
        print('VERSIONING ERROR:', str(e), file=sys.stderr, flush=True)
        sys.exit(1)
