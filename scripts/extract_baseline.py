"""Extract the original 133-card Mood Swings pool from a MoodSwings-Web checkout.

Usage: python scripts/extract_baseline.py <path-to-MoodSwings-Web> [out.json]

Parses database/migrations/0003_create_card_catalog.sql (the seed) and applies
the later UPDATE-only fix migrations that touch card values/text, so the output
matches what the simulator actually runs.
"""
import json
import re
import sys
from pathlib import Path

SEED = "0003_create_card_catalog.sql"
FIXES = [
    "0005_fix_card_alt_values.sql",
    "0030_fix_rationalization_optional.sql",
    "0055_fix_hesitation_optional.sql",
    "0313_fix_guilt_optional.sql",
]
ROW = re.compile(
    r"^\((\d+), '((?:[^']|'')*)', '(\w+)', '(\w+)', '(\w+)', (\d+), (NULL|\d+), "
    r"([01]), ([01]), ([01]), '((?:[^']|'')*)'\)[,;]$",
    re.M,
)


def unq(s):
    return s.replace("''", "'")


def main():
    root = Path(sys.argv[1]) / "database" / "migrations"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parent.parent / "baseline" / "original-pool.json"
    cards = {}
    for r in ROW.findall((root / SEED).read_text(encoding="utf8")):
        i = int(r[0])
        cards[i] = {
            "id": i, "name": unq(r[1]), "effect_key": r[2], "color": r[3], "rarity": r[4],
            "base_value": int(r[5]), "alt_value": None if r[6] == "NULL" else int(r[6]),
            "to_play": bool(int(r[7])), "while_in_play": bool(int(r[8])), "after_playing": bool(int(r[9])),
            "rules_text": unq(r[10]),
        }
    for f in FIXES:
        for m in re.finditer(r"UPDATE cards SET (.*?) WHERE id = (\d+);", (root / f).read_text(encoding="utf8"), re.S):
            sets, i = m.group(1), int(m.group(2))
            a = re.search(r"alt_value = (\d+)", sets)
            if a:
                cards[i]["alt_value"] = int(a.group(1))
            t = re.search(r"rules_text = '((?:[^']|'')*)'", sets)
            if t:
                cards[i]["rules_text"] = unq(t.group(1))
    out.write_text(json.dumps([cards[i] for i in sorted(cards)], indent=1, ensure_ascii=False) + "\n", encoding="utf8")
    print(f"wrote {len(cards)} cards to {out}")


if __name__ == "__main__":
    main()
