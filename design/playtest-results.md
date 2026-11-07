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

## Session 1b: E1 mirror (2 games)

**Source.** The simulator exports of games 500 and 501 (6 November, evening): the same Duel setup, both players on the original E1
list (not E1b), the two testers from session 1. Haunting was already the new version here (printed 0, plays kept only if you still
have it). The logs show every mood played, the cards moved and drawn by each effect, and the scores.

### Summary

| | |
|---|---|
| Result | The tester who was seat 0 (P1) won both games: 3 to 0 in rounds in game 500, 3 to 2 in game 501 (5 rounds, the longest game so far). |
| Scores | Game 500: 5 to 2, 5 to 2, 10 to 7. Game 501: 0 to 2, 5 to 7, 12 to 7, 12 to 7, 12 to 12. |
| Biggest turn | **10 plays in one turn** (game 500, round 1, from the opening hand). |
| Ties | One: game 501, round 5, 12 to 12, won by the player who played first. |
| Time | 18 and 11 minutes. |

### Insights

1. **The engine can go off, and it does not win by points.** In game 500 round 1, P1 played 10 moods: Rashness, Overconfidence,
   Affinity, Reverie, Fear (which bounced Rashness), Rashness again, Reinvigoration, then Affinity, Reverie and Overconfidence from
   the pile. The opening hand was Rashness, Overconfidence, Affinity, Reverie and Reinvigoration (the draws came from Reverie
   during the turn), a very good hand for this deck. The turn scored only 5 against 2, but it did three other things: two
   Rashness removed two of the opponent's three cheap moods, Reverie drew four cards, and the lead held (the Overconfidence
   penalty meant P1 could not play in round 2 and still won it 5 to 2). So the burst converts into tempo, removal and cards more than
   points. It is possible from an opening hand, so it can decide a game early, but it needs several of the deck's best cards at once.
2. **Reverie is the keystone.** All four cards drawn in that turn came from Reverie's "each time you play another mood" trigger,
   and its loot kept feeding the chain. This is worth a close look: with a long chain it draws a card per play. It was also the
   card that looked weak in session 1, because it was never played with a chain.
3. **Rashness is a real removal card in this deck.** Its extra play is not what matters here: against a board of cheap moods it
   cleared two of three. Against the baseline (all 3s) it had no targets. Note for game 501: P18's Rashness had three value-0
   targets in play (Haunting, Adrenaline, Resilience) in rounds 3 and 4 and removed none. Was that a choice?
4. **Reinvigoration is value-neutral.** In game 500 P1's board was worth 5 before and 5 after (three of five moods came back, "up
   to that many"), and in game 501 P18's board was worth 7 before and 7 after (all four came back), a round that P18 then lost 7 to
   12. It does not replay "a whole board" for free in practice: it costs the turn (you can't play anything else) and only pays if
   the replayed moods have effects worth repeating (Reverie's draws in game 500, nothing in game 501). The worry that it scales and
   runs away has not shown up, and it may be too weak outside a deck of strong after-playing effects. More games needed.
5. **Haunting at 0 is slow, not strong.** In game 501 P1 played it in round 1 (0 points, lost the round 0 to 2), discarded three
   cards and replayed exactly those three from the pile in round 2 (Resentment, Adrenaline, Resilience), scoring 5 and losing 5 to
   7. That is no card advantage, one round late. In game 500 P18 played it with nothing discarded. It also survived the whole
   game in 501 although the opponent held Rashness with value-0 targets. So no sign it is too strong now; whether it is too
   weak needs a deck that wants it (Longing, Brooding, Dejection, Martyrdom).
6. **Overconfidence's penalty is real.** P1 passed round 2 of game 500 and round 4 of game 501 because of it, and its second play
   from the pile re-applied it. It is a front-loaded card: the board you build in the turn has to carry the next one.
7. **The 5-gates decided the close rounds again.** Reverence, Resentment, Detachment and Contentment were the 5-point plays in
   every close round (game 500 round 3; game 501 rounds 2, 3 and 5). The mirror matches two decks of near-identical bodies, so
   the gate you have the color for is what separates the scores.
8. **Ties go to the first player, again.** The game 501 round 5 tie (12 to 12) went to P1, who had won round 4 and so played first.
   With two low-value decks, ties will be common; first play is worth about a point.

### Questions for the testers

- Game 501: P18's Rashness had targets in rounds 3 and 4 and removed nothing. Was that a choice, or was the prompt missed?
- Game 501, round 5: P1 passed holding Nostalgia, with nothing to lose. Was that a choice?
- Game 500, round 2: P18 played Haunting with no discards. Was that a misplay or to bank the body?
- Fun and clarity, especially for Reverie's loot and Reinvigoration.

### Game logs

**Game 500.** P1 (seat 0) against P18 (seat 1); P18 went first. P1 won 3 to 0.
- Scores: 5 to 2, 5 to 2, 10 to 7.
- Longest turn: P1's 10 plays in round 1 (above).
- Hands: P1 finished with 2 cards (Remorse, Resilience), P18 with 2 (Contentment, Resilience).
- Decided: round 1. After it P1's lead held even with a skipped round 2.
- Simulator bugs: none seen.

**Game 501.** P1 (seat 0) against P18 (seat 1); P18 went first. P1 won 3 to 2 in rounds, five rounds.
- Scores: 0 to 2, 5 to 7, 12 to 7, 12 to 7, 12 to 12 (tie, P1 played first).
- Longest turn: P18's Reinvigoration in round 4 (5 plays, no change in score).
- Hands: P1 finished with Nostalgia, P18 with Haunting.
- Decided: P1's round 3 (12 against 7: Resentment, Detachment, Overconfidence and three 0-value moods) and the round 5 tie.
- Simulator bugs: none seen.

### Notes by card (mirror games)

| Card | What the games showed |
|---|---|
| Reverie | Drew 4 cards in one turn (game 500) by looting on each later play. Also played alone as a 2. |
| Reinvigoration | Value-neutral twice (5 to 5, 7 to 7); costs the rest of the turn. |
| Overconfidence | Gave two extra plays; the next-turn restriction made P1 pass twice. |
| Rashness | Removed two cheap moods in game 500; unused with targets in game 501. |
| Affinity, Fear | Links in the chain (Fear bounced Rashness for a second removal). |
| Haunting | Banked 3 plays once (game 501) and returned the same 3 cards from the pile; no discards once. |
| Gates (Reverence, Resentment, Detachment, Contentment) | The 5-point plays in the close rounds. |

## Session 1c: E2 Green replay against B Baseline (4 games)

**Source.** The simulator exports of games 502 to 505 (6 to 7 November). The tester in seat 0 of the earlier games (P1) played in all
four and won all four. The other seat was a practice bot in games 502 (E2), 503 (B) and 505 (B), identified by the search
results in the logs, and the second tester in game 504 (E2). So the games show how the decks play in a good player's hands, but not
which deck is stronger: P1 won with B (502, 504) and with E2 (503, 505).

### Summary

| | |
|---|---|
| Result | B (P1) beat E2 in 502 (3 to 2) and 504 (3 to 0). E2 (P1) beat B in 503 (3 to 2) and 505 (3 to 2). |
| Round scores, E2 played by P1 | Game 503: 0, 6, 12, 22, 36. Game 505: 6, 3, 0, 14, 23. |
| Round scores, B played by the bot | Game 503: 3, 6, 9, 15, 18. Game 505: 3, 6, 7, 12, 17. |
| Game length | 5 rounds in three games, 3 in one. Both E2 wins came on the fifth round. |
| Ties | Two: game 503 round 2 (6 to 6) and game 504 round 1 (3 to 3). Both went to B, who played first. |
| Time | 10 to 12 minutes, except game 505: 53 minutes, about 39 of them on E2's side. |

### Insights

1. **E2 is a late-game snowball.** In both wins E2 lost or tied the first rounds, then passed B in round 4: 22 against 15 and 36
   against 18 in game 503, 14 against 12 and 23 against 17 in game 505. B's score grows by about 3 a round (it tops out at 17 or
   18 by round 5), E2's grows by 9 to 14 a round once its board has 6 to 9 moods. The margin was thin: B had two round wins
   in each game, E2 won the last three rounds of game 503, and in game 505 it lost rounds 2 and 3 and won rounds 1, 4 and 5.
2. **The engine is the pile loop.** Carelessness mills two cards, Resilience and Thrift let you play moods worth 3 or less from the
   pile, and replaying Carelessness from the pile mills two more: in game 503 round 4 Carelessness (from the pile) milled
   Perseverance and Vindication (both worth 2), and in round 5 both were played from the pile as free extra plays. That is the card
   advantage the green axis was designed for, and by round 5 the board was 9 moods and 36 points. It needs three or four rounds to
   assemble, which is why E2 trails early.
3. **Reinvigoration has two uses, and neither is the feared one.**
   - Game 502 round 3 (the bot): Pacifism appears to have suppressed Honesty (E2 scored only 3 in round 2). Reinvigoration put Honesty and Restlessness into the pile and
     they came back unsuppressed, so the turn scored 9 (round 3 won 9 to 7). That makes it an answer to suppression.
   - Game 505 round 3: P1 used it as a reset. It put the only other mood (Carelessness) into the pile and replayed Resilience, so
     the board was worth 0 that round (lost 0 to 7), but it switched on Resilience's pile plays for the 14 to 12 and 23 to 17 rounds that followed.
   So it is not the runaway engine the checklist feared: it costs the whole turn. It was never played in game 504.
4. **Honesty is a 6 on turn one in a one-color deck.** In games 502 and 505 it was played first and scored 6 against B's 3, winning
   round 1 both times. B is five colors, so for B it would almost never be 6. This is what the card is for, but a 6 on your first
   play at uncommon is notable: check it in a two-color deck, where the condition is harder.
5. **Green has no removal, and B's cheap removal slowed it.** Vengeance removed E2's highest mood in 503 round 1 (0 to 3) and
   in 505 round 2 (Honesty); Disdain, Hate and Shock took a mood each in game 502 rounds 4 and 5 (1 and 3 points against 9 and 11); Panic and
   Hate kept a one-mood board in game 504 (3, 3, 3 against 3, 6, 6). E2 recovers when its pile loop is running, and not before.
6. **Ties go to the first player, again.** Both ties (game 503 round 2, game 504 round 1) went to B, who played first. In total that is
   six ties in the three sessions, all won by the first player. A first-turn 3 to 3 decides round 1.
7. **A slow start is possible.** In game 504 E2's player finished with Contentment, Perseverance, Possessiveness, Reinvigoration and
   Resilience in hand and a one-mood board all game. The loop may need a first turn that starts it, and this opening may not
   have had one; the logs cannot say why those cards were not played (see the questions).

### Questions for the testers

- Game 505 took 53 minutes, 39 of them on E2's side. Was that a break, or is the pile loop too heavy to play (many choices per turn,
  Wastefulness's prompt every turn)?
- Game 505, round 3: was the Reinvigoration reset deliberate, to switch on Resilience?
- Game 504: what kept E2's hand (Resilience, Reinvigoration, Possessiveness, Perseverance, Contentment) from being played?
- Fun and clarity for Carelessness, Resilience, Thrift and Reinvigoration.

### Game logs

**Game 502.** B (P1, seat 0) against E2 (bot, seat 1); B went first. B won 3 to 2.
- Scores: 3 to 6 (E2), 4 to 3 (B), 7 to 9 (E2), 9 to 1 (B), 11 to 3 (B).
- Longest turn: 3 plays (E2, round 3: Reinvigoration, then Honesty and Restlessness from the pile).
- Decided: rounds 4 and 5, when Disdain, Hate and Shock took E2's board.
- Simulator bugs: none seen.

**Game 503.** E2 (P1, seat 0) against B (bot, seat 1); E2 went first. E2 won 3 to 2.
- Scores: 0 to 3, 6 to 6 (tie, B), 12 to 9, 22 to 15, 36 to 18.
- Longest turn: 3 plays (round 5: Thrift, then Vindication and Perseverance from the pile).
- Hands: E2 finished with 1 card, B with 3.
- Decided: rounds 4 and 5, once the pile loop and Kinship were running.

**Game 504.** B (P1, seat 0) against E2 (second tester, seat 1); B went first. B won 3 to 0.
- Scores: 3 to 3 (tie, B), 6 to 3, 6 to 3.
- Longest turn: 1 play every round.
- Decided: the round 1 tie, then Panic and Hate on E2's single mood.
- Hands: E2 finished with 5 cards unplayed.

**Game 505.** E2 (P1, seat 0) against B (bot, seat 1); B went first. E2 won 3 to 2.
- Scores: 6 to 3, 3 to 6, 0 to 7, 14 to 12, 23 to 17.
- Longest turn: 3 plays (round 4: Thrift, Contentment, Honesty from the pile).
- Decided: round 3's Reinvigoration reset, which turned the game around by round 4.
- Simulator bugs: none seen.

### Notes by card (E2 games)

| Card | What the games showed |
|---|---|
| Honesty | 6 on turn one in a one-color deck (502, 505). Replayed from the pile as a 6 again (503, 505). |
| Carelessness | Mill fuel; replayed from the pile it milled the next two plays (503). |
| Resilience, Thrift | Let the pile loop run; Resilience at 0 is a body only. |
| Reinvigoration | Cleaned off Pacifism's suppression (502); a reset that cost a round but switched on Resilience (505). |
| Kinship, Vindication, Perseverance, Urgency | Part of the 22 and 36 point boards in game 503. |
| Wastefulness | Prompts at the start of each turn (two prompts in game 503); worked. |
| Determination, Optimism | One mood a round in game 504, 3 points each. |
| Possessiveness | Not played (never had 5 cards in the pile in game 504). |
