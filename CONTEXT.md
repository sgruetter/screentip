# Screentip

Personal taste over films and series: which **Title**s are liked, disliked, or still unseen, so an agent can recommend what to watch next.

## Language

**Title**:
A **Film** or a **Series**, identified by name. It is the thing liked, disliked, asked about, or recommended.
_Avoid_: watchable, work, entry, item

**Film**:
A **Title** released as a movie.
_Avoid_: picture

**Series**:
A **Title** released as a television or streaming show.
_Avoid_: TV show, programme

**Stance**:
The user's position on one **Title**: liked, disliked, or unseen.
_Avoid_: rating, review, verdict, status

## Flagged ambiguities

**Title vs name.** The everyday name is how a **Title** is pointed at. Two **Title**s can share a name (two *The Office*s, two *Dune*s). Identity beyond the name is not resolved.

**Unseen vs missing.** Unseen is a **Stance** the user can state. Whether that is written into the store, or is simply the default for any **Title** not liked or disliked, is not resolved.

## Example dialogue

Dev: They liked *The Apartment*. Is that a **Title** or a **Film**?

Expert: Both. *The Apartment* is a **Title**. It is a **Film**. Every **Title** is one **Film** or one **Series**.

Dev: They said the **Title** is the name. So the string "The Apartment" is the **Title**?

Expert: No. The **Title** is the film. The name is how we refer to it. If two **Title**s share a name, the name alone is not enough.

Dev: They haven't seen *The Third Man*. Do they have a **Stance**?

Expert: They can say unseen. Whether we record that, or treat it as "no liked/disliked record", is still open.
