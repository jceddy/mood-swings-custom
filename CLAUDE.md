# Notes for Claude: mood-swings-custom

This repo holds the work-in-progress design of a community-designed custom set for the Mood Swings TCG. Read this file first, then
`README.md` and `design/open-questions.yaml`.

## What we are doing

- Designing a **standalone set of about 133 cards**. Reprints from the original pool must be **under 10%** (cap of 13).
- Using the principles of Adam Prosak's **design skeleton** from Magic: The Gathering (Mark Rosewater, "Nuts & Bolts 13: Design Skeleton
  Revisited", 2021-03-22) as far as they apply. Mood Swings is simpler than Magic: no lands, no mana. See `design/principles.md` for the
  mapping.
- Only mechanics that **work on paper** and can **realistically be implemented in the digital simulator** (the sibling repo
  `jceddy/MoodSwings-Web`). Simulator changes are handled separately; a mechanic only has to be implementable in principle.
- Producing a **current-state spreadsheet at any step** as an output deliverable.

## Mood Swings facts that matter for design

- Cards are called **moods** once in play. Each has a printed value (0 to 12) in the top-right corner, sometimes an alternate value.
  Players score their moods each round; highest total wins the round.
- No mana or lands. Plays are gated by "one play per turn"; moods can grant extra plays (unrestricted, or restricted by color, value,
  discard pile, and so on).
- Ability timings: **to play** (a cost/restriction), **while in play** (static), **after playing** (one-shot). A card can have several.
- Interaction verbs by color in the original pool: white suppresses, blue bounces to hand, black and red move moods to the discard pile,
  green has no removal. See the Baseline sheet for the full original pool.
- The original pool is 133 cards: 48 common, 40 uncommon, 30 rare, 15 mythic. Each color has exactly 8 uncommons, 6 rares and 3 mythics.
  `baseline/original-pool.json` is extracted from MoodSwings-Web's `database/migrations/0003_create_card_catalog.sql` plus later fixes
  (`scripts/extract_baseline.py`). Source repo for the simulator: https://github.com/jceddy/MoodSwings-Web (it has its own CLAUDE.md).

## Set decisions made so far (full detail in `design/open-questions.yaml`)

- Skeleton: 5 colors x (8 common, 8 uncommon, 6 rare, 3 mythic) = 125, plus 8 colorless (5 common, 2 uncommon, 1 rare) = 133.
- Colorless commons (X-C01..X-C05): value 4 each, and each can only be played if a mood of one specific color is in play
  (one card per color). Nothing multicolored yet.
- The original ally/enemy value-swapping wheel (10 commons) is **replaced** by a cycle of cards (slots C01/C02 per color) that care about
  2+ ally or enemy colored moods for a *different effect*.
- Probable reprints are role-player commons, pre-assigned to slots as `reprint_candidate` in the skeleton: Pacifism, Panic, Fear, Ambition,
  Hate, Suspicion, Shock, Bravado, Zeal, Compulsion, Joy, Nostalgia, Determination (13, exactly the cap). Not final.
- Mythic slots: in each color, M01 is a dedicated build-around and M02/M03 are flexible (need not be build-arounds). The
  build-around axes themselves are **undecided** (Q5) and will likely shape the rest of the set. Other rare/uncommon roles may be revised once they exist.
- The colorless gate counts **any player's** moods ("there is a white mood"), decided in Q7. The five gate cards are drafted
  (X-C01..X-C05, placeholder names); open sub-question: whether a suppressed mood still counts.

## How the tracking works

- `design/skeleton.yaml`: one entry per slot (id like `W-C03`, color, rarity, role, target value/timing). It is the source of truth for
  structure; edit it directly. Roles and counts are proposals, not rules.
- `cards/<name>.yaml`: one file per card, claiming a slot via its `slot` field. Format in `design/card-schema.md`
  (includes `status`, `reprint_of`, and `impl_tier` for simulator feasibility).
- `design/open-questions.yaml`: decisions and open questions; shown on the spreadsheet.
- Build the deliverable: `pip install -r requirements.txt` then `python scripts/build_xlsx.py` (writes `out/set.xlsx`, which is gitignored).
  Sheets: Set, Summary (progress, value/timing vs the original pool, rule checks), Baseline, Open Questions. After any change, rebuild and
  check the "Rule checks" section for problems (wrong color/rarity for a slot, duplicate slot claims or names, bad `reprint_of`, reprint cap).

## Working conventions

- Work on branch `set-skeleton-and-tracking` (not merged to `main` yet). No pull request is open.
- The author prefers decisions recorded in `design/open-questions.yaml` (status: decided) as they are made.
- Keep `design/principles.md`, `README.md` and this file consistent with the skeleton when decisions change.
- Card text style follows the original pool: "After playing this mood, ...", "While in play, ...", "To play this card, ...".
- If you use shell heredocs to write files with apostrophes, prefer the file-writing tool instead; heredocs with quotes were unreliable
  in the original session's shell.

## Suggested next steps

1. Decide the five mythic build-around axes, one per color in the M01 slots (Q5); revise the other rare and uncommon roles to fit.
2. Design the ally/enemy cycle effects (slots C01/C02 per color) (the 5 colorless gate cards are drafted).
3. Confirm the reprint list, then start filling slots with card files and rebuild the spreadsheet.
