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

- Moods stay in play after a round is scored, so boards grow over the whole game.
- Each player gets one turn per round (one play per turn, plus any extra plays), so boards grow by about one mood per round. A
  "start of each of your turns" trigger and a start-of-round trigger fire the same number of times.
- Hand sizes are public.
- The losing player (or players) draw a card at the end of each round. There is no draw each turn, so hands refill only that way
  and through card effects: cards in hand are a scarce resource.
- Cards are called **moods** once in play. Each has a printed value (0 to 12) in the top-right corner, sometimes an alternate value.
  Players score their moods each round; highest total wins the round.
- No mana or lands. Plays are gated by "one play per turn"; moods can grant extra plays (unrestricted, or restricted by color, value,
  discard pile, and so on).
- When several triggers or replacement effects apply to the same event, they are applied starting with the active player and then player by player in turn order (stated by the author; the simulator already resolves after-scoring effects per controller in turn order). When one player controls more than one, that player chooses the order (decided).
- Ability timings: **to play** (a cost/restriction), **while in play** (static), **after playing** (one-shot). A card can have several.
- Interaction verbs by color in the original pool: white suppresses, blue bounces to hand, black and red move moods to the discard pile,
  green has no removal. See the Baseline sheet for the full original pool.
- The baseline's rules text was extracted from the simulator's database, so parenthetical reminder text on the printed cards may be
  missing there (for example, "If you can't do that, you can't play this card." on every to-play cost is parenthetical on the
  printed cards but plain text in the baseline). Match the printed form in new cards.
- The printed card images are in MoodSwings-Web under `web-static/img/cards/MSW/<number>-<name>.webp` (convert to PNG to view). Checked for the
  13 original reprints (Ambition and Bravado were replaced later): the wording matches the baseline, except that four printed cards carry reminder text the baseline lacks (Pacifism: suppressed
  moods have a value of 0 and are turned sideways; Hate, Bravado and Determination: "Moods are cards in play."). Printed cards also write
  the ability line as "After playing this mood — Choose ..." (em dash, capital after it) and "While in play — This mood's value is ...";
  the simulator text uses a comma. Our card files use the printed form (decided, all cards converted).
- The original pool is 133 cards: 48 common, 40 uncommon, 30 rare, 15 mythic. Each color has exactly 8 uncommons, 6 rares and 3 mythics.
  `baseline/original-pool.json` is extracted from MoodSwings-Web's `database/migrations/0003_create_card_catalog.sql` plus later fixes
  (`scripts/extract_baseline.py`). Source repo for the simulator: https://github.com/jceddy/MoodSwings-Web (it has its own CLAUDE.md).

## Set decisions made so far (full detail in `design/open-questions.yaml`)

- Set name and code: **Emotional Baggage, XEMB** (tentative, the group is still discussing; Q11). Set codes for community sets are an X plus a three-letter abbreviation so they cannot collide with a later official code. Card names are single mood words (feelings or dispositions), as in the original pool.
- Skeleton: 5 colors x (8 common, 8 uncommon, 6 rare, 3 mythic) = 125, plus 8 colorless (5 common, 2 uncommon, 1 mythic) = 133.
- Colorless commons (X-C01..X-C05): value 5 each, and each can only be played if you have a mood of one specific color
  (one card per color). Nothing multicolored yet.
- The original ally/enemy value-swapping wheel (10 commons) is **replaced** by a cycle of cards (slots C01/C02 per color) that care about
  2+ ally or enemy colored moods for a *different effect*.
- Reprints are role-player commons, pre-assigned to slots as `reprint_candidate` in the skeleton: Pacifism, Panic, Fear, Hate, Suspicion,
  Shock, Zeal, Compulsion, Joy, Nostalgia, Determination (11; the cap is 13). Ambition and Bravado were replaced by the new cards Remorse
  and Rashness to complete the zero-point free-play cycle (Q3, Q10).
- Mythic slots: in each color, M01 is a dedicated build-around and M02/M03 are flexible (need not be build-arounds). Each color has a
  tentative build-around axis and an M01 mythic (Q5 stays open; see `design/axes.md`): white numbers (Orderliness), blue recycling the
  discard pile (Reverie), black hand pressure (Neglect), red playing red moods (Dominance), green replaying from the discard
  pile (Reinvigoration). White's partner cards are written; the other four axes' partners are not. Other rare/uncommon roles may be
  revised once they exist.
- The colorless gate counts **only your own** moods ("if you have a white mood"), decided in Q7 (originally any player's), and the
  value was raised from 4 to 5 to match (Q1). A suppressed mood still counts as a mood of its color for the gate. The five gate cards
  are drafted (X-C01..X-C05, placeholder names).

## How the tracking works

- `design/skeleton.yaml`: one entry per slot (id like `W-C03`, color, rarity, role, target value/timing). It is the source of truth for
  structure; edit it directly. Roles and counts are proposals, not rules.
- `cards/<name>.yaml`: one file per card, claiming a slot via its `slot` field. Format in `design/card-schema.md`
  (includes `status`, `reprint_of`, and `impl_tier` for simulator feasibility).
- `design/open-questions.yaml`: decisions and open questions; shown on the spreadsheet.
- `design/axes.md`: the tentative mythic build-around axis for each color (Q5) and a partner-slot plan of about 14 slots per axis.
- Build the deliverable: `pip install -r requirements.txt` then `python scripts/build_xlsx.py` (writes `out/set.xlsx`, which is gitignored).
  Sheets: Set, Summary (progress, value/timing vs the original pool, rule checks), Baseline, Open Questions. After any change, rebuild and
  check the "Rule checks" section for problems (wrong color/rarity for a slot, duplicate slot claims or names, bad `reprint_of`, reprint cap).

## Working conventions

- `main` holds the work so far (PRs #1 to #3 are merged). Do new work on a feature branch off `main` and open a pull request only
  when asked.
- The author prefers decisions recorded in `design/open-questions.yaml` (status: decided) as they are made.
- Keep `design/principles.md`, `README.md` and this file consistent with the skeleton when decisions change.
- Digital asynchronous play: avoid "may" reactions that prompt a player during an opponent's turn (found on Defensiveness, where every extra play would have asked its holder). Prefer static effects, mandatory triggers, or effects that only fire on your own turn. Random picks (Cruelty-style) are a good way to avoid choices. There are no known optional reactions on an opponent's turn in the set.
- Card text style follows the printed cards: "After playing this mood — Choose ...", "While in play — This mood's value is ...", "To play this card — Discard ..." (em dash, then a capital letter).
- If you use shell heredocs to write files with apostrophes, prefer the file-writing tool instead; heredocs with quotes were unreliable
  in the original session's shell.

## Suggested next steps

All 133 slots are filled (122 cards are still `idea`, the 11 reprints are `final`). What is left is checking that the cards work.

1. Play test. The checklist is `design/playtest-checklist.md`, generated from `design/playtest.yaml` (edit the yaml, then run
   `python scripts/build_playtest_md.py`); the spreadsheet has the same list as the Playtest sheet with result columns. Test tier 1
   (could break the game) first. Paper first, with proxies printed from the MSE set file in `jceddy/edition1`.
2. After each test, move the card's `status` to `draft` or `playtest`, and record the decision in `design/open-questions.yaml`
   (Q8 for the two Entitlement versions, Q9 for the other watch items). Apply a chosen fallback in the card file, with the reason
   in its notes.
3. Resolve Q5 (the mythic build-around axes, see `design/axes.md`) once the axis decks have been played.
4. Cards that need new simulator effects are impl tier 2 (37 cards); three are paper only (tier 3: Admiration, Elusiveness,
   Grudge). Simulator work is handled separately.
5. Releases: pushing a tag or running the Release workflow publishes the spreadsheet (`.github/workflows/release.yml`).
