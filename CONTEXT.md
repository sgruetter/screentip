# Screentip

Personal taste over films and series: which **Title**s are liked, disliked, or **Ignored**, so an agent can offer a **Tip** for what to watch next.

## Language

**Title**:
A complete **Film** or a complete **Series**, identified by name and year. It is the thing liked, disliked, **Ignored**, or offered as a **Tip**. A season or episode is not a **Title**. When name and year match, **Film** vs **Series** distinguishes them.
_Avoid_: watchable, work, entry, item, season, episode

**Film**:
A **Title** released as a movie. Each film in a franchise is its own **Title**.
_Avoid_: picture

**Series**:
A **Title** released as a television or streaming show. The whole run is one **Title**, including anthologies.
_Avoid_: TV show, programme

**Stance**:
The user's recorded position on one **Title**: liked, disliked, or **Ignored**. Stated by naming a **Title**, or as a reply to a **Tip**. Never inferred. One per **Title**: a later statement replaces the earlier. A **Title** with no **Stance** is unseen.
_Avoid_: rating, review, verdict, status, history

**Ignored**:
A **Stance** on a **Title**: set aside without being liked or disliked. The user is not interested in it, and does not claim to know whether they would like it. Applies only to a **Title**, never to a kind of thing.
_Avoid_: not interested, skip, pass, dismissed, hidden, uninterested, unseen

**Tip**:
One or more unseen **Titles** offered to watch, optionally steered by a kind, genre, or mood. Never a **Title** that already has a **Stance**; if the user has already seen it, they state a **Stance** and another **Tip** follows.
_Avoid_: recommendation, rec, rewatch, watchlist, pick, quiz, ask, refine

## Example dialogue

Dev: They liked *The Apartment*. Is that a **Title** or a **Film**?

Expert: Both. *The Apartment* is a **Title**. It is a **Film**. Every **Title** is one **Film** or one **Series**.

Dev: They liked *True Detective* season 1 and not season 2. Two **Title**s?

Expert: No. *True Detective* is one **Series**, so one **Title**, so one **Stance**. A season is not a **Title**.

Dev: *John Wick* and *John Wick: Chapter 4*?

Expert: Two **Film**s, two **Title**s. A franchise is not one **Title**.

Dev: Two *Dune*s. Two *The Office*s. Same name?

Expert: Different years, so different **Title**s. Name and year identify them. If name and year still match, **Film** vs **Series** does.

Dev: They haven't seen *The Third Man*. Do they have a **Stance**?

Expert: No. Unseen is the absence of a **Stance**. They did not state one, so nothing is recorded.

Dev: They name *Twilight* and say they are not interested; they have not watched it, so they do not dislike it.

Expert: That is **Ignored**, stated by naming a **Title**. Not disliked. Not only a reply to a **Tip**.

Dev: They later watch *Twilight* and like it.

Expert: The new **Stance** is liked. **Ignored** is gone. One **Stance** per **Title**, no history.

Dev: They say they do not do superhero movies.

Expert: That is not a **Stance**. Superhero is not a **Title**. **Ignored** only applies to a **Title**. A kind of thing can steer a **Tip**; it is not recorded as **Ignored**.

Dev: Friday night. *The Apartment* is liked, *Twilight* is **Ignored**, *Cats* is disliked. Can any of those be a **Tip**?

Expert: No. A **Tip** is only an unseen **Title**. Liked, disliked, and **Ignored** are already judged. A rewatch is not a **Tip**.

Dev: A **Tip** names a **Title** they already saw.

Expert: They state a **Stance**. Then another **Tip**. That is not a quiz. There is no quiz.
