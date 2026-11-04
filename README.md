# mood-swings-custom
A community-designed custom set for the Mood Swings TCG

Working title: **Emotional Baggage** (set code `XEMB`; the group may still change it, see `design/open-questions.yaml` Q11).

## Layout

| Path | Purpose |
|---|---|
| `design/principles.md` | Set-building principles and how they map to Mood Swings |
| `design/skeleton.yaml` | The slot skeleton: one entry per card slot (color, rarity, role, target value) |
| `design/open-questions.yaml` | Unresolved design decisions |
| `design/card-schema.md` | Format of a card file |
| `design/axes.md` | Tentative mythic build-around axes and the partner-slot plan (Q5) |
| `cards/*.yaml` | One file per card; each claims a skeleton slot |
| `baseline/original-pool.json` | The original 133-card pool, extracted from the simulator |
| `design/release-notes.md` | Instructions for reading the spreadsheet; the body of each release |
| `scripts/build_xlsx.py` | Builds the current-state spreadsheet |
| `scripts/extract_baseline.py` | Regenerates the baseline from a MoodSwings-Web checkout |

## Current-state spreadsheet

```
pip install -r requirements.txt
python scripts/build_xlsx.py        # writes out/set.xlsx
```

A build of the spreadsheet is attached to each [release](../../releases): pushing a tag such as `0.2.4` (or running the workflow by hand from the Actions tab and typing a version) runs `.github/workflows/release.yml`, which rebuilds it (and stops if a rule check fails) and publishes it with `design/release-notes.md` as the notes.

Sheets: **Set** (every slot and the card filling it), **Summary** (progress, distribution vs the original pool, rule checks),
**Baseline** (the original pool), **Open Questions**.

## Set constraints

- Standalone set of about 133 cards, keeping the original pool's symmetry (per color: 8 uncommons, 6 rares, 3 mythics).
- Reprints from the original pool: under 10% of the set (cap of 13). Probable reprints are role-player commons, listed as candidates in the skeleton.
- Colorless cards allowed: 5 commons (value 5, each playable only if you have a mood of one particular color, replacing the original vanilla-4 cycle), 2 uncommons and 1 mythic. Nothing multicolored yet.
- The original ally/enemy value-swapping wheel is replaced by a cycle of cards that count 2+ ally or enemy moods for a different effect.
- Only mechanics that work on paper and are realistic to implement in the MoodSwings-Web simulator (simulator changes are handled separately).
