# Play test decks and session log

Companion to `design/playtest-checklist.md` (generated from `design/playtest.yaml`). This file has the test decks for the
first three sessions and a log template. The per-card ratings (strength, clarity, fun, fallback chosen) go in the **Playtest**
sheet of the spreadsheet; the log below is for what happened in each game.

## Setting up the games

The decks are written in the simulator's decklist format (an optional `About` block with a `Name` line, a blank line, then
one `count name` line per card). They are meant for a Duel game with a custom decklist per player (`custom_duel`) with the
user-defined rules: at least 20 cards, no rarity limits and no copy limits. Each deck is 20 cards, one copy of each (the Power Duel decks of session 3 are 15 cards with a single mythic). If the
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

## Session 3: Power Duel decks

Power Duel is 15 cards with a single mythic, so these decks are 15 cards each (not the 20 of sessions 1 and 2), one copy of each card, and
the only mythic is the build-around card. Every card is from the custom set (the reprints count as part of it). They are proposals from a
first pass over the play test results; none has been played in this form. Red and green are close to tested lists (R and G), white is the
tested W list trimmed, and blue and black are new, so expect to change them. Set the Duel rules to 15 cards if the app asks for a minimum.

### PW Even numbers (white, Orderliness)

The W list without its extra mythic and its weakest cards (Grudge, Levelheadedness, Largesse, Confidence, Solace). Orderliness (even) with the many
2s, Humility and Solidarity; Familiarity, Affinity and Modesty chain extra plays; Levity and Discernment add card flow. The risk is still
running out of cards by round 4.

```
About
Name PW Even numbers

1 Orderliness
1 Solidarity
1 Humility
1 Equanimity
1 Familiarity
1 Modesty
1 Affinity
1 Discernment
1 Levity
1 Reassurance
1 Temperance
1 Pacifism
1 Fairness
1 Reverence
1 Impartiality
```

### PU Reverie engine (blue, Reverie)

Untested. Reverie draws a card each time a mood is played while the discard pile has cards, and Reflection fills the pile itself. Rumination returns a
mood to the hand to replay its after-playing effect. Finishers: Anticipation (6 with four cards in hand), Resignation (6), Detachment (5). Watch for
deck-outs: Reflection with Reverie takes about one card from the deck per mood played, and a 15-card deck has 10 cards in it after the opening hand.

```
About
Name PU Reverie engine

1 Reverie
1 Reflection
1 Admiration
1 Rumination
1 Fear
1 Reminiscence
1 Rapport
1 Anticipation
1 Resignation
1 Impulse
1 Desperation
1 Detachment
1 Elusiveness
1 Deflection
1 Panic
```

### PB Neglect pressure (black, Neglect)

Untested. Suspicion, Nosiness, Dejection and Martyrdom empty the opponent's hand, Neglect then removes their best mood before scoring, and
Opportunism takes what they discard. Schadenfreude (6 after an opponent discards) and Composure (6 with more cards in hand than each other player)
are the bodies. Hands were empty by rounds 4 and 5 in earlier games, so this deck should peak late; the risk is a slow start.

```
About
Name PB Neglect pressure

1 Neglect
1 Suspicion
1 Nosiness
1 Dejection
1 Pettiness
1 Opportunism
1 Martyrdom
1 Schadenfreude
1 Composure
1 Vengeance
1 Resentment
1 Remorse
1 Hate
1 Brooding
1 Longing
```

### PR Ardor red pile (red, Ardor)

The R list without its other mythics (Dominance, Competitiveness) and its weakest cards (Hellbent, Covetousness, Rancor). Rashness, Adrenaline and Whimsy
chain red moods; Ardor and Verve pay them off; Frenzy and FOMO are the big single plays. Ardor is under discussion in Q13 (option A: count only the other red moods).
For a Dominance version, swap Ardor for Dominance.

```
About
Name PR Ardor red pile

1 Ardor
1 Verve
1 Adrenaline
1 Rashness
1 Exuberance
1 Impatience
1 Frenzy
1 FOMO
1 Whimsy
1 Shock
1 Zeal
1 Compulsion
1 Vindictiveness
1 Ruthlessness
1 Belligerence
```

### PG Fulfillment anthems (green, Fulfillment)

The G list without the fuel cards (Carelessness, Wastefulness, Possessiveness) that did not work in earlier games. Honesty, Determination, Resolve, Restlessness
and Urgency are the 6-value moods that Fulfillment doubles, and Vitality adds +2 a turn. For the replay mythic instead, swap Fulfillment for Reinvigoration and
Vitality, Maturity and Perseverance for Resilience, Possessiveness and Carelessness.

```
About
Name PG Fulfillment anthems

1 Fulfillment
1 Vitality
1 Maturity
1 Honesty
1 Determination
1 Resolve
1 Restlessness
1 Urgency
1 Vindication
1 Perseverance
1 Kinship
1 Contentment
1 Joy
1 Nostalgia
1 Thrift
```

### PW Even numbers splash (white with a splash, Orderliness)

A variant of PW built after the first Power Duel round (games 546 to 566, where PW went 10 wins to 11). It keeps 10 white cards and Reverence (the colorless gate that needs
a white mood) and adds four cards of other colors, aimed at what PW lacked: answers (white has none; Ardor ran away in 560 and 561), more chain starters (PW lost when it drew none, game 554), card flow
(its hand ran dry), and bodies worth more than 2. It drops Affinity, Reassurance, Pacifism and Fairness. Mood Swings has no mana, so a splash costs nothing except the card's own condition, and Power Duel decks may use more than one color.

- **Rashness** (red, 0): a free extra play and removal of an opponent's mood worth 1 or less (Vitality, Fulfillment, Kinship, Adrenaline, Verve, an early Ardor).
- **Hate** (black reprint, 0): puts any mood on the bottom of the deck and draws, so it is card-neutral; the answer to Ardor, Maturity or an opponent's best mood.
- **Determination** (green reprint, 3 or 6): a 6 once any three moods share a color, which PW's own white chain does.
- **Rapport** (blue, 3): a loot, and a second loot while two or more white and/or black moods are out.

Rashness, Hate and Levity print 0, so they feed Orderliness (even), Humility and Equanimity, and Modesty's extra play accepts all four splash cards (0 to 3). Determination and Rapport print an odd 3, so PW's
own Impartiality (odd) suppresses them; choose even when the board is full of 3s. Levelheadedness (white) is the alternative to Rapport (11 white cards) if you want to test that line.

```
About
Name PW Even numbers splash

1 Orderliness
1 Solidarity
1 Humility
1 Equanimity
1 Familiarity
1 Modesty
1 Discernment
1 Levity
1 Temperance
1 Impartiality
1 Reverence
1 Rashness
1 Hate
1 Determination
1 Rapport
```

### PU Reverie discard (blue and black, Reverie)

A variant of PU built after the Power Duel games against PW, PB, PR and PG (games 546 to 579, where PU won 6 and lost 11). Reverie never ran: it needs cards in the discard pile, and blue has almost no way to put
them there (it did nothing with an empty pile in 547 and 575, and was used as a cost or put on the bottom of the deck in others). This version adds the black discard cards as fuel: Dejection (a 5; each player discards a card, so two
cards go into the pile), Suspicion and Nosiness (the opponent discards), and Remorse (a free extra play that moves a pile card to the bottom of the deck and draws). With Impulse's second play each turn Reverie can trigger twice a turn, and Rapport's second loot is on because the black moods count as white and/or black.
Schadenfreude is a 6 whenever an opponent discarded a card this round, Rumination finally has targets (bounce Suspicion or Nosiness at the start of the turn and play it again), Hate gives permanent, card-neutral removal, and Deflection with Fear is the bounce lock that won game 579.

It cuts Reflection, Admiration, Anticipation, Elusiveness, Panic and Reminiscence; Panic and Reminiscence are the first cards to swap back in if the deck lacks tempo or bodies. Risks: Dejection costs PU a card and its hand is already small, Neglect still punishes an empty hand,
and against decks that discard little (PG, PR) the pile may run short.

```
About
Name PU Reverie discard

1 Reverie
1 Impulse
1 Dejection
1 Suspicion
1 Nosiness
1 Remorse
1 Schadenfreude
1 Resignation
1 Detachment
1 Deflection
1 Rapport
1 Hate
1 Rumination
1 Fear
1 Desperation
```

### PU Reverie splash (blue with a tempo and scaling splash, Reverie)

The other PU variant from the same review: it keeps ten blue cards and adds five cards of other colors aimed at PU's other weaknesses, which were low values late (PG reached 40 and 41 with Fulfillment and Maturity, PR 30 and 49 with Ardor) and no permanent answers
(Panic and Deflection only bounce). It cuts Rumination (declined 11 times), Elusiveness, Reflection, Admiration and Anticipation.

- **Hate** (black reprint, 0): permanent, card-neutral removal (answers Maturity, Fulfillment, Ardor).
- **Rashness** (red, 0): a free extra play and removal of a mood worth 1 or less (Fulfillment when Kinship is not boosting it, Vitality, Adrenaline, Verve, Opportunism).
- **Determination** (green reprint, 3 or 6): a 6 once any three moods share a color, which PU's blue board does by round 2 or 3.
- **Vitality** (green rare, 1): +2 to each blue mood every turn, PU's own scaling; the riskiest card (a 1 that Rashness and Shock can kill, and on the Q9 watch list).
- **Temperance** (white, 3 or 5): a 5 when PU holds fewer cards than each other player, which is usually the case.

```
About
Name PU Reverie splash

1 Reverie
1 Impulse
1 Resignation
1 Detachment
1 Deflection
1 Panic
1 Rapport
1 Reminiscence
1 Fear
1 Desperation
1 Hate
1 Rashness
1 Determination
1 Vitality
1 Temperance
```

### PB Neglect splash (black with a tempo and removal splash, Neglect)

A variant of PB built after its Power Duel games (games 552 to 590, where PB went 15 wins to 7: against PW 4 to 2, PU 4 to 2, PR 5 to 0, PG 2 to 3). It keeps ten black cards and Resentment (the colorless gate that needs a black mood). It adds four cards of other colors aimed at what PB lacked: PB ended games holding unplayed cards (Neglect and Pettiness in 587, Brooding, Hate and Neglect in 588, Longing, Neglect and Remorse in 589)
because Remorse was its only extra play; it had no body above 5 and scored 3, 6 and 11 by round 3 against PG's 24 and 23; and it had only Vengeance and Hate as answers. It cuts Pettiness (never played), Opportunism (a 1 that was
discarded as fodder twice), Martyrdom (a 1 that needs a sacrifice) and Composure (a conditional 6 that scored once).

- **Resignation** (blue, 6): a turn-one 6. Its cost is a card from the hand, and PB usually has spare cards (a stuck Neglect).
- **Rashness** (red, 0): a free extra play and removal of an opponent's mood worth 1 or less (Fulfillment, Kinship, Vitality, Adrenaline, an early Ardor).
- **Fear** (blue reprint, 0): a free extra play that bounces one of your moods, so Vengeance, Nosiness, Suspicion or Dejection can be played again; the risk is the value of the mood it takes out of play.
- **Shock** (red, 2): removes up to two moods worth 3 or less. The other decks' mythics are low-valued early (Orderliness 2, Reverie 2, Fulfillment 1, Ardor around 0).

Brooding stays (it took PG's Determination back and played it as a 6 in 587 round 5); Neglect stays as the only mythic. Risks: Rashness, Fear and Remorse all print 0, so the deck only gains if the extra plays are used, and Schadenfreude is the only
conditional 6 left besides Resignation. Composure or Anticipation (blue, 3 or 6 with four or more cards in hand) is the first card to swap back in for Fear if board values run low.

```
About
Name PB Neglect splash

1 Neglect
1 Suspicion
1 Nosiness
1 Dejection
1 Schadenfreude
1 Vengeance
1 Resentment
1 Remorse
1 Hate
1 Brooding
1 Longing
1 Resignation
1 Rashness
1 Fear
1 Shock
```

### Games to play

Run each deck against each other once (10 pairings), swapping who goes first between games. Add a second game for any pairing that was close or
unclear. Against the baseline (B) the decks are 20 cards, so use B only for a sanity check of an individual deck.

| # | Decks | Games | What to look for |
|---|---|---|---|
| 1 | PW against PU | 1 | Whether blue's draw engine finds cards faster than white's extra plays; whether either runs out of cards. |
| 2 | PW against PB | 1 | Whether black's hand pressure strips white's small hand before its board comes online. |
| 3 | PW against PR | 1 | Red removal against white's low-value moods (Shock, Belligerence); white's Pacifism and Fairness against Ardor. |
| 4 | PW against PG | 1 | The earlier G against W games (G won 2 of 3): does the trimmed deck still win? |
| 5 | PU against PB | 1 | Whether Reverie has enough discard-pile fuel against a hand-pressure deck (Neglect's discards feed the pile). |
| 6 | PU against PR | 1 | Whether blue's engine is fast enough against red's early pressure; deck-outs with Reflection. |
| 7 | PU against PG | 1 | Whether Reverie keeps up with Vitality and Fulfillment. |
| 8 | PB against PR | 1 | Whether Neglect's round 4 and 5 payoff arrives before red's Ardor (red empties its own hand early). |
| 9 | PB against PG | 1 | Hand pressure against a deck that plays one mood a turn; Suspicion and Nosiness against Honesty (which reveals the hand). |
| 10 | PR against PG | 1 | The earlier R against G games (R won 4 of 6) with both decks trimmed to one mythic. |

PU variants (PU Reverie discard and PU Reverie splash): play each against PW, PB, PR and PG, swapping seats, and compare with the plain PU's record of 6 wins and 11 losses (against PW 2 to 3, PB 2 to 4, PR 1 to 1, PG 1 to 3).
For Reverie discard, look at whether the pile has cards for Reverie to use, how many cards Reverie draws a turn, whether PU runs out of cards (Dejection's cost, Neglect) and whether Schadenfreude is a 6. For Reverie splash, look at whether Hate and Rashness answer Maturity, Fulfillment and Ardor in time, whether Vitality survives, and whether PU's values keep up with the scaling decks.

Splash variant (PW Even numbers splash): play it against each of PU, PB, PR and PG, swapping seats, and compare with the 10 wins to 11 of the plain PW (against PU 3 to 2, PB 2 to 4, PR 4 to 2, PG 1 to 3).
Look at whether Hate and Rashness answer Ardor, Vitality and Maturity in time, whether Determination reaches 6, whether Rapport keeps the hand from running dry (Neglect, game 555), and whether PW still draws a chain starter.

Splash variant (PB Neglect splash): play it against each of PW, PU, PR and PG, swapping seats, and compare with the 15 wins to 7 of the plain PB (against PW 4 to 2, PU 4 to 2, PR 5 to 0, PG 2 to 3).
Look at whether Resignation's cost (a spare card) is easy to pay, whether Rashness and Shock answer the other decks' early mythics (Fulfillment, Orderliness, Reverie, Ardor) in time, whether Fear's replayed Vengeance or Nosiness is worth the mood it bounces,
whether the extra plays empty PB's hand (does Neglect fire more often?), and whether board values keep up with PG's scaling.

For every game note the Power Duel setup (15 cards, one mythic, no extra mythics), the result by round, the largest turn, and whether any player
ran short of cards or decked out.

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
