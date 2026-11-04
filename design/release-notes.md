# Mood Swings custom set: current-state spreadsheet

This release is a snapshot of the community-designed custom set for the Mood Swings TCG (about 133 cards). The attached file `mood-swings-custom-set.xlsx` is built from the card files and design notes in this repository at the tagged commit. Download it and open it in Excel, LibreOffice or Google Sheets.

## How to read the spreadsheet

| Sheet | What it shows |
|---|---|
| **Set** | Every card slot of the set (for example `W-C03` is the third white common) with its role and target value and timing, and the card filling it: status, name, value, ability timing, rules text, reprint, simulator implementation tier, designer and notes. A slot with no name is still open. |
| **Summary** | Progress per color and rarity (filled / slots), how many cards are final versus ideas, the average printed value and ability-timing counts compared with the original pool, and the **Rule checks** section. It should say "none: all checks pass". |
| **Baseline** | The original 133-card pool, for comparison and for checking that a new card is not a clone. |
| **Open Questions** | Design decisions still to make (status `open`) and ones already made (status `decided`), with the notes behind them. |

Card names are **placeholders**: the pool names cards with single emotion words, and names may change.

The `status` of a card is `idea` (written, not tested), `draft`, `playtest` or `final`. Reprints from the original pool are marked `final` once checked against the printed card.

## Where the cards live

The spreadsheet is generated, so to change a card, edit its file in the repository, not the spreadsheet:

- `cards/<name>.yaml`: one file per card (format in `design/card-schema.md`).
- `design/skeleton.yaml`: the slot structure.
- `design/open-questions.yaml`: decisions and open questions.

To build the spreadsheet yourself: `pip install -r requirements.txt`, then `python scripts/build_xlsx.py` (it writes `out/set.xlsx`).

## Fan content

Unofficial community design for the Mood Swings TCG. Not an official product.
