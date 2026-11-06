# Play test results

Results of play tests, newest session last. The log format is the one in `design/playtest-decks.md`. Per-card ratings of
fun and clarity can only come from the testers, so they are left out where the game logs cannot show them.

## Session 1: E1 Free-play cycle against B Baseline (6 games)

**Source.** The simulator exports of games 493 to 498 (6 November: Duel, custom decklists, 20 cards each, first to 3 round
wins, starting hands of 5). Two testers played, and each piloted E1 three times and B three times, swapping decks every game.
The logs show every mood played, the scores, the forced choices (Compulsion, Suspicion) and the end-of-round draws. They do
not show optional "may" choices that move no card into play (Levity's or Reverie's "bottom a card, draw", Nostalgia's pickup)
or the starting hands, so those are not assessed here.

### Summary

| | |
|---|---|
| Result | **B won all 6 games (6 to 0) and 18 of the 19 rounds.** E1 won one round (game 498, round 1). |
| Both testers lost with E1 | Each tester lost all three of their E1 games, and each won all three of their B games, so this is the decks, not the pilot. |
| Game length | 3 rounds in five games, 4 in one. Three rounds is the shortest possible game to 3 round wins. 5 to 21 minutes per game. |
| Round scores, E1 | round 1: 2.2 on average; round 2: 4.5; round 3: 5.5 (6 games). |
| Round scores, B | round 1: 3.0; round 2: 5.8; round 3: 8.7 (about one 3 per round, stacking: 3, 6, 9). |
| Plays per game | E1 4.7, B 3.3. E1 used 11 extra plays in total (none in game 494); the most plays in one turn was 4 (game 497, round 1). |
| Ties | Three rounds tied (9 to 9, 6 to 6, 3 to 3) and all went to B, who had played first each time. This matches the simulator's rule that a tie goes to whoever played earliest. |

### Deductions

1. **E1 does not break the game; as built it cannot win.** The five free-play commons did their job, but the extra plays have
   nothing valuable to carry. Eight of E1's 20 cards print 0, two print 1, five print 2 and five print 5 (average 1.85), against
   about 2.65 for B before its 3-to-6 conditionals. E1's best turn, four plays (Rashness, Familiarity, Fear, Affinity) in game 497,
   round 1, scored 3 and tied B's single 3, which B won by playing first. A deck that turns a hand into a board faster but
   whose board is worth nothing is not an engine problem. The question this session was meant to answer, how strong the
   extra-play engines get when they have bodies, is still open.
2. **The engines are limited by hand size.** With a 5-card start and one draw per lost round, bursts happen in round 1 (up to
   4 plays) and shrink to about 1 play by round 3. B finished with 1 to 3 cards in hand in all six games. E1 finished with an empty hand in
   two (495 and 497) and with unplayable or unused cards in the other four. This supports the checklist's worry that hands
   run dry, but for engine decks and not for ordinary ones.
3. **The colorless 5-gate commons were E1's best scoring cards.** E1's only round win (game 498, round 1) was Remorse (0) into
   Resentment (5), 5 to 3. Contentment (5) carried E1 to 5 to 6 and 6 to 6 in round 2 of games 494 and 496, and B's own
   Impatience (5) was the biggest card in B's 11 in game 495. Their cost is the color requirement: Resentment sat in hand at the end
   of games 493 and 494 (no black mood), and Detachment never came into play. So 5 does not look too low or too high: the
   gate is strong when you have the color and dead when you don't. Nothing here argues for changing it to 4.
4. **Hand attacks are strong against small hands.** B played Suspicion three times (E1 discarded a card each time, in 495, 496
   and 497) and Compulsion twice (493 and 495 took a card). E1's hands were small, so each one removed a real
   option. In game 496 B's Hate also seems to have put E1's Contentment (5) on the bottom of the deck (it is in E1's deck at
   the end although it was played), which would explain why E1 scored only 2 in round 3. This helps the hand-pressure axis (Neglect, Nosiness, Greed): the cards work against a small hand. It also supports the
   Neglect finding that empty hands come up mainly against engine decks.
5. **The baseline is a real opponent.** B scores about one 3 per round and wins in the minimum 3 rounds. Any deck that does
   not reach about 3, 6 and 9 over three rounds loses. That is a useful yardstick: an engine has to beat the curve 3 / 6 / 9.
6. **No rules or simulator problems appeared.** Plays, grants (Familiarity and Modesty restrictions, Resilience's pile
   grant), forced choices and tie-breaks all behaved as written. Familiarity came back to hand and was replayed in game 497 (Fear's bounce or Nostalgia's pickup).

### What I would do next

- **Rebuild E1 with bodies (E1b); the decklist is now in `design/playtest-decks.md`.** Keep the five free-play commons, Affinity, Familiarity, Modesty, Reverie and the five gates,
  and replace the 0-value cards that are not engines (Adrenaline, Resilience, Reinvigoration, Wistfulness) with 3-value
  bodies, then replay against B. If E1b still loses, the free-play cycle is too weak; if it wins, check how often.
- **Test the cards that never showed up.** Overconfidence and Reinvigoration were never drawn, Haunting was drawn once and
  never played (game 494), and Detachment was never played. They need more games, or a deck built around them, before any
  verdict.
- **Questions for the testers** (the logs cannot answer them):
  - Game 494: E1 passed round 1 holding Levity and Modesty, and finished with Haunting, Levity, Modesty and Resentment unplayed. Was that a
    choice, or did the free-play cards not feel worth playing?
  - Game 498: E1 passed in rounds 2 and 3 with playable cards in hand (Nostalgia, Rashness) and lost both. Was that deliberate, for
    example to lose a round and draw a card? If so, that is worth knowing as a strategy.
  - Game 496, round 3: E1 held Impatience (5) with Rashness (red) in play, and chose Affinity instead. Was Impatience playable?
  - Were Levity's and Reverie's draw options used? Were any of the E1 cards unclear?
  - Fun and clarity for each card.

### Game logs

**Game 493.** B (seat 0) against E1 (seat 1); E1 went first. B won 3 to 0 in rounds.
- Scores: round 1: B 3, E1 2; round 2: B 6, E1 4; round 3: B 9, E1 9 (tie, B played first).
- Longest turn: 2 plays (E1 round 1: Levity then Reverie; round 2: Modesty then Nostalgia).
- Hands: E1 ran out of legal plays in round 2 (Resentment stuck in hand, no black mood); B finished with 3 cards.
- Decided: B's Compulsion took a card from E1 in round 1; round 3 was a tie that B won by playing first. The closest game of the six.
- Unclear text: none seen. Simulator bugs: none.

**Game 494.** E1 (seat 0) against B (seat 1); E1 went first. B won 3 to 0.
- Scores: 0 to 3, 5 to 6, 5 to 9.
- Longest turn: 1 play every round (E1: Resilience, Contentment, Adrenaline).
- Hands: E1 finished with 4 cards (Haunting, Levity, Modesty, Resentment); B with 2.
- Decided: E1 never used its free-play cards, so this game says little about the engine. B's Determination and Exuberance were 6 each.

**Game 495.** B (seat 0) against E1 (seat 1); E1 went first. B won 3 to 0.
- Scores: 3 to 2, 6 to 4, 11 to 6.
- Longest turn: 3 plays (E1 round 1: Levity, Familiarity, Resilience, scoring 2). B's Compulsion took a card after it.
- Hands: B's Suspicion made E1 discard in round 2. E1 finished with an empty hand and six moods, all low value.
- Decided: B's Impatience (5) in round 3.

**Game 496.** E1 (seat 0) against B (seat 1); E1 went first. B won 3 to 0.
- Scores: 1 to 3, 6 to 6 (tie, B played first), 2 to 6.
- Longest turn: 2 plays (E1 round 3: Rashness, Affinity).
- Hands: B's Suspicion made E1 discard Reverie in round 2. E1 finished with Detachment and Impatience in hand.
- Decided: the round 2 tie, then B's Hate bottomed E1's Contentment (5) before round 3.
- Question: Impatience was in hand with Rashness in play in round 3 (see above).

**Game 497.** B (seat 0) against E1 (seat 1); B went first. B won 3 to 0.
- Scores: 3 to 3 (tie, B played first), 5 to 3, 8 to 6.
- Longest turn: 4 plays (E1 round 1: Rashness, Familiarity, Fear, Affinity), scoring only 3 after B's Suspicion had made E1 discard.
- Hands: E1 finished with an empty hand; B with 2 cards.
- Decided: the round 1 tie. This was E1's best chance: the biggest burst of the session produced a tie.

**Game 498.** E1 (seat 0) against B (seat 1); E1 went first. B won 3 to 1, four rounds.
- Scores: 5 to 3 (E1 won: Remorse then Resentment), 5 to 6, 5 to 9, 7 to 21.
- Longest turn: 2 plays (E1 round 1; B round 4: Exuberance, then Indignation as an extra play from Joy).
- Hands: E1 passed in rounds 2 and 3 holding playable cards and finished with 4 cards in hand (Nostalgia, Rashness, Reverence,
  Wistfulness); B finished with 1.
- Decided: B stacked five moods worth 21 by round 4 while E1 stalled.

### Notes by card (from what the logs show)

| Card | What the games showed | Notes |
|---|---|---|
| Levity | Played first in 493 and 495 (then Reverie; then Familiarity and Resilience). Held unplayed in 494. | Worked as the opener for a 2 or 3 play turn. Was its draw option used? Unknown. |
| Fear | Played in 497 round 1; Familiarity was replayed in round 2 (Fear's bounce or Nostalgia's pickup). | Worked as written. |
| Nostalgia | Played in 493, 495, 497. | Gives an extra play; pickups not visible. |
| Remorse | Played in 498 round 1, then Resentment. | Enabled E1's only round win. |
| Rashness | Played in 496 and 497; held in 498. | Its removal had few targets, since B's moods are mostly 3. In 496 B's Hate (0) ended in B's discard pile, so it probably hit that. The extra play is what it mostly did. |
| Affinity | Played in 496 and 497 as the last link of a chain. | Worked; the number 5 on the gates also turns it on. |
| Familiarity, Modesty | Familiarity played in 495 and 497, Modesty in 493 and 495. | Worked as restricted extra plays; low value bodies. |
| Reverie | Played in 493, 495, 498. | Draw option not visible. |
| Reverence, Contentment, Resentment, Impatience | Played 1, 2, 1 and 1 times. | The best scoring cards in E1, but color-dependent (see deduction 3). |
| Detachment | Drawn once, never played. | No blue mood. |
| Overconfidence, Reinvigoration | Never drawn. | No data. |
| Haunting | Drawn once (494), never played. | No data. |
| Adrenaline, Resilience, Wistfulness | Played once, twice and once; 0, 0 and 1 value. | Bodies too small to matter. |

Status changes: none yet. No card has enough evidence to move from `idea`; the free-play commons and the gates will be
retested in E1b.
