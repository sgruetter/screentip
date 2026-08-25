---
name: like
description: Record a liked Stance on a Title (film or series) in the local taste store. The user may give a name, a year, a description, or a mix. Use when the user liked a film or series, describes something they enjoyed watching, or says /like.
argument-hint: Title, year, or description
---

# Like

Record **Stance** liked on a **Title**.

## Quick start

```
/like The Apartment (1960)
/like the gerard butler submarine movie
```

## Workflow

1. Follow **Recording a Stance** in `AGENTS.md` with `liked`. Resolve descriptions and name collisions there. Do not record until the **Title** is identified.
2. If they have not seen it, that is **Ignored**, not liked. Say so and use `/ignore` instead if that is what they mean.
3. Do not commit. The store is gitignored.
