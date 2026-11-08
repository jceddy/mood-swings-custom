# Play test decks and session log

Companion to `design/playtest-checklist.md` (generated from `design/playtest.yaml`). This file has the test decks for the
first two sessions and a log template. The per-card ratings (strength, clarity, fun, fallback chosen) go in the **Playtest**
sheet of the spreadsheet; the log below is for what happened in each game.

## Setting up the games

The decks are written in the simulator's decklist format (an optional `About` block with a `Name` line, a blank line, then
one `count name` line per card). They are meant for a Duel game with a custom decklist per player (`custom_duel`) with the
user-defined rules: at least 20 cards, no rarity limits and no copy limits. Each deck is 20 cards, one copy of each. If the
Duel setup in the app differs from this, use whichever custom-deck option lets each player bring their own list.

Two things to keep in mind while playing:

- **Text against implementation.** If the simulator does something the card text does not say, write it down as a bug
  and do not count it as a result for the card. Several cards were reworded recently (Vitality, Schadenfreude, Restlessness,
  Candor), so check the text on the card against what happens.
- **Same deck, both seats.** Swap who goes first between games. The mirror games show how strong an engine is on its own;
  the games against the baseline show whether it beats ordinary cards.

## The baseline deck

An ordinary pile with no extra plays: the original role-player reprints (Pacifism, Panic, Hate, Suspicion, Shock, Zeal,
Compulsion, Joy, Determination) plus plain conditional and removal cards in all five colors. Every engine and scaling deck
below plays against it first.

```
About
Name B Baseline

1 Pacifism
1 Panic
1 Hate
1 Suspicion
1 Shock
1 Zeal
1 Compulsion
1 Joy
1 Determination
1 Temperance
1 Anticipation
1 Exuberance
1 Resolve
1 Largesse
1 Prudence
1 Vengeance
1 Reminiscence
1 Distrust
1 Disdain
1 Indignation
```

## Session 1: extra-play engines

Why first: the free-play cards, the grants and the burst turns stack, so this is where a game is most likely to break.

### E1 Free-play cycle (all five colors)

All five zero-value free-play commons (Fear, Nostalgia, Levity, Remorse, Rashness) and the grants (Affinity, Familiarity,
Modesty), plus Reverie, Overconfidence, Haunting, Reinvigoration, Resilience and Wistfulness. The five colorless gate
commons are the bodies: each free-play card gives you the color its gate needs (Rashness and Adrenaline for Impatience,
Remorse and Haunting for Resentment), and the five gates all have the number 5, which turns Affinity on.

```
About
Name E1 Free-play cycle

1 Fear
1 Nostalgia
1 Levity
1 Remorse
1 Rashness
1 Adrenaline
1 Affinity
1 Familiarity
1 Modesty
1 Reverie
1 Overconfidence
1 Haunting
1 Reinvigoration
1 Resilience
1 Wistfulness
1 Reverence
1 Detachment
1 Resentment
1 Impatience
1 Contentment
```

### E2 Green replay (mono-green)

The green axis: replaying moods from the discard pile (Reinvigoration, Resilience, Wistfulness, Thrift, Nostalgia) with
fuel (Carelessness, Wastefulness, Possessiveness) and 3-to-6 bodies.

```
About
Name E2 Green replay

1 Reinvigoration
1 Resilience
1 Wistfulness
1 Nostalgia
1 Thrift
1 Joy
1 Carelessness
1 Wastefulness
1 Possessiveness
1 Optimism
1 Urgency
1 Determination
1 Resolve
1 Honesty
1 Gratitude
1 Kinship
1 Vindication
1 Perseverance
1 Contentment
1 Restlessness
```

### E1b Free-play cycle with bodies (all five colors)

Added after the first session (see `design/playtest-results.md`): E1 lost all six games to B because eight of its 20 cards
print 0, so its extra plays had nothing valuable to carry. E1b keeps the five free-play commons, the grants (Affinity, Familiarity,
Modesty), Reverie, Overconfidence, Haunting and the five colorless gates, and replaces the four weakest cards (Adrenaline,
Resilience, Reinvigoration, Wistfulness) with 3-value bodies that help an engine: Joy (an extra play next turn), Compulsion (takes a
card, which helps a small hand), Temperance (worth 5 when you hold fewer cards than each other player, which an engine deck
usually does) and Reminiscence (a loot that refills the hand). Joy and Compulsion also give the deck green and red moods for
Contentment and Impatience. The average printed value goes from 1.75 to 2.3 (Haunting now prints 0; B is about 2.65 before its 3-to-6 cards).
Reinvigoration is still tested in E2.

```
About
Name E1b Free-play cycle with bodies

1 Fear
1 Nostalgia
1 Levity
1 Remorse
1 Rashness
1 Affinity
1 Familiarity
1 Modesty
1 Reverie
1 Overconfidence
1 Haunting
1 Joy
1 Compulsion
1 Temperance
1 Reminiscence
1 Reverence
1 Detachment
1 Resentment
1 Impatience
1 Contentment
```

### Games to play

| # | Decks | Games | What to look for |
|---|---|---|---|
| 1 | E1 against B | 3, swapping seats | Largest turn (number of plays), whether the opponent can respond, whether E1 actually wins. |
| 2 | E1 mirror | 2 | How fast both sides snowball; whether the first player wins every time; Overconfidence's skipped turn. |
| 3 | E2 against B | 3, swapping seats | How many plays Reinvigoration gives, whether the discard pile runs dry, Resilience and Wistfulness together. |
| 4 | E1 against E2 | 1 or 2 | Which engine is stronger; the game length with two engines. |
| 5 | E1b against B | 3, swapping seats | Does the free-play cycle win once it has bodies? Compare with E1 (0 to 6, no round won except one): round scores against B's 3, 6, 9, and the largest burst. |
| 6 | E1b mirror | 1 | How fast two decks with bodies snowball; how the free-play chains and the gates compare. |

## Session 2: scaling and anthems

Run each scaling deck against B first, then against each other.

### G Green anthems (mono-green)

Fulfillment (scores each mood worth 6 or more twice) with the 3-to-6 cards, Vitality, Maturity, Vindication and
Perseverance. Possessiveness is fed by Carelessness and Wastefulness.

```
About
Name G Green anthems

1 Fulfillment
1 Vitality
1 Maturity
1 Determination
1 Restlessness
1 Urgency
1 Possessiveness
1 Resolve
1 Honesty
1 Perseverance
1 Vindication
1 Kinship
1 Gratitude
1 Optimism
1 Thrift
1 Joy
1 Nostalgia
1 Carelessness
1 Wastefulness
1 Contentment
```

### R Red pile (mono-red)

Ardor (value up by the number of red moods) with Verve, Dominance, Exuberance and Adrenaline, plus FOMO (value 7, drains
the hand), Frenzy and removal.

```
About
Name R Red pile

1 Ardor
1 Verve
1 Dominance
1 Exuberance
1 Adrenaline
1 Frenzy
1 FOMO
1 Covetousness
1 Rashness
1 Shock
1 Zeal
1 Compulsion
1 Belligerence
1 Hellbent
1 Whimsy
1 Impatience
1 Competitiveness
1 Ruthlessness
1 Rancor
1 Vindictiveness
```

### W White numbers (white, with Grudge and Elusiveness)

Levelheadedness and Rudeness (the swing cards) with the numbers cards (Orderliness, Affinity, Solidarity, Humility,
Equanimity, Familiarity, Modesty). Grudge (the white mythic) replaces Solace and Elusiveness (blue) replaces Vigilance, so
both replacement effects are on one board and the ordering rule can be tested: when one player controls both, that player
chooses the order.

```
About
Name W White numbers

1 Levelheadedness
1 Rudeness
1 Affinity
1 Orderliness
1 Solidarity
1 Humility
1 Equanimity
1 Familiarity
1 Modesty
1 Confidence
1 Discernment
1 Reassurance
1 Temperance
1 Largesse
1 Pacifism
1 Grudge
1 Elusiveness
1 Fairness
1 Compassion
1 Reverence
```

### Games to play

| # | Decks | Games | What to look for |
|---|---|---|---|
| 1 | G against B | 2 | The round Fulfillment, Vitality or Maturity start deciding games; whether opponents can remove Maturity in time. |
| 2 | R against B | 2 | Ardor's snowball; whether FOMO is discarded too soon for a 7 to be fair; Rancor and Volatility hitting your own cheap moods. |
| 3 | W against B | 2 | Levelheadedness (every mood scores 2: who gains?) and Rudeness (one blank turn for every other player) against a combo turn. Grudge gives extra plays equal to the chosen opponent's round wins, so check the burst once B has won a round or two; with Elusiveness on the same board, check the replacement ordering (Grudge sends a mood to the bottom of the deck, Elusiveness to your hand) and who chooses. |
| 4 | G, R and W against each other | 1 each | Color balance and the axis question (Q5): does each axis feel like a deck? |

## Coverage of the first tier

Every card in the first tier of the checklist is in a deck above.

| Card | Deck |
|---|---|
| Fear, Nostalgia, Levity, Remorse, Rashness | E1 |
| Affinity | E1, W |
| Reverie, Overconfidence, Haunting | E1 |
| Reinvigoration | E1, E2 |
| Reverence, Detachment, Resentment, Impatience, Contentment | E1 (all five); Impatience also in R, Contentment also in G and E2 |
| Fulfillment, Vitality, Maturity | G |
| Ardor, FOMO | R |
| Levelheadedness, Rudeness, Grudge | W (Elusiveness is in W too, for the ordering rule) |

## Session log

Copy this for each game.

```
Game:            (session and number, for example S1-3)
Decks and seats: (who played which deck, who went first)
Result:          (winner, round wins, number of rounds played)
Longest turn:    (number of plays, which cards)
Hands:           (did a player run dry, in which round)
Decided the game: (cards or plays)
Too strong:      (card, why)
Too weak:        (card, why)
Unclear text:    (card, what was misread)
Rules questions: (anything the text did not settle)
Simulator bugs:  (card text against what the simulator did)
```

After a session:

1. Fill in the **Playtest** sheet row for each card that came up: strength (too strong, fair, too weak), clarity, fun, the
   fallback you would pick, and notes.
2. Move the card's `status` in `cards/<name>.yaml` from `idea` to `draft` or `playtest`.
3. Record the decision in `design/open-questions.yaml` (Q8 for the two Entitlement versions, Q9 for the other watch items),
   and apply a chosen fallback in the card file with the reason in its notes.
4. Whole-game findings (game length, hand sizes, color balance, axis decks) go on the **Playtest games** sheet.
