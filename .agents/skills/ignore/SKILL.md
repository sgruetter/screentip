---
name: ignore
description: Record an Ignored Stance on a Title without judging it liked or disliked. Use when the user is not interested in a film or series, wants it set aside, or says /ignore.
argument-hint: Title (year)
---

# Ignore

Record **Ignored** on a **Title**.

## Quick start

```
/ignore Twilight (2008)
```

## Workflow

1. Follow **Recording a Stance** in `AGENTS.md` with `ignored`.
2. **Ignored** is not disliked. Do not record disliked because they are uninterested.
3. Applies only to a **Title**, never to a kind (superhero, horror). A kind may steer `/tip`; it is not **Ignored**.
4. Do not commit. The store is gitignored.
