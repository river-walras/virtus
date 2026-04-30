---
name: git-auto-release
description: Review git changes first, then create an appropriate commit, create or choose a release tag, and push the branch and tag. Use when the user asks to auto commit, tag, push, publish a release tag, or prepare a git-based release after local changes are ready.
---

# Git Auto Release

## Workflow

1. Inspect repository state before changing anything:
   - Run `git status --short --branch`.
   - Run `git diff --stat`.
   - Run `git diff`.
   - If staged changes exist, also run `git diff --staged --stat` and `git diff --staged`.

2. Decide whether to continue:
   - Continue automatically only when the changed files match the user's request and the diff is coherent.
   - Stop and ask when the working tree contains unrelated changes, secrets, generated clutter, merge conflicts, or changes whose purpose is unclear.
   - Stop when no commit-worthy changes exist.

3. Run repo checks before committing when the repository documents them:
   - Prefer commands from `AGENTS.md`, README, or existing CI.
   - For `uv` Python repositories, use documented commands such as `uv run pytest` and `uv run ruff check .`.
   - If checks fail because of environment permissions or missing external services, report that clearly and do not hide the failure.

4. Stage and commit:
   - Stage only files that belong to the inspected change.
   - Use a concise imperative commit message that describes the actual diff.
   - Do not amend, squash, rebase, or rewrite history unless the user explicitly asks.

5. Choose the tag:
   - If the user supplied a tag, use it.
   - For Python packages with `pyproject.toml`, read `[project].version` and use `v<version>`.
   - If that tag already exists locally or remotely, stop and ask before deleting, moving, or replacing it.
   - If there is no reliable version source, ask the user for the tag name.

6. Create and push:
   - Create an annotated tag with `git tag -a <tag> -m <tag>`.
   - Push the current branch with `git push origin HEAD`.
   - Push the tag with `git push origin <tag>`.

## Safety Rules

- Always run and inspect `git diff` before committing.
- Never commit files that were not reviewed in the diff.
- Never push when the commit failed, checks failed, or tag selection is ambiguous.
- Never use destructive commands such as `git reset --hard`, `git checkout --`, or tag deletion unless the user explicitly requests them.
- Preserve unrelated user changes by leaving them unstaged.

## Final Response

Report:

- Commit hash and commit message.
- Tag name.
- Branch pushed.
- Check results, including any checks that could not be run.
