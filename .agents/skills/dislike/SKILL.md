---
name: dislike
description: Record a disliked Stance on a Title (film or series) in the local taste store. The user may give a name, a year, a description, or a mix. Use when the user disliked a film or series they watched, describes something they hated, or says /dislike.
argument-hint: Title, year, or description
---

# Dislike

Record **Stance** disliked on a **Title**.

## Quick start

```
/dislike Cats (2019)
/dislike that musical about cats that everyone roasted
```

## Workflow

1. Follow **Recording a Stance** in `AGENTS.md` with `disliked`. Resolve descriptions and name collisions there. Do not record until the **Title** is identified.
2. Disliked means seen and judged. If they have not seen it and do not want to, that is **Ignored**. Say so and use `/ignore` if that is what they mean.
3. Do not commit. The store is gitignored.
