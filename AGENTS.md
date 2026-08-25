# Screentip

Personal tracker for **Title**s the user likes, dislikes, or **Ignored**. Language: `CONTEXT.md`. Skills: `.agents/skills/`. Do not put skills under a vendor path (`.grok/`, `.claude/`, `.cursor/`).

## Taste store

Gitignored file `data/taste.txt`. Create on first write. Never commit it. Never `git add -f` it. Ledger-only edits stay local: skip commit and push.

One **Title** per line, tab-separated:

```
stance<TAB>kind<TAB>year<TAB>name
```

- `stance`: `liked` | `disliked` | `ignored`
- `kind`: `film` | `series`
- `year`: four-digit first-release year
- `name`: the **Title** name (spaces allowed)

Identity is kind + year + name (case-insensitive). A later **Stance** replaces the earlier.

Mutate only via:

```
python3 .agents/scripts/taste.py list
python3 .agents/scripts/taste.py set <liked|disliked|ignored> <film|series> <year> <name>
```

Do not hand-edit the file from a skill.

## Recording a Stance

Follow this for `/like`, `/dislike`, `/ignore`, and for a **Stance** stated on a **Tip**.

1. Read `CONTEXT.md` if terms are unclear.
2. Resolve the **Title**. Input may be a name, a year, a description, or a mix.
   - Look it up. Search when the name is missing, partial, descriptive, or could collide.
   - Identity is name + year + **Film** or **Series**.
   - If one **Title** is clearly meant, use it.
   - If it is still ambiguous after research, or two **Title**s share a name: do not record. Offer numbered options. Each option is name, year, **Film** or **Series**, and one distinguishing fact (cast, premise, origin). Wait for a pick. Do not guess.
3. `liked` and `disliked` mean seen and judged. **Ignored** means set aside without that judgment. If the user used the wrong skill, say so and record the **Stance** they actually meant — do not guess in silence.
4. Run `set` as above. Tell them the **Stance**, and whether it replaced one.

## Skills

| Skill | Stance / job |
|---|---|
| `/like` | liked |
| `/dislike` | disliked |
| `/ignore` | **Ignored** |
| `/tip` | **Tip** (unseen only; a seen pick takes a **Stance** then another **Tip**) |

There is no `/ask`, `/refine`, or `/recommend`.

## Git

After every completed change to tracked files, commit and push to `origin` on the current branch. Do not ask for confirmation. Do not wait for the user to request a commit.

- Stage only tracked paths.
- Write a short commit message that says what changed.
- If the branch has no upstream, `git push -u origin HEAD`. Otherwise `git push`.
- If there is nothing to commit, do not push.
