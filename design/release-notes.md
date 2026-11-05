# Mood Swings custom set: current-state spreadsheet

This release is a snapshot of the community-designed custom set for the Mood Swings TCG (about 133 cards), working title **Emotional Baggage** (set code `XEMB`). The attached file `mood-swings-custom-set.xlsx` is built from the card files and design notes in this repository at the tagged commit. Download it and open it in Excel, LibreOffice or Google Sheets.

## How to read the spreadsheet

| Sheet | What it shows |
|---|---|
| **Set** | Every card slot of the set (for example `W-C03` is the third white common) with its role and target value and timing, and the card filling it: status, name, value, ability timing, rules text, reprint, simulator implementation tier, designer, notes and any rulings (how the card works in play, which do not change its text). A slot with no name is still open. |
| **Summary** | Progress per color and rarity (filled / slots), how many cards are final versus ideas, the average printed value and ability-timing counts compared with the original pool, and the **Rule checks** section. It should say "none: all checks pass". |
| **Baseline** | The original 133-card pool, for comparison and for checking that a new card is not a clone. |
| **Open Questions** | Design decisions still to make (status `open`) and ones already made (status `decided`), with the notes behind them. |
| **Playtest** | One row per card for play testing: a tier (1 could break the game, 2 interactions, 3 possibly too weak, 4 rules and clarity, 0 general check only), what to check, and the fallback to try if the card is off. The last columns are for your results: strength (too strong, fair, too weak), clarity, fun, the fallback you chose, and notes. |
| **Playtest games** | The whole-game checks (game length, hand sizes, color balance, the axis decks, extra-play engines, 3 to 4 player games, trigger ordering, paper counters) with a result column, and a blank game log. |

Card names are **placeholders**: the pool names cards with single emotion words, and names may change. The same checklist is in `design/playtest-checklist.md` in the repository; to change it, edit `design/playtest.yaml`.

The `status` of a card is `idea` (written, not tested), `draft`, `playtest` or `final`. Reprints from the original pool are marked `final` once checked against the printed card.

## Where the cards live

The spreadsheet is generated, so to change a card, edit its file in the repository, not the spreadsheet:

- `cards/<name>.yaml`: one file per card (format in `design/card-schema.md`).
- `design/skeleton.yaml`: the slot structure.
- `design/open-questions.yaml`: decisions and open questions.

To build the spreadsheet yourself: `pip install -r requirements.txt`, then `python scripts/build_xlsx.py` (it writes `out/set.xlsx`).

## Fan content

Unofficial community design for the Mood Swings TCG. Not an official product.
