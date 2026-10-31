# Set-building principles

Source: Adam Prosak's design skeleton, as described in Mark Rosewater's "Nuts & Bolts 13: Design Skeleton Revisited"
(Wizards of the Coast, 2021-03-22). Notes here are paraphrased and adapted to Mood Swings, which has no creatures, mana,
or lands: plays are gated by a one-play-per-turn allowance, and cards in play (moods) can grant extra plays, either
unrestricted or restricted by color, value, and so on.

## The method

1. Plan every slot before designing cards: color, rarity, role, target value, ability timing.
2. Treat the skeleton as a living document. Adjust it when the set needs it, but note the change.
3. Spend complexity by rarity: commons are simple (one ability timing, one idea); uncommons loosen up; rares and mythics carry the engines.
4. Keep each color's job distinct (the color pie) and fill each color's common slots with variety, not repeats.
5. Use a cycle at common to show players what the archetypes are (Magic: the two-color uncommon signposts; Mood Swings: the ally/enemy wheel).
6. Include colorless slots deliberately, and make them tell the player something about the set.

## How the Magic skeleton maps here

| Magic skeleton | Mood Swings equivalent |
|---|---|
| Mana value curve at common | Printed value (0-12) distribution; the modal common is 3 |
| Creature / spell ratio per color | Static-value moods vs effect moods |
| Keyword budget per color | Ability-timing budget; one timing at common |
| Color pie spell slots | Per-color verbs: suppress (W), bounce (U), discard-pile removal (B/R), play grants (W/G) |
| Two-color uncommon signposts | Ally/enemy cycle at common (no multicolor cards yet): cards that care about 2+ adjacent or opposing colored moods |
| Artifacts (colorless) | Colorless commons worth 5 that need one of your moods of a specific color (one per color), plus 2 colorless uncommons and a rare |
| Lands | Not applicable |

## Original-pool numbers used as the baseline

See `baseline/original-pool.json` (regenerate with `scripts/extract_baseline.py`) and the Baseline sheet of the spreadsheet.

- 133 cards: 48 common, 40 uncommon, 30 rare, 15 mythic. Each color has exactly 8 uncommons, 6 rares, 3 mythics.
- Average printed value falls with rarity: 3.17 / 2.25 / 1.53 / 1.40 (common to mythic).
- Roughly (hand-tagged by keyword, so approximate): 25 cards grant extra plays; 19 remove moods to the discard pile; 11 bounce; 7 suppress (all white).
- Sweepers appear only at uncommon and above (about 15).
