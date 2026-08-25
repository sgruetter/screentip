# Screentip

Personal tracker for films and series the user likes or dislikes. Domain language lives in `CONTEXT.md`. Project skills live in `.grok/skills/`.

## Taste store

The store is a gitignored text file at `data/taste.txt`. Create it on first write if it is missing.

- Never commit it.
- Never `git add -f` it.
- Ledger-only edits stay local: skip commit and push.

## Git

After every completed change to tracked files, commit and push to `origin` on the current branch. Do not ask for confirmation. Do not wait for the user to request a commit.

- Stage only tracked paths.
- Write a short commit message that says what changed.
- If the branch has no upstream, `git push -u origin HEAD`. Otherwise `git push`.
- If there is nothing to commit, do not push.
