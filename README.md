# Screentip

Private taste. Public skills. A straight answer to *what should I watch next?*

Screentip is an agent workspace, not an app. You tell it films and series you like or dislike. It keeps that record in a local text file, then recommends what to watch — optionally steered by genre, mood, or a direction you name.

Your taste never leaves the machine. The file is gitignored and is not part of this repository.

Any coding agent that reads `AGENTS.md` and project skills can run it.

## Commands

Project skills live in `.agents/skills/`. Invoke them by name:

| Command | Purpose |
|---|---|
| `/like` | Add a film or series you liked |
| `/dislike` | Add a film or series you didn't |
| `/ask` | Answer a probe about something you might have seen, so the picture of your taste gets sharper |
| `/recommend` | Get one or more things to watch. Pass a genre, mood, or direction if you have one |

Examples:

```
/like The Apartment (1960)
/dislike a show that wasted a great premise after season one
/ask
/recommend something tense but not bleak, weekday night, about 2 hours
```

## Layout

| Path | Role |
|---|---|
| `AGENTS.md` | Rules every agent in this repo should follow |
| `CONTEXT.md` | Domain language |
| `.agents/skills/` | `/like`, `/dislike`, `/ask`, `/recommend` |
| `data/taste.txt` | Local taste store (gitignored) |

## Taste store

Likes and dislikes live in `data/taste.txt` on your machine. Clone the repo and that file is yours to fill; it is not committed, not pushed, and not shared.

The repository is the system: skills, language, and how the agent should work. The taste is personal.

## Setup

```bash
git clone git@github.com:sgruetter/screentip.git
cd screentip
```

Open the repo in your coding agent. Start with `/like`, `/dislike`, or `/ask`. No account, no database server, no vendor lock-in.

## License

Private taste, public repo. Use the skills; keep your own store.
