---
name: like
description: Record a liked Stance on a Title (film or series) in the local taste store. Use when the user liked a film or series, enjoyed something they watched, or says /like.
argument-hint: Title (year)
---

# Like

Record **Stance** liked on a **Title**.

## Quick start

```
/like The Apartment (1960)
```

## Workflow

1. Follow **Recording a Stance** in `AGENTS.md` with `liked`.
2. If they have not seen it, that is **Ignored**, not liked. Say so and use `/ignore` instead if that is what they mean.
3. Do not commit. The store is gitignored.
