#!/usr/bin/env python3
"""Local taste ledger. One home for the data/taste.txt format.

Each line is tab-separated: stance, kind, year, name
  stance: liked | disliked | ignored
  kind:   film | series
  year:   four-digit first-release year
  name:   Title name (may contain spaces)

Identity is kind + year + name (case-insensitive). set replaces Stance.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

STANCES = ("liked", "disliked", "ignored")
KINDS = ("film", "series")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def store_path() -> Path:
    return repo_root() / "data" / "taste.txt"


def key_of(kind: str, year: str, name: str) -> tuple[str, str, str]:
    return (kind, year, name.casefold())


def parse_line(line: str) -> tuple[str, str, str, str] | None:
    raw = line.rstrip("\n")
    if not raw.strip() or raw.lstrip().startswith("#"):
        return None
    parts = raw.split("\t")
    if len(parts) != 4:
        raise ValueError(f"bad line (need 4 tab-separated fields): {raw!r}")
    stance, kind, year, name = (p.strip() for p in parts)
    if stance not in STANCES or kind not in KINDS:
        raise ValueError(f"bad stance or kind: {raw!r}")
    if not (len(year) == 4 and year.isdigit()):
        raise ValueError(f"bad year: {raw!r}")
    if not name:
        raise ValueError(f"missing name: {raw!r}")
    return stance, kind, year, name


def format_line(stance: str, kind: str, year: str, name: str) -> str:
    return f"{stance}\t{kind}\t{year}\t{name}\n"


def load(path: Path) -> list[tuple[str, str, str, str]]:
    if not path.exists():
        return []
    rows: list[tuple[str, str, str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines(True):
        parsed = parse_line(line)
        if parsed is not None:
            rows.append(parsed)
    return rows


def save(path: Path, rows: list[tuple[str, str, str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = "".join(format_line(*row) for row in rows)
    path.write_text(body, encoding="utf-8")


def cmd_list(_args: argparse.Namespace) -> int:
    rows = load(store_path())
    sys.stdout.write("".join(format_line(*row) for row in rows))
    return 0


def cmd_set(args: argparse.Namespace) -> int:
    stance = args.stance
    kind = args.kind
    year = args.year
    name = " ".join(args.name).strip()
    if stance not in STANCES:
        print(f"error: stance must be one of {', '.join(STANCES)}", file=sys.stderr)
        return 1
    if kind not in KINDS:
        print(f"error: kind must be one of {', '.join(KINDS)}", file=sys.stderr)
        return 1
    if not (len(year) == 4 and year.isdigit()):
        print("error: year must be four digits", file=sys.stderr)
        return 1
    if not name:
        print("error: name is required", file=sys.stderr)
        return 1

    path = store_path()
    rows = load(path)
    target = key_of(kind, year, name)
    replaced: str | None = None
    found = False
    new_rows: list[tuple[str, str, str, str]] = []
    for row in rows:
        if key_of(row[1], row[2], row[3]) == target:
            found = True
            if row[0] != stance:
                replaced = row[0]
            new_rows.append((stance, kind, year, name))
        else:
            new_rows.append(row)
    if not found:
        new_rows.append((stance, kind, year, name))
    save(path, new_rows)
    sys.stdout.write(format_line(stance, kind, year, name))
    if replaced:
        print(f"replaced {replaced}", file=sys.stderr)
    elif found:
        print("unchanged", file=sys.stderr)
    else:
        print("added", file=sys.stderr)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read and write the local taste store.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="print the store as TSV").set_defaults(func=cmd_list)
    set_p = sub.add_parser("set", help="upsert a Stance on a Title")
    set_p.add_argument("stance", choices=STANCES)
    set_p.add_argument("kind", choices=KINDS)
    set_p.add_argument("year")
    set_p.add_argument("name", nargs="+")
    set_p.set_defaults(func=cmd_set)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return args.func(args)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
