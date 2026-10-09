# CAPE stage-2 validation

Private workbook version history for Apoorv. PDFs, source instruction files, Excel lock files, and all non-allowlisted files remain local.

## Workflow

- The initial commit stores the unedited workbook.
- Assistant edits require explicit approval and are followed by a verified commit/push.
- A macOS LaunchAgent checks every 60 seconds for stable saved Excel changes (at least 10 seconds old). Unsaved edits and intermediate saves between checks are not captured. No AI bot or paid automation is used.
- `cape_stage2_validation.xlsx` is the authoritative artifact. `workbook_snapshot.json` provides readable cell values and `CHANGELOG.md` records changed cells. Formatting-only changes are preserved in the XLSX.
- The checker never writes to the workbook. Offline/authentication failures are logged and pushes retry on the next cycle. This is local-to-GitHub backup, not bidirectional syncing. Remote divergence stops a push; there are no force pushes.
- Keep this folder in place; moving it requires updating the LaunchAgent.

## Manual checkpoint

`/opt/anaconda3/bin/python version_workbook.py "Describe approved change"`

## Recovery

Retrieve any earlier workbook without overwriting the working file:

`git show COMMIT:cape_stage2_validation.xlsx > /path/to/recovered-version.xlsx`

Review the recovered file before replacing the working workbook. Close Excel before a deliberate restore. Do not reset history or force-push for ordinary recovery.

## Monitor

LaunchAgent label: `com.apoorv.cape-stage2-versioning`

Logs: `~/.hermes/profiles/econometrics-project-ra/logs/stage2-versioning.log` and `stage2-versioning.error.log`.

To temporarily pause versioning, create `.git/pause-versioning`; remove that file to resume. This pause file is never uploaded.
