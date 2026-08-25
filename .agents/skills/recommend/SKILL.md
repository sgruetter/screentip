---
name: recommend
description: Recommend one or more unseen Titles to watch, optionally steered by genre, mood, or direction. Use when the user asks what to watch, wants a Recommendation, or says /recommend. If they have already seen a pick, record the Stance they state and recommend another.
argument-hint: "[count] genre, mood, or direction"
---

# Recommend

Offer a **Recommendation**: unseen **Title**s only.

## Quick start

```
/recommend something tense but not bleak, weekday night, about 2 hours
```

## Workflow

1. Run `python3 .agents/scripts/taste.py list`. Those rows are **Stance**s. Everything else is unseen.
2. Parse count, genre, mood, or direction. Default to **one** **Title** unless they ask for more.
3. Pick **Title**s with no **Stance**. Never liked, disliked, or **Ignored**. A rewatch is not a **Recommendation**.
4. For each pick, give name, year, **Film** or **Series**, and why it fits the steer and their liked **Title**s.
5. If they already saw a pick: follow **Recording a Stance** in `AGENTS.md` with the **Stance** they state, then recommend another. Do not quiz. Do not invent `/ask` or `/refine`.
6. If they do not want a pick and have not judged it, that is **Ignored** (`set ignored`), then another **Recommendation**.

Do not commit unless you changed tracked files. Store edits stay local.
