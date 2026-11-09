"""Build the play test checklist (design/playtest-checklist.md) from design/playtest.yaml and the card files.

Usage: python scripts/build_playtest_md.py

Edit design/playtest.yaml, not the markdown. The spreadsheet (scripts/build_xlsx.py) has the same checklist as the
"Playtest" and "Playtest games" sheets, with columns for the results.
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

INTRO = """# Play test checklist

Generated from `design/playtest.yaml` by `scripts/build_playtest_md.py`. Edit the yaml, not this file. The
spreadsheet has the same list as the **Playtest** and **Playtest games** sheets, with columns for the results.

## How to run it

- Play in the simulator, which now implements every card of the set (the cards that needed new effects are impl tier 2; no
  card is paper only any more). If it does something the card text does not say, note it as a bug and not as a result for
  the card. Paper also works: proxies can be printed from the Magic Set Editor set file (the new cards have no art, which
  does not matter for testing).
- Build a few themed decks rather than random piles: one per color axis (white numbers, blue recycling, black hand
  pressure, red red moods, green pile replay and 6s) plus one colorless gate deck. Ready-made decklists for the first three
  sessions (extra-play engines, scaling and anthems, then five 15-card Power Duel decks), a baseline deck and a game log are in
  `design/playtest-decks.md`.
- Play some 2-player games and at least one with 3 or 4 players (Hurt Feelings, trailing conditions).
- For each card that comes up, write down three things: **strength** (too strong, fair, too weak), **clarity** (was the
  text clear?) and **fun**. If a card is off, note which fallback below you would pick.
- When a card has been tested, move its `status` in `cards/<name>.yaml` from `idea` to `draft` or `playtest`, and record
  the decision in `design/open-questions.yaml` (Q8 for the two Entitlement versions, Q9 for the rest).

## Order

Test tier 1 first, since those cards could break a game. Tier 2 cards are about interactions, tier 3 about cards that may
be too weak, and tier 4 about rules questions.
"""


def main():
    data = yaml.safe_load((ROOT / "design" / "playtest.yaml").read_text(encoding="utf8"))
    cards = {}
    for p in sorted((ROOT / "cards").glob("*.yaml")):
        c = yaml.safe_load(p.read_text(encoding="utf8"))
        cards[c["name"]] = c
    problems = [e["card"] for e in data["cards"] if e["card"] not in cards]
    if problems:
        sys.exit("unknown cards in playtest.yaml: " + ", ".join(problems))
    out = [INTRO]
    for tier, title in data["tiers"].items():
        entries = [e for e in data["cards"] if e["tier"] == tier]
        out.append("## Tier %s: %s (%d cards)\n" % (tier, title, len(entries)))
        for e in entries:
            c = cards[e["card"]]
            out.append("- [ ] **%s** (%s %s%s): %s" % (
                e["card"], c["color"], c["rarity"], ", " + c["slot"] if c.get("slot") else ", unslotted backup", e["check"]))
            out.append("  - Fallback: %s" % e["fallback"])
        out.append("")
    out.append("## Whole-game checks\n")
    for g in data["games"]:
        out.append("- [ ] %s" % g["check"])
    out.append("")
    (ROOT / "design" / "playtest-checklist.md").write_text("\n".join(out), encoding="utf8")
    print("wrote design/playtest-checklist.md: %d card items, %d game checks" % (len(data["cards"]), len(data["games"])))


if __name__ == "__main__":
    main()
