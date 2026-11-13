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
| Game length | 3 rounds in five games, 4 in one. Three rounds is the shortest possible game to 3 round wins. |
| Round scores, E1 | round 1: 2.2 on average; round 2: 4.5; round 3: 5.5 (6 games). |
| Round scores, B | round 1: 3.0; round 2: 5.8; round 3: 8.7 (about one 3 per round, stacking: 3, 6, 9). |
| Plays per game | E1 4.7, B 3.3. E1 used 11 extra plays in total (none in game 494); the most plays in one turn was 4 (game 497, round 1). |

### Deductions

1. **E1 does not break the game; as built it cannot win.** The five free-play commons did their job, but the extra plays have
   nothing valuable to carry. Eight of E1's 20 cards print 0, two print 1, five print 2 and five print 5 (average 1.85), against
   about 2.65 for B before its 3-to-6 conditionals. E1's best turn, four plays (Rashness, Familiarity, Fear, Affinity) in game 497,
   round 1, scored 3 against B's single 3 and lost the round. A deck that turns a hand into a board faster but
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
   grant), forced choices all behaved as written. Familiarity came back to hand and was replayed in game 497 (Fear's bounce or Nostalgia's pickup).

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
- Scores: round 1: B 3, E1 2; round 2: B 6, E1 4; round 3: B 9, E1 9.
- Longest turn: 2 plays (E1 round 1: Levity then Reverie; round 2: Modesty then Nostalgia).
- Hands: E1 ran out of legal plays in round 2 (Resentment stuck in hand, no black mood); B finished with 3 cards.
- Decided: B's Compulsion took a card from E1 in round 1; round 3 ended 9 to 9. The closest game of the six.
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
- Scores: 1 to 3, 6 to 6, 2 to 6.
- Longest turn: 2 plays (E1 round 3: Rashness, Affinity).
- Hands: B's Suspicion made E1 discard Reverie in round 2. E1 finished with Detachment and Impatience in hand.
- Decided: the 6 to 6 second round, then B's Hate bottomed E1's Contentment (5) before round 3.
- Question: Impatience was in hand with Rashness in play in round 3 (see above).

**Game 497.** B (seat 0) against E1 (seat 1); B went first. B won 3 to 0.
- Scores: 3 to 3, 5 to 3, 8 to 6.
- Longest turn: 4 plays (E1 round 1: Rashness, Familiarity, Fear, Affinity), scoring only 3 after B's Suspicion had made E1 discard.
- Hands: E1 finished with an empty hand; B with 2 cards.
- Decided: round 1 (3 to 3). This was E1's best chance: the biggest burst of the session produced only 3 points.

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
- Scores: 0 to 2, 5 to 7, 12 to 7, 12 to 7, 12 to 12.
- Longest turn: P18's Reinvigoration in round 4 (5 plays, no change in score).
- Hands: P1 finished with Nostalgia, P18 with Haunting.
- Decided: P1's round 3 (12 against 7: Resentment, Detachment, Overconfidence and three 0-value moods) and round 5 (12 to 12).
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

### Insights

1. **E2 is a late-game snowball.** In both wins E2 trailed in the early rounds, then passed B in round 4: 22 against 15 and 36
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
6. **A slow start is possible.** In game 504 E2's player finished with Contentment, Perseverance, Possessiveness, Reinvigoration and
   Resilience in hand and a one-mood board all game. The loop may need a first turn that starts it, and this opening may not
   have had one; the logs cannot say why those cards were not played (see the questions).

### Questions for the testers

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
- Scores: 0 to 3, 6 to 6, 12 to 9, 22 to 15, 36 to 18.
- Longest turn: 3 plays (round 5: Thrift, then Vindication and Perseverance from the pile).
- Hands: E2 finished with 1 card, B with 3.
- Decided: rounds 4 and 5, once the pile loop and Kinship were running.

**Game 504.** B (P1, seat 0) against E2 (second tester, seat 1); B went first. B won 3 to 0.
- Scores: 3 to 3, 6 to 3, 6 to 3.
- Longest turn: 1 play every round.
- Decided: round 1 (3 to 3), then Panic and Hate on E2's single mood.
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

## Session 1d: E1 Free-play cycle against E2 Green replay (6 games)

**Source.** The simulator exports of games 506 to 511 (7 November). The first tester (P1) played in all six: E2 in 506, 508 and 510,
E1 in 507, 509 and 511. The other seat was a practice bot in 506 (E1), 507 (E2), 508 (E1) and 511 (E2), and the second tester in 509
(E2) and 510 (E1).

### Summary

| | |
|---|---|
| Result | **E2 won all six games (6 to 0) and 18 of the 20 rounds.** E1 won two rounds: game 506 round 1 (0 to 0) and game 509 round 1 (4 to 3). |
| Every pilot pairing | E2 beat E1 with the practice bot on E2 against a human E1 (507, 511), with a human on E2 against a bot on E1 (506, 508), and with two humans (509, 510). So this is the decks, not the pilots. |
| Scores by round, E2 | 506: 0, 5, 8, 21. 507: 3, 8, 11. 508: 3, 11, 15. 509: 3, 8, 11, 14. 510: 6, 10, 18. 511: 6, 11, 16. |
| Scores by round, E1 | 506: 0, 0, 5, 7. 507: 2, 3, 8. 508: 1, 7, 9. 509: 4, 5, 5, 5. 510: 4, 9, 12. 511: 2, 7, 9. |
| Game length | 3 rounds in four games, 4 in two. |
| Biggest turn | 9 plays (E2, game 506 round 4, scoring 21 against E1's 7). |

### Insights

1. **E1, as built, is clearly the weaker deck.** E2 led after round 2 in all six games and the gap grew: by round 3 E2 had 8 to 18 against E1's
   5 to 12. This matches session 1 (E1 lost 0 to 6 to B). The E1b list, with bodies in place of its zero-value cards, is the right next
   test, and E1 should now be treated as a baseline for how weak a pure engine is.
2. **The one-color gate is a free 5.** E2 is mono-green, so Contentment (5) is always playable. E2 played it in round 2 in four of the
   six games (506, 507, 508, 509) and it was the difference each time: for example 8 to 3 in game 507 and 11 to 7 in game 508. In a
   one-color deck the gate is simply the best common body (5 where the other commons are 3), at no cost. That is the case the
   gate was priced for in a five-color pile, and the checklist's "5 against 4" question now has data: in a mono-color deck, 5 is
   very strong. Worth testing the fallback of 4 if one-color decks stay this good.
3. **The discard pile is shared, and Haunting can feed the opponent's pile engine.** In game 511 round 1, E1 played Modesty and
   then Haunting (value 0) and discarded its hand (Detachment, Reverie, Wistfulness). E2 played next in the same round and used
   Thrift to play Wistfulness from the pile, then Reverie from the pile (the Wistfulness trigger); in round 2 Nostalgia put
   Detachment into E2's hand and it played it. All three of E1's discards ended up on E2's side (E1's Reverie and Detachment were in E2's
   board at the end), and E1's banked plays had nothing left to play (round 2: Reverence and a pass). So Haunting's discards sit in
   a shared pile through the rest of the round and any turn that comes before yours, and a pile deck like E2 takes them. This is a
   real weakness, separate from its 0 value.
4. **Reinvigoration is neutral again, except with Urgency.** E1's board was worth 5 before and 5 after it in game 509 (four
   replays). The exception is game 509 round 4 on E2's side, where Reinvigoration plus three replays made four plays and turned
   Urgency from 3 to 6 (11 to 14). E2's nine-play turn in game 506 scored 21, with Restlessness, Kinship and the replays all in it. It pays when a replayed mood counts plays or
   re-triggers something; otherwise it costs the turn.
5. **E1's all-in turn still loses.** Game 510 round 3: E1 played Overconfidence, Affinity, Fear and Nostalgia (4 plays), scored 12 and
   lost 12 to 18. It finished with seven moods and an empty hand. The pattern from sessions 1 and 1b holds: the burst makes tempo and a wide
   board but little value.
6. **Honesty is again a 6 on turn one** (game 510 round 1, 6 to 4). Kinship (+1 for each of your moods that shares a color with
   another) was in E2's biggest turns (games 506, 508, 511).

### Questions for the testers

- Game 511: was the Haunting discard deliberate, and did you expect E2 to take the cards from the pile?
- Game 509 round 4: both players played Reinvigoration in the same round. Was the E1 one a choice or the only play available?
- Fun and clarity for Haunting's delay and for sharing the pile.

### Game logs

**Game 506.** E2 (P1, seat 0) against E1 (bot, seat 1); E1 went first. E2 won 3 to 1 (four rounds).
- Scores: 0 to 0, 5 to 0, 8 to 5, 21 to 7.
- Longest turn: 9 plays (E2, round 4: Restlessness, Kinship, Reinvigoration, then six replays from the pile).

**Game 507.** E1 (P1, seat 0) against E2 (bot, seat 1); E1 went first. E2 won 3 to 0.
- Scores: 2 to 3, 3 to 8, 8 to 11.
- Decided: Contentment in round 2 (8 to 3).

**Game 508.** E2 (P1, seat 0) against E1 (bot, seat 1); E2 went first. E2 won 3 to 0.
- Scores: 3 to 1, 11 to 7, 15 to 9.
- Longest turn: 3 plays (E1 round 2: Remorse, Wistfulness, Contentment).

**Game 509.** E1 (P1, seat 0) against E2 (second tester, seat 1); E1 went first. E2 won 3 to 1 (four rounds).
- Scores: 4 to 3 (E1), 5 to 8, 5 to 11, 5 to 14.
- Longest turn: 5 plays (E1 round 4: Reinvigoration and four replays, no change in score).
- Decided: Contentment in round 2, then Urgency at 6 after E2's Reinvigoration.

**Game 510.** E2 (P1, seat 0) against E1 (second tester, seat 1); E2 went first. E2 won 3 to 0.
- Scores: 6 to 4, 10 to 9, 18 to 12.
- Longest turn: 4 plays (E1 round 3: Overconfidence, Affinity, Fear, Nostalgia).

**Game 511.** E1 (P1, seat 0) against E2 (bot, seat 1); E1 went first. E2 won 3 to 0.
- Scores: 2 to 6, 7 to 11, 9 to 16.
- Decided: round 1, when Haunting's discards went to E2 (above).
- Simulator bugs: none seen in any of the six games.

### Notes by card (E1 against E2)

| Card | What the games showed |
|---|---|
| Contentment | A free 5 in a one-color deck: round 2 in four of six games. |
| Haunting | Its discards fed E2's pile plays in game 511 (shared discard pile). |
| Reinvigoration | Neutral for E1 (game 509); +3 for E2 with Urgency (game 509); part of E2's nine-play, 21-point turn (game 506). |
| Honesty, Kinship | Honesty was 6 on turn one; Kinship was in E2's biggest turns. |
| Overconfidence, Affinity, Fear, Nostalgia | A 4-play turn that scored 12 and still lost (game 510). |
| Thrift, Wistfulness, Nostalgia (E2) | Took E1's discarded cards in game 511. |

## Draft 1: quick draft between two human players (match 150, 2 games)

**Source.** The simulator exports of the two games of one quick-draft match (games 490 and 499, 6 to 7 November), which also hold the
draft itself. It is a two-player quick draft from a random pool of 48 distinct cards (47 are cards of this set and one is an original),
four rounds: in each round each player draws a pile of six, keeps two, and the other player keeps two of the remaining four (two are left
over). Each player ends with 16 cards and builds a 12-card deck. Both players were human (user 8 and user 1, the first tester). The
games were played asynchronously over about two days. The only chat lines were one joke each, so they say nothing about the cards.

### Summary

| | |
|---|---|
| Result | User 8 (white, black, green, plus Desperation and Rashness) won both games, 3 to 0 (game 490) and 3 to 2 (game 499). User 1 played a red deck with black and white. |
| Pool | 17 commons, 16 uncommons, 10 rares and 5 mythics; by color 11 red, 9 white, 9 blue, 8 black, 8 green and 3 colorless. |
| Left undrafted | 16 of the 48 cards: 9 commons, 5 uncommons, 2 rares and no mythics. |

### Draft insights

1. **Rarity drove the picks.** All five mythics were drafted (Haunting, Wistfulness, Grudge, Unity, Restraint); 2 of 10 rares, 5 of 16
   uncommons and 9 of 17 commons were left. Two mythics were passed by the first picker and taken by the other player (Unity and
   Restraint), and neither mattered: Unity needs five moods that share a color, which neither deck reached in games of three and five
   rounds, and Restraint stayed on the bench.
2. **Red was the deepest color and blue the shallowest.** All 11 red cards were drafted (user 1 took ten of them), but 6 of the 9 blue
   cards and 5 of the 8 green cards were left (blue: Distrust, Anticipation, Turmoil, Deflection, Chagrin, Prudence; green:
   Carelessness, Resolve, Honesty, Restlessness, Wariness). Only 3 of the 9 blue cards were drafted at all, and one of those
   (Admiration, a rare with new art) was benched. This is one draft with two players, so treat it as a prompt to look at blue's
   and green's commons and uncommons rather than a verdict. The unpicked green cards are the 3-to-6 conditionals and Carelessness.
3. **Both colorless gates were left undrafted** (Reverence in round 1, Detachment in round 4), after both players saw them in a pile.
   In a five-color pool a gate is hard to count on, which matches the checklist's concern; in a one-color deck (session 1d) it was a
   free 5. So the gate is a deck-dependent card: weak to a drafter, strong to a mono-color deck.
4. **Rudeness (a tier 1 white rare) and Greed (a black rare) were left**, as was Schadenfreude. Nobody wanted to build around them
   in a 12-card deck of two or three colors.
5. **Benched picks:** user 8 left out Admiration, Discernment, Restraint and Fairness; user 1 left out Indignation, Resignation,
   Vindictiveness and Frenzy. Grudge was in user 1's deck but never drawn, so it gave no data.

### Game insights

6. **Haunting was very strong in game 490, and that was the old version.** Its round 1 score was 2, so Haunting was still a 2 with no
   condition (the nerf to a 0 was merged later that day). User 8 discarded four cards from hand (Modesty, Malevolence, Vindication,
   Solidarity), then in round 2 replayed all four from the pile as free plays and scored 17 against 3. Malevolence, replayed from
   the pile, removed user 1's only mood. User 1's red deck had no pile plays, so nothing could take the cards or stop it, and
   user 8 won the game from there (12 to 6 in round 3). This is the burst the nerf was meant to answer. Under the new text it needs
   Haunting still in play at the start of the turn; user 1's deck had Volatility (a random mood worth 1 or less is put into the
   discard pile each turn), which would have been a real answer to a 0.
7. **In game 499 user 8 used Haunting as discard fodder.** Longing discarded Haunting from hand to put Martyrdom and Jealousy back
   into hand. Whether that reflects the changed Haunting, or just a different hand, is unknown; ask.
8. **The cheap-2 white and black cards worked together.** Solidarity (+1 for each other mood with a 2 in its top right corner),
   Modesty, Malevolence, Vindication and Nosiness all print 2, and Vindication grows with round wins. That is the white numbers
   axis behaving as designed in an unplanned deck.
9. **Both decks were low in value (average printed value about 1.7).** User 8: Temperance 3, Modesty 2, Solidarity 2, Desperation 3,
   Malevolence 2, Longing 3, Nosiness 2, Haunting 0, Rashness 0, Gratitude 0, Vindication 2, Wistfulness 1. User 1: Unity 3, Jealousy
   0, Zeal 3, Volatility 2, Verve 1, Whimsy 2, Righteousness 3, Intuition 1, Martyrdom 1, Grudge 0, Levelheadedness 1, Exuberance 3.
   A 12-card deck with one or two plays a round reaches about 10 to 12 points by round 4 or 5; the exception is game 490's
   Haunting turn (17 in round 2).
10. **Round scores in game 499 were close** (2 to 1, 5 to 5, 5 to 8, 10 to 10, 12 to 10), a good sign for a draft game; game 490 was
    decided by the Haunting turn.

### Questions for the testers

- Was blue left alone because of the cards in that pool, or because it felt weak? Same for green's conditional 3-to-6 cards.
- Why were the gates passed: color, or the 5 not worth a pick?
- Game 499: why did user 8 discard Haunting to Longing?
- Did either deck feel too low in value at 12 cards, or the draft too short?
- Fun and clarity, especially for Haunting and Malevolence.

## Session 1e: E1b Free-play cycle with bodies against B Baseline (3 games)

**Source.** The simulator exports of games 512, 514 and 515 (7 November; game 513 was not in the export). E1b is the E1 rebuild with four
3-value bodies (Joy, Compulsion, Temperance, Reminiscence) in place of Adrenaline, Resilience, Reinvigoration and Wistfulness.
The first tester (P1) played E1b in 512 and 515 and B in 514. The other seat was a practice bot (B) in 512 and 515, and the second
tester (E1b) in 514. The Haunting in these games is the new version (value 0, plays kept only while you still have it).

### Summary

| | |
|---|---|
| Result | **E1b won 1 of 3** (515). B won 512 (3 to 2 in rounds, against P1's E1b) and 514 (3 to 1, B played by P1). E1 had lost 0 to 6 to B. |
| Rounds | E1b won 6 of 13 rounds (512: rounds 2 and 3; 514: round 2; 515: rounds 2, 3 and 4). E1 had won 1 of 19. |
| Scores by round, E1b | 512: 3, 8, 10, 7, 7. 514: 3, 6, 6, 11. 515: 0, 22, 14, 9. |
| Scores by round, B | 512: 3, 6, 9, 10, 13. 514: 3, 4, 13, 13. 515: 6, 6, 7, 8. |
| Biggest turn | **6 plays scoring 22** (game 515 round 2, after a Haunting turn). |

### Insights

1. **The bodies worked: E1b is now competitive.** It won 6 of 13 rounds (E1: 1 of 19) and its round 2 scores were 8, 6 and 22 against
   E1's 2 to 4. It still lost two of three games, so it is not yet a deck that beats B on average, but it has the burst turns E1
   never had. This is what the E1b change was for.
2. **Haunting at 0 still produces a game-winning turn.** In game 515 P1 played Haunting first (0 points, lost round 1 by 0 to 6),
   discarded Compulsion, Familiarity and Affinity, and kept Haunting to the next turn. In round 2 it replayed those three from the
   pile and added Reverence (5), Resolve (3 or 6, here 6) and Contentment (5): six plays, **22 points against 6**, and the lead held
   (14 to 7, then 9 to 8). So the nerf did not remove the burst; what it adds is a round of risk (the 0 and the removal window). B's
   bot did not remove Haunting or take the pile (its Reminiscence in round 2 did neither). Compare E1 and E2: there the pile was taken
   (game 511) or the burst was small. Haunting is strongest in a deck with real bodies and weakest when the opponent has pile plays.
3. **Compulsion was the best new card.** It took Zeal in game 514 and Resolve in game 515 from B, and E1b played both. In round 2
   of game 515 the stolen Resolve was a 6 (E1b trailed in round wins) and Compulsion was itself played from the pile by Haunting's banked
   plays. A 3-value body that takes a card, played from the pile, is the deck's card advantage.
4. **Contentment (5) fits E1b through Joy.** Joy (green) gave Contentment its color in all three games, and Contentment was played in each
   (512 round 2, 514 rounds 2 and 4, 515 round 2). The other gates were less lucky: Impatience (no red mood) sat in hand at the end of
   game 512 and Reverence (no white mood) in game 514. This is the same finding as before: the gate is as good as its enabler.
5. **B's tempo removal is its real strength.** Pacifism (game 512 round 4) appears to have suppressed Contentment and cost E1b 5 points (E1b scored 7 in a round where its board was
   worth 12),
   Panic bounced Reverence (515 round 4), and Indignation removed Reminiscence (514 round 3, where B scored 13, apparently with Determination at 6 because three red moods
   were in play). In game 515 E1b's board fell from 22 to 14 to 9 as Pacifism and Panic came down, and it won round 4 by a single point.
   The baseline's cheap interaction is what keeps a big board in check.
6. **Overconfidence did not decide anything here.** It was played once (game 512 round 4) and the extra plays were not used, so no
   penalty applied (the turn shows no restriction). E1b then passed in round 5 holding Nostalgia and Impatience.

### Questions for the testers

- Game 512 round 5: E1b passed holding Nostalgia (and Impatience with no red mood). Was that a choice? The turn had no restriction.
- Game 514: E1b finished with Familiarity, Reminiscence, Reverence and Reverie in hand. Was Reverence stuck (no white mood), and why
  were the others not played?
- Game 515: B's bot did not use Reminiscence on the pile with E1b's three discards in it. Would a human have?
- Fun and clarity for Haunting, Compulsion and Joy.

### Game logs

**Game 512.** E1b (P1, seat 0) against B (bot, seat 1); B went first. B won 3 to 2 in rounds.
- Scores: 3 to 3, 8 to 6 (E1b), 10 to 9 (E1b), 7 to 10, 7 to 13.
- Longest turn: 4 plays (E1b round 2: Contentment, Levity, Fear, Joy).
- Decided: B's Pacifism in round 4, then E1b passing in round 5.

**Game 514.** B (P1, seat 0) against E1b (second tester, seat 1); B went first. B won 3 to 1.
- Scores: 3 to 3, 4 to 6 (E1b), 13 to 6, 13 to 11.
- Longest turn: 2 plays (B rounds 2 and 3; E1b round 4).
- Decided: round 3 (Determination at 6, Indignation removing Reminiscence).
- Hands: E1b finished with 4 cards unplayed.

**Game 515.** E1b (P1, seat 0) against B (bot, seat 1); E1b went first. E1b won 3 to 1.
- Scores: 0 to 6, 22 to 6 (E1b), 14 to 7 (E1b), 9 to 8 (E1b).
- Longest turn: 6 plays (E1b round 2, 22 points).
- Decided: round 2.

### Notes by card (E1b against B)

| Card | What the games showed |
|---|---|
| Haunting | Value 0 in round 1 (lost 0 to 6), then 3 plays from the pile in a 6-play, 22-point turn (515). |
| Compulsion | Took Zeal (514) and Resolve (515, played for 6); played from the pile by Haunting's plays. |
| Joy | Gave Contentment its green mood in all three games; replayed after Fear's bounce (512). |
| Contentment | Played in every game; the one gate that was reliably live. |
| Reverence, Impatience | Stuck in hand without a white or red mood (514, 512). |
| Fear, Levity | Part of the four-play turn in 512 (Levity cycled itself for Nostalgia). |
| Reminiscence | Removed by Indignation (514); returned by Nostalgia and replayed. |
| Overconfidence | Played once, extras unused, no penalty (512). |

## Session 1f: E1b mirror (3 games)

**Source.** The simulator exports of games 516, 517 and 518 (7 to 8 November): both seats on the E1b list (the E1 rebuild with bodies). The first
tester (P1) was seat 0 in all three; the other seat was a practice bot in 516 and 517 and the second tester in 518. The Haunting is the new
version (value 0, plays kept only while you still have it), though it did not come up.

### Summary

| | |
|---|---|
| Result | P1 won 516 (3 to 1 in rounds) and 518 (3 to 0); the bot won 517 (3 to 2). |
| Margins | Close: 516 ended 16 to 15, 517 14 to 17 and 518 12 to 10 in the last round. |
| Scores by round, seat 0 | 516: 3, 8, 13, 16. 517: 3, 11, 12, 12, 14. 518: 9, 9, 12. |
| Scores by round, seat 1 | 516: 5, 7, 10, 15. 517: 5, 7, 12, 17, 17. 518: 2, 7, 10. |
| Biggest turn | 4 plays (game 518 round 1: Overconfidence, Detachment, Levity, Familiarity), scoring 9 against 2. |

### Insights

1. **The mirror is close and the gates decide it.** The 5-point gates were the biggest scoring plays in the decisive rounds: Detachment
   in 518 (5 of the first player's 9 in round 1), Impatience in 516 round 3 (13 to 10), Contentment in 517 round 2 (11 to 7), and in 517 the bot's
   Reverence and Detachment (10 of its 17 points in round 4). In E1b the free-play cards supply every color, so the gates are nearly
   always live, and they are the deck's real scoring. Together with sessions 1d and 1e this is the clearest pattern so far:
   wherever a deck can enable its gates, the gates win close rounds. If win rates later say they are too strong, 4 is the
   fallback.
2. **Two of the gates are hard to enable in E1b.** Resentment (black) and Impatience (red) each have only two enablers in the deck
   (Remorse and Haunting; Rashness and Compulsion). They sat in hand at the end of game 517 (Impatience) and game 518 (two Resentments,
   one of them taken by Compulsion) and were played in 516. White has five enablers and blue four. If E1b is retuned,
   Temperance (white, never seen in these games) could give way to a red or black 3-value body.
3. **Compulsion takes the victim's worst card.** The target chooses what to give, so it handed over an unplayable Resentment in game
   518 and cost the victim little. In 516 both players played Compulsion in round 1 and each took a card from the other. It is a fair
   3-value body with a small bonus; in session 1e it looked better because it was played from the pile and took a card that
   fit.
4. **Overconfidence's trade worked.** In 518 round 1 it gave four plays and 9 points against 2; the forced pass in round 2 still won
   9 to 7, because the board did the scoring. The penalty hurts most when the board is small.
5. **A burst of 0 and 1 value plays does not score.** In 517 round 4 P1 played Rashness and Remorse (value 0 each) and its score
   stayed at 12, while the bot's single Detachment took it from 12 to 17. Extra plays only help if the cards in hand have value.
6. **Reverie was a body here (2), not an engine,** in all three games: no draw from its trigger appears in the logs, probably because
   the hands had no chain to trigger it.

### Questions for the testers

- Game 518: was the Overconfidence line in round 1 a close decision?
- Do the red and black gates (Impatience, Resentment) feel stuck in E1b, as the logs suggest?
- Fun and clarity for the free-play chains and Compulsion.

### Game logs

**Game 516.** E1b (P1, seat 0) against E1b (bot, seat 1); P1 went first. P1 won 3 to 1.
- Scores: 3 to 5, 8 to 7, 13 to 10, 16 to 15.
- Longest turn: 2 plays (several).
- Decided: Impatience (5) in round 3, then a one-point final round.

**Game 517.** E1b (P1, seat 0) against E1b (bot, seat 1); P1 went first. The bot won 3 to 2.
- Scores: 3 to 5, 11 to 7, 12 to 12, 12 to 17, 14 to 17.
- Decided: the bot's Reverence and Detachment in rounds 3 and 4; P1's round 4 plays (Rashness, Remorse) added nothing.

**Game 518.** E1b (P1, seat 0) against E1b (second tester, seat 1); P1 went first. P1 won 3 to 0.
- Scores: 9 to 2, 9 to 7, 12 to 10.
- Longest turn: 4 plays (round 1, 9 points).
- Hands: the second tester finished with Affinity, Fear and two Resentments in hand.

### Notes by card (E1b mirror)

| Card | What the games showed |
|---|---|
| Detachment, Reverence, Contentment, Impatience, Resentment | Detachment, Reverence, Contentment and Impatience were the big plays; Resentment and Impatience also sat stuck in hand. |
| Overconfidence | Four plays, 9 points, and a forced pass that still won the round (518). |
| Compulsion | Both players used it in 516; it handed over a dead Resentment in 518. |
| Joy | Gave Contentment its color (517) and was an extra play for Joy after Levity's draw (518). |
| Reverie | A 2-point body in all three games. |
| Rashness, Remorse | Two zeros that added nothing to a 12-point board (517 round 4). |
| Temperance | Not seen. |

## Session 2a: G Green anthems against B Baseline (4 games)

**Source.** The simulator exports of games 519 to 522 (8 November). The first tester (P1) played B in 519 and 521 and G in 520 and 522. The other
seat was a practice bot (G) in 519 and the second tester in the other three games (B in 520 and 522, G in 521). G is the mono-green anthem
deck (Fulfillment, Vitality, Maturity, Kinship, Vindication, Perseverance, Urgency and the 3-to-6 cards).

### Summary

| | |
|---|---|
| Result | The games split 2 to 2: B won 519 (3 to 2 in rounds, against the bot on G) and 520 (3 to 0); G won 521 (3 to 2) and 522 (3 to 1). |
| Scores by round, G | 519: 6, 6, 3, 9, 9. 520: 2, 2, 2. 521: 3, 6, 9, 18, 18. 522: 2, 9, 11, 16. |
| Scores by round, B | 519: 3, 3, 6, 9, 11. 520: 3, 6, 6. 521: 3, 6, 12, 18, 16. 522: 6, 8, 10, 16. |
| Plays | Almost every turn was a single play for both decks. G made two plays in a turn twice (519 round 4, 521 round 3). |

### Insights

1. **G is a slow, board-dependent deck, and B's cheap tempo cards keep a one-mood board in check.** In game 520 G scored 2, 2 and 2: B's
   Panic bounced its only mood, Hate put it on the bottom of the deck, and each round G was back to one mood. G finished that game
   with five cards in hand (Carelessness, Determination, Gratitude, Nostalgia, Possessiveness), all of them conditionals that need a
   board or a pile to do anything. Honesty (6 on turn one) carried G to 6 to 3 in rounds 1 and 2 of game 519, but Hate (on Vindication), Vengeance
   (on Honesty) and Shock (on Joy) took the board apart from round 2.
2. **Maturity is strong when it comes down early.** In game 522 round 1 it was a 2, then 4, 6 and 8 (scores 2, 9, 11, 16 with Contentment
   and Determination). B's Shock (a value of 3 or less) could not reach it once it passed 3, and it took Perseverance instead. In game 520
   it came down in round 3, after B had already won two rounds. A Maturity played in round 1 is a 6 in round 3 and an 8 in round 4. The notes' worry that opponents may not have time to remove it holds: B had no answer in time.
3. **Contentment (5) was again the key play in a one-color deck.** G played it in game 522 round 2 (9 to 8), and B's own Largesse gave G the card
   that round. This repeats the gate pattern from sessions 1d to 1f.
4. **Fulfillment and Vitality did not appear.** Fulfillment was milled by Carelessness in game 519 round 5 (with Perseverance) and never
   played, and Vitality was not drawn. The anthem payoffs are untested; this session shows the deck's early game instead.
5. **Hand attacks hit again.** B's Compulsion (519, 521 and 522) and Suspicion (519 and 521) each took a card from a small green
   hand. In 519 Suspicion made G discard Honesty in round 4 and Nostalgia returned it; in 521 Suspicion made G discard in round 2 and Nostalgia
   returned Joy in round 3.
6. **The games were close when G's board survived.** Game 521 went to round 5 (G 18 to 16 on Honesty after B's Pacifism), and game 522 was
   decided by one point in each of rounds 2 and 3.

### Questions for the testers

- Game 520: G played one mood a round and finished with Nostalgia (a free extra play) and four other cards in hand. Was playing it first
  considered, and did the single play per round feel forced?
- Game 522: B's Shock took Perseverance, not Maturity. Was Maturity out of reach by then, and what is the right answer to it?
- Game 519: was Carelessness a choice with Fulfillment in the deck (it can mill the mythic)?
- Fun and clarity for the anthems and Maturity's growth.

### Game logs

**Game 519.** B (P1, seat 0) against G (bot, seat 1); G went first. B won 3 to 2.
- Scores: B 3, G 6; B 3, G 6; B 6, G 3; B 9, G 9; B 11, G 9.
- Decided: Hate and Vengeance on G's early moods, then Shock on Joy in round 5.

**Game 520.** G (P1, seat 0) against B (second tester, seat 1); B went first. B won 3 to 0.
- Scores: G 2, B 3; G 2, B 6; G 2, B 6.
- Decided: Panic and Hate kept G at one mood; G held five cards at the end.

**Game 521.** B (P1, seat 0) against G (second tester, seat 1); G went first. G won 3 to 2.
- Scores: B 3, G 3; B 6, G 6; B 12, G 9; B 18, G 18; B 16, G 18.
- Longest turn: 2 plays (G round 3: Nostalgia and Joy).
- Decided: Honesty in round 5 after B's Pacifism.

**Game 522.** G (P1, seat 0) against B (second tester, seat 1); G went first. G won 3 to 1.
- Scores: G 2, B 6; G 9, B 8; G 11, B 10; G 16, B 16.
- Decided: Maturity (2, 4, 6, 8) with Contentment and Determination.

### Notes by card (G against B)

| Card | What the games showed |
|---|---|
| Maturity | 2, 4, 6, 8 in game 522 (out of Shock's reach by round 3); played too late in game 520. |
| Honesty | 6 on turn one (519); replayed from the pile after a Suspicion discard (519 round 4); a 6 again in 521 round 5. |
| Contentment | A free 5 in a mono-green deck (522). |
| Vindication, Perseverance | Bounced or bottomed by B's cheap tempo cards before they grew. |
| Carelessness | Milled Fulfillment and Perseverance (519); used as fuel in 521. |
| Fulfillment, Vitality | Not played (milled, and not drawn). |
| Possessiveness, Gratitude, Determination, Nostalgia | Sat in hand in game 520 with no board to support them. |

## Session 2b: R Red pile against B Baseline (4 games)

**Source.** The simulator exports of games 523 to 526 (8 November). The first tester (P1) played B in 523 and 525 and R in 524 and 526. The other seat
was a practice bot (R) in 523 and the second tester in the other three games (B in 524 and 526, R in 525). The tester reports that the bot played
FOMO badly in game 523 (it kept paying for a suppressed FOMO), that this was then fixed, and that FOMO did not come up in games 524 to 526.
R is the mono-red deck (Ardor, Verve, Dominance, Exuberance, Adrenaline, Frenzy, FOMO, Covetousness, Competitiveness and the removal).

### Summary

| | |
|---|---|
| Result | **B won 3 of 4** (523, 524, 525, each 3 to 1 in rounds); R won game 526 (3 to 1). |
| Scores by round, R | 523: 0, 6, 0, 3. 524: 0, 9, 5, 13. 525: 4, 4, 6, 7. 526: 4, 1, 10, 27. |
| Scores by round, B | 523: 1, 4, 7, 10. 524: 5, 8, 11, 13. 525: 3, 6, 12, 12. 526: 3, 7, 9, 13. |
| Game length | 4 rounds in every game. |
| Biggest turn | **27 points in one round** (game 526 round 4, Ardor with four red moods). |

### Insights

1. **R is slow to start and spikes late.** Its first three rounds scored 0 to 10 (average about 4), and B's removal answered its key cards in each
   game. The one win came from Ardor: in game 526 round 4, with Ardor, Competitiveness, Hellbent and Whimsy in play (four red moods), every red
   mood got +4, and R scored 27 against 13. That is the card doing what the checklist feared, and it needs a four-mood red board,
   which only one of the four games reached. Before that R had scored 4, 1 and 10.
2. **B's cheap interaction answers the red mythics.** Competitiveness (printed 0, and worth 1 more than B's biggest mood) was bounced by
   Panic (game 526 round 2: R 1 against 7) and removed by Vengeance (game 524 round 3: R 5 against 11). Rancor was bottomed by Hate
   (525 round 4). The baseline's removal-heavy deck is the real test of the red build-arounds, and in three of four games it won.
3. **Belligerence and Rashness often had no targets.** B's moods are mostly 3s, so Belligerence (value 2 or less) did nothing in games
   524 round 3 and 525 round 1, and Rashness found a target only in game 525 round 4 (B's Hate). Against decks of 0 to 2 value moods
   (E1, E2) they are real; against B they are blanks. This repeats the session 1 note about Rashness.
4. **Adrenaline worked.** In game 524 it gave R two plays in rounds 2 to 4 (Competitiveness then Ruthlessness, Covetousness then
   Belligerence, Frenzy then Impatience). The chain of red moods is the engine behind Ardor's four-mood board.
5. **FOMO was a trap for the bot, which was the tester's point.** In game 523 R played FOMO in round 1 (discarding Competitiveness as the
   cost), B's Pacifism suppressed it at once (R scored 0), and the bot kept paying: it discarded two more cards in rounds 2 and 3 (Ardor
   and Verve ended in the pile with Competitiveness) before putting FOMO into the discard pile in round 4. So the bot threw away three cards for a value-0
   mood. Suppressed moods keep their abilities, so Pacifism
   on FOMO turns a 7 into a pure cost, and a player should drop it immediately. FOMO's value-7 play is untested.
6. **Frenzy and Impatience gave R a 13 in game 524 round 4** (Frenzy 6 and Impatience 5 with Adrenaline, Belligerence and Covetousness), against B's 13;
   the gate again was a key scoring play.

### Questions for the testers

- Game 526 round 4: was Ardor held for a four-mood board, or did it come together?
- Fun and clarity for Adrenaline's chains and Ardor.

### Game logs

**Game 523.** B (P1, seat 0) against R (bot, seat 1); R went first. B won 3 to 1.
- Scores: B 1, R 0; B 4, R 6; B 7, R 0; B 10, R 3.
- Decided: Pacifism on FOMO, then Hate and Reminiscence in round 3.

**Game 524.** R (P1, seat 0) against B (second tester, seat 1); R went first. B won 3 to 1.
- Scores: R 0, B 5; R 9, B 8; R 5, B 11; R 13, B 13.
- Longest turn: 2 plays (R in rounds 2, 3 and 4, from Adrenaline).
- Decided: Vengeance and Shock on R's best moods.

**Game 525.** B (P1, seat 0) against R (second tester, seat 1); R went first. B won 3 to 1.
- Scores: B 3, R 4; B 6, R 4; B 12, R 6; B 12, R 7.
- Decided: Vengeance, then Hate on Rancor.

**Game 526.** R (P1, seat 0) against B (second tester, seat 1); B went first. R won 3 to 1.
- Scores: R 4, B 3; R 1, B 7; R 10, B 9; R 27, B 13.
- Decided: round 4, Ardor with four red moods.

### Notes by card (R against B)

| Card | What the games showed |
|---|---|
| Ardor | +4 on each of four red moods: 27 points (526 round 4). |
| Competitiveness | Bounced by Panic (526) and removed by Vengeance (524); good when it stays. |
| Adrenaline | Two plays a turn in game 524 rounds 2 to 4. |
| FOMO | Suppressed at once by Pacifism; the bot paid three cards (523). |
| Belligerence, Rashness | Often no targets against B's 3-value moods. |
| Frenzy, Impatience | 6 and 5: the biggest plays of game 524 round 4. |
| Hellbent | A 2 with cards in hand (526), part of the four-red-mood board. |

## Session 2c: W White numbers against B Baseline (6 games)

**Source.** The simulator exports of games 527 to 532 (8 November). The first tester (P1) played B in 527, 529 and 531 and W in 528, 530 and 532. The
other seat was a practice bot (W) in 527 and the second tester in the other five games (B in 528, 530 and 532, W in 529 and 531). W is the white
numbers deck (Levelheadedness, Rudeness, Orderliness, Affinity, Familiarity, Modesty, Confidence, Humility, Equanimity and the rest) with Grudge and
Elusiveness in place of Solace and Vigilance, so this is the first session where both replacement effects were in the deck.

### Summary

| | |
|---|---|
| Result | **B won all 6 games and 18 of the 27 rounds.** Round scores in the games: 3 to 2 (527, 529, 530, 531), 3 to 0 (528), 3 to 1 (532). W won 9 rounds. |
| Scores by round, W | 527: 7, 4, 8, 11, 6. 528: 0, 1, 5. 529: 5, 5, 8, 8, 10. 530: 2, 2, 7, 5, 5. 531: 1, 1, 4, 4, 8. 532: 1, 5, 10, 14. Average 5.4 a round. |
| Scores by round, B | 527: 3, 8, 8, 8, 9. 528: 3, 6, 8. 529: 3, 4, 10, 12, 12. 530: 1, 7, 4, 7, 10. 531: 0, 1, 7, 10, 13. 532: 6, 6, 9, 15. Average 7.0 a round. |
| Game length | 3 to 5 rounds, 4.5 on average (four games went to five rounds). |
| Biggest turn | **3 plays** (game 530 round 3: Modesty, Pacifism, then Compassion from Grudge; 7 to 4, a round win). Highest W score: 14 (532 round 4, lost to a 15). |

### Insights

1. **W ran out of cards.** Its extra-play cards (Modesty, Confidence, Familiarity, Affinity, Grudge) spend the hand faster than one card a round for the
   loser can refill it. W had played its last card by round 4 or 5 in four of the five long games (527 rounds 4 and 5, 530 rounds 4 and 5, 531
   round 5, 529 round 5 with Largesse) while B kept 2 to 4 cards in hand at the end of every game. The clearest cost is Grudge: of the 11 extra plays it
   granted over the six games (including the turn it was played), W used 4. All 7 unused ones came with an empty hand (527 rounds 4 and 5, 530 rounds
   4 and 5, 531 round 5). So the engine had no fuel at the point it was strongest. This is the same lesson as E1 (the free-play engine needs bodies), and
   here W lacks card flow (Discernment is its only loot and was never played).
2. **W won early and lost late.** W won round 1 in four of six games (and round 2 in two of those), but won none of the four fifth rounds. In games 529 and 531 it led 2 to 0 and then lost three rounds in a row.
   B's comeback cards helped: Resolve is a 6 for a player behind in rounds (529 round 3: B scored 10 with it), and Determination is a 6 once three moods
   share a color.
3. **A mono-white board switches on B's Determination.** In every round where Determination was in play and not suppressed it was a 6 (530 round 2,
   531 rounds 3 to 5, 532 round 4: five rounds). In 530 W's own Pacifism suppressed it from round 3 on, which is why B scored 7 and 10 there. B has white
   cards of its own (Pacifism, Temperance), but W's board supplies the other two. This is a deck-building effect, not a flaw in W, but it explains part of B's edge.
4. **Reverence was the target of B's Pacifism every time.** Reverence (5) was suppressed in 527 round 5, 530 round 1 and 531 round 2, the only games where it was
   played. In 530 round 1 that turned a 7 into a 2 (W still won 2 to 1, Pacifism being a 1). The five-point gates continue to be the highest-value mood on a W board and
   the natural suppression target; in 527 round 4 it did score its 5 (11 against 8, a round win).
5. **Grudge works as written, and is a comeback card.** It gave extra plays the turn it was played (527 round 4, 531 rounds 4 and 5), counted the
   chosen player's round wins correctly (0 extras on 528 round 1 and 530 round 2, when B had no wins), and was put on the bottom of the deck when Vengeance
   would have discarded it (528 round 2: its owner had no other mood, so Vengeance had to pick it). Two Grudge turns won a round (527 round 4,
   530 round 3). Played on turn 1 or 2 it is a 0-point mood that gives nothing (528 round 1: 0 against 3; 530 round 2: 2 against 7), so it is only good late, which is when the hand
   is empty (see 1). The card is fine; the problem is the number of cards left to play with it.
6. **Elusiveness did its job once and covers only half of B's removal.** In 528 round 3 Shock put it into W's hand instead of the discard pile, as
   written. It does nothing against B's Pacifism, Panic, Hate or Distrust (suppress, hand and bottom of the deck), so it applies to Vengeance, Shock,
   Disdain and Indignation only. As a turn-1 play it is a 1 (532 round 1: 1 against 6). The replacement ordering with Grudge was not tested: the two never
   shared a board (in 528 Grudge was gone before Elusiveness was played).
7. **Modesty was reliable; Confidence was not.** Modesty gave an extra play in all three games it was played (527 round 1, 529 round 1, 530 round 3) and W won all
   three rounds. Confidence's extra play needs a 4 to 6 card, and the deck has two (Reverence, Largesse), so it was used once in three plays (530
   round 1, for Reverence) and twice passed with the grant unused (527 round 2, 529 round 4). Familiarity (527 round 3) and Affinity (531 round 5, a grant with no card left to use it) worked.
8. **Orderliness was the strongest numbers card, and the bot misplayed it.** In 532 it added +3 on round 4 (Elusiveness, Equanimity and Humility each +1) and, with Humility,
   made 10 and 14. In 527 round 3 the bot chose "odd" with Modesty, Confidence and Familiarity (all 2) in play; "even" would have made
   11 instead of 8 and a win over B's 8. The log shows the choice came from the bot's generic resolver, not an evaluation. Orderliness (even) also undoes Reassurance: it raises a 2 to 3, and Reassurance only
   protects moods with a value of 2 or less (529 round 2: B's Pacifism chose Reassurance, which was then a 3).
9. **Levelheadedness and Rudeness are still untested.** Rudeness was never drawn in six games (it stayed in the deck every time). Levelheadedness was drawn in three games
   and never played: it was discarded to Suspicion in 532 round 2 (a choice) and in 530 round 5 (the only card in hand), and it sat in the hand when game 528 ended. Fairness, Solidarity and Discernment were also not played (Discernment was given away to Compulsion in 529 round 1). The two swing cards need a game built to
   draw them, for example a shorter list or stacked hands.
10. **Compassion moved the first turn once and did not change a result.** In 530 round 3 W won, but with six moods against B's three it lost first player
    to B in round 4 (the override is recorded in the log). It gives the first turn to the smaller board, which is the opposite of what an
    extra-play deck wants. In 529 it never changed the order.
11. **W's printed values are low.** The deck averages 2.05 a card (E1b 2.3, B about 2.65), so it needs Orderliness and Humility boosts to compete: it scored 5.4 a round
    against B's 7.0. When both boosts were in play (532 rounds 3 and 4) W scored 10 and 14, so the build-around works but needs a board of three or four moods.

### Questions for the testers

- Game 528 round 1 (Grudge) and game 532 round 1 (Elusiveness): were these deliberate tests of the card on turn 1, or the best opening you had?
- Game 532 round 2: why was Levelheadedness the card to discard to Suspicion? How does it read in hand, and in games 528 and 532 was there a round where you wanted to play it
  (every mood scores 2, so it favors the player with more moods)?
- Does Grudge feel too slow because of the empty hand, or too weak because it is a 0? What would make the late turn worth it (fewer cards, a loot, a different count)?
- Confidence: is "a 4, 5 or 6 in its top right corner" understood? The deck has only two such cards; would you want more of them in W?
- Orderliness: did the odd/even choice read clearly (printed number against current value)? Did Reassurance and Orderliness feel like they work against each other?
- Fun and clarity for Grudge and Elusiveness, and for the W deck as a whole.

### Game logs

**Game 527.** B (P1, seat 0) against W (bot, seat 1); B went first. B won 3 to 2.
- Scores: B 3, W 7; B 8, W 4; B 8, W 8; B 8, W 11; B 9, W 6.
- Longest turn: 2 plays (W in rounds 1, 3 and 4: Modesty then Temperance, Familiarity then Orderliness, Grudge then Reverence).
- Hands: W had an empty hand from round 4 (one Grudge play unused in round 4, two in round 5).
- Decided: round 3 (the bot chose "odd" for Orderliness; "even" would have scored 11 against B's 8) and round 5 (Pacifism on Reverence).

**Game 528.** W (P1, seat 0) against B (second tester, seat 1); W went first. B won 3 to 0.
- Scores: W 0, B 3; W 1, B 6; W 5, B 8.
- Decided: Grudge as a first play (0 points), Vengeance sending it to the bottom of the deck, Shock returning Elusiveness to the hand.

**Game 529.** B (P1, seat 0) against W (second tester, seat 1); W went first. B won 3 to 2.
- Scores: B 3, W 5; B 4, W 5; B 10, W 8; B 12, W 8; B 12, W 10.
- Longest turn: 2 plays (W in round 1: Modesty then Orderliness).
- Decided: Resolve as a 6 for B in round 3, Shock on Modesty, Indignation on Compassion in round 5 (12 against 10).

**Game 530.** W (P1, seat 0) against B (second tester, seat 1); W went first. B won 3 to 2.
- Scores: W 2, B 1; W 2, B 7; W 7, B 4; W 5, B 7; W 5, B 10.
- Longest turn: 3 plays (W in round 3: Modesty, Pacifism, Compassion).
- Hands: W had an empty hand in rounds 4 and 5 (one Grudge play unused in round 4, two in round 5).
- Decided: Determination as a 6 in round 2 (W's Pacifism suppressed it from round 3); Vengeance on Compassion and Suspicion on the last card in hand.

**Game 531.** B (P1, seat 0) against W (second tester, seat 1); B went first. B won 3 to 2.
- Scores: B 0, W 1; B 1, W 1; B 7, W 4; B 10, W 4; B 13, W 8.
- Longest turn: 2 plays (W in rounds 4 and 5, from Grudge; one of the two Grudge plays was unused in round 5).
- Decided: W's Pacifism on Temperance in round 1; Determination as a 6 for B from round 3; W's empty hand in round 5.

**Game 532.** W (P1, seat 0) against B (second tester, seat 1); W went first. B won 3 to 1.
- Scores: W 1, B 6; W 5, B 6; W 10, B 9; W 14, B 15.
- Longest turn: 1 play every turn.
- Decided: round 4 by one point (14 against 15, Determination as a 6).

### Notes by card (W against B)

| Card | What the games showed |
|---|---|
| Grudge | Extra plays as written (4 used of 11 granted; the rest wasted with an empty hand). Bottom-of-deck replacement worked (528). 0 points on turn 1. |
| Elusiveness | Returned to hand by Shock (528). Does not cover Pacifism, Panic, Hate, Distrust. 1 point as a first play (532). |
| Levelheadedness | Not played (discarded twice, held once). |
| Rudeness | Never drawn. |
| Modesty | Extra play in 3 of 3 games; all three rounds won. |
| Confidence | 1 of 3 plays used the extra play (two had no 4 to 6 card). |
| Familiarity, Affinity | Worked (527 round 3; 531 round 5, no card left). |
| Orderliness | +3 (532); bot chose "odd" with all 2s (527 round 3). With Reassurance: raises 2 to 3. |
| Humility | +1 on 0 to 2 moods (532 rounds 2 to 4). |
| Equanimity | Never a 6 (needs four even moods); 3 points in 531 and 532. |
| Reverence | 5 once (527 round 4); suppressed by Pacifism in the other three plays. |
| Reassurance | Chosen by Pacifism when Orderliness (even) made it a 3 (529). |
| Compassion | Flipped the first player once (530 round 4); no effect on a result. |
| Temperance | 5 points in 527 round 1 (W had fewer cards in hand); discarded by Disdain. |
| Largesse | 5 points twice (528, 529); gives B a card. |
| Fairness, Solidarity, Discernment | Not played. |

## Session 2d: G Green anthems against R Red pile (6 games)

**Source.** The simulator exports of games 533 to 537 and 539 (8 November; game 538 is not in the zip). The first tester (P1) played R in 533, 535 and 537 and G in 534, 536
and 539. The other seat was a practice bot (G) in 533 and the second tester in the other five games (G in 535 and 537, R in 534, 536 and 539). G is the
mono-green anthem deck (Fulfillment, Vitality, Maturity, Vindication, Kinship, Honesty, Determination, Resolve, Restlessness, Urgency and the
fuel cards); R is the mono-red pile (Ardor, Dominance, Verve, Exuberance, Rashness, Frenzy, Shock and the rest).

### Summary

| | |
|---|---|
| Result | **R won 4 of 6** (534, 535 and 537 by 3 to 2 in rounds, 536 by 3 to 0); G won 533 (3 to 0, against P1's R, G played by the bot) and 539 (3 to 1). Rounds: R 13, G 12. |
| Scores by round, G | 533: 6, 9, 15. 534: 3, 15, 18, 18, 40. 535: 3, 9, 11, 21, 24. 536: 3, 9, 11. 537: 6, 6, 6, 9, 9. 539: 2, 8, 12, 20. |
| Scores by round, R | 533: 3, 7, 12. 534: 3, 10, 19, 28, 40. 535: 3, 6, 13, 18, 35. 536: 4, 12, 22. 537: 2, 5, 11, 13, 15. 539: 6, 3, 7, 15. |
| Game length | 3 to 5 rounds, 4.2 on average (three games went to five rounds). |
| Biggest turn | 2 plays (R in 533 round 2, 535 round 3 and 536 round 1; G in 534 round 2 and 536 round 2). **Highest scores so far: 40 for both decks in game 534 round 5**, 35 for R in 535 round 5. |

### Insights

1. **Both decks scale, and the games are decided in rounds 3 to 5.** Round 1 scored 2 to 6 for both sides in every game. By round 5 the long games scored 24 to 40 (534: 40 to 40; 535: 24 to 35), against 9 to 15 in game 537, where R stripped G's board. Earlier sessions topped out at 27. Scaling against scaling
   made the largest totals so far. The rounds split 13 to 12, but R won 4 of the 6 games.
2. **R's engine is Ardor plus cheap red moods.** Ardor was in play in four games (534 round 3, 535 round 5, 536 round 1, 539 round 3) and R won three of them. Three red moods gave 19 (534 round 3), four gave 22 (536 round 3) and 28 (534 round 4), and five gave 40 (534 round 5; Competitiveness, Shock and Verve filled the board). In game 535 round 5 Ardor with four red moods made 35, and
   Ardor had been drawn on the round 4 loss: one card swung the game (18 against 21 became 35 against 24). Rashness gave a free play in 535 round 3 (Kinship) and 536 round 1 (Ardor on turn 1: 4 to 3), the first real use of the free-play chain in a game.
3. **G's engine is Fulfillment plus the 3-to-6 cards, and the 6s come easily.** In 534 round 5 G had Honesty, Determination and Restlessness all at 6 and Fulfillment
   doubled them: 40 points from five moods (+18 from Fulfillment). In 535 Fulfillment added 6 on round 4 (Resolve) and 6 on round 5 (Restlessness). Honesty was a 6 on turn one in 533 and 537 (and in 534 round 2), because every card in hand shared the mood's color, so G won the first round when it opened with it (6 against 3 and 6 against 2). The shared weakness is the same as in session 2a: G's
   moods are exposed at 3 (Shock hits 3 or less) and safe at 6.
4. **R's removal beat G in game 537, and Dominance did the work.** Dominance (the red mythic) removed Kinship (round 2) and Perseverance (round 3) for free when
   Ruthlessness and Exuberance were played, and Shock removed Urgency (round 5). G ended with two moods (Honesty and Restlessness) and scored 6, 6, 6, 9, 9. Shock also removed Joy in 534 round 4 (G 18 against 28). G's
   cheap bodies (Joy 3, Kinship 1, Perseverance 2, Urgency 3) are all in range of Shock and Dominance, as the checklist feared for decks with many small moods.
5. **The fuel package did not work.** Carelessness milled two of G's own cards in both games it was played, and the cards were the wrong ones: Possessiveness and Determination in 535, Urgency and Maturity in 536. Nostalgia got Urgency back in 536 round 2 (a 6 with the extra play), the one case where
   the discard pile helped. Possessiveness (6 with five or more cards in the pile) never reached five cards, and Wastefulness was never played: G gave it away to Compulsion twice (533, 539) and held it at the end of 535, 536 and 537. Carelessness cost a card of its own deck and gave back a 3; it did not feel like fuel.
6. **Vitality and Maturity did not come up.** Neither was played in six games: Vitality sat in the hand at the end of 533 (bot) and 537, and Maturity was milled by Carelessness in 536. Gratitude and Optimism were not played either. G's decks chose cheaper moods that score now.
   Whether the anthems are too slow (a 1 and a 2 that need turns) or just outcompeted by the 3-to-6 cards needs the testers' view.
7. **Compulsion gave R G's best card once.** In 535 round 1 R took Kinship from G's hand (G chose to give it), and played it in round 3 for +3 on three red moods: R 13 against G's 11, a round decided by a card from G's own deck. In 533 and 539 G gave Wastefulness, the weakest card in its hand, so Compulsion costs a G player little unless it
   has nothing to give.
8. **Resolve, Vindication and Urgency worked as comeback and tempo cards.** Resolve was a 6 for the player behind in rounds (535 rounds 2 and 4, 539 round 2). Vindication was a 6 after two round wins (533 round 3, 539 round 4). Urgency needs two plays in a turn, and made a 6 only once (536 round 2, with Nostalgia); alone it was a 3, and Shock took it in 537 round 5.
9. **Frenzy and Hellbent barely mattered.** Frenzy was a 6 on turn one in 539 (6 to 2) and then discarded as written. Hellbent never reached 7 (R held cards in every game it was played). Covetousness was never played (it found nothing at 1 or less to take).

### Questions for the testers

- Game 537: G held Vitality (and Wastefulness) for five rounds. Was Vitality unclear, too slow, or just worse than what else you could play? Same question for Maturity, Gratitude and Optimism.
- Game 539: R held Dominance and Hellbent in the last rounds and played Ardor and Ruthlessness. Why? How did you see Dominance against G?
- Carelessness: did milling two of your own cards feel like a cost or like fuel? Did the Carelessness, Wastefulness and Possessiveness package feel like a plan, and is Possessiveness (five cards in the pile) ever reachable?
- Compulsion: when you chose a card to give (Wastefulness in 533 and 539, Kinship in 535), was it the weakest card in hand? Did Kinship feel like a mistake given R's red board?
- Scores of 20 to 40 appeared for the first time. Does a round of 40 against 40 read as fun and fair, or too swingy?
- Fun and clarity for Ardor, Dominance, Fulfillment, Honesty and the Rashness chain.

### Game logs

**Game 533.** R (P1, seat 0) against G (bot, seat 1); R went first. G won 3 to 0.
- Scores: R 3, G 6; R 7, G 9; R 12, G 15.
- Longest turn: 2 plays (R in round 2: Whimsy, then Hellbent).
- Decided: Honesty as a 6 on turn one, Vindication as a 6 in round 3. The bot played Thrift in round 2 with an empty discard pile and passed the extra play.

**Game 534.** G (P1, seat 0) against R (second tester, seat 1); G went first. R won 3 to 2.
- Scores: G 3, R 3; G 15, R 10; G 18, R 19; G 18, R 28; G 40, R 40.
- Longest turn: 2 plays (G in round 2: Honesty then Determination, from Joy).
- Decided: Ardor in round 3 (19 against 18), Shock on Joy and Ardor with four red moods in round 4 (28), Fulfillment against five red moods in round 5 (40 each).

**Game 535.** R (P1, seat 0) against G (second tester, seat 1); R went first. R won 3 to 2.
- Scores: R 3, G 3; R 6, G 9; R 13, G 11; R 18, G 21; R 35, G 24.
- Longest turn: 2 plays (R in round 3: Rashness, then Kinship).
- Decided: Kinship, taken from G by Compulsion, in round 3; Ardor drawn in round 4 and played in round 5 (35).

**Game 536.** G (P1, seat 0) against R (second tester, seat 1); R went first. R won 3 to 0.
- Scores: G 3, R 4; G 9, R 12; G 11, R 22.
- Longest turn: 2 plays (R in round 1: Rashness then Ardor; G in round 2: Nostalgia then Urgency).
- Decided: Carelessness milling Urgency and Maturity in round 1; R's four red moods in round 3 (22).

**Game 537.** R (P1, seat 0) against G (second tester, seat 1); G went first. R won 3 to 2.
- Scores: R 2, G 6; R 5, G 6; R 11, G 6; R 13, G 9; R 15, G 9.
- Decided: Dominance removing Kinship and Perseverance in rounds 2 and 3, Shock on Urgency in round 5.

**Game 539.** G (P1, seat 0) against R (second tester, seat 1); G went first. G won 3 to 1.
- Scores: G 2, R 6; G 8, R 3; G 12, R 7; G 20, R 15.
- Decided: Resolve as a 6 in round 2, Contentment in round 3, Restlessness as a 6 in round 4 (20).

### Notes by card (G against R)

| Card | What the games showed |
|---|---|
| Fulfillment | +18 in 534 round 5 (three 6s), +6 in 535 rounds 4 and 5. |
| Honesty | A 6 on turn one in 533 and 537 and in 534 round 2. |
| Resolve, Vindication | Comeback 6s (Resolve) and a 6 after two wins (Vindication). |
| Restlessness, Determination | 6 in the big rounds (534 round 5, 539 round 4). |
| Urgency | A 6 once (536 round 2); otherwise a 3 that removal took. |
| Carelessness | Milled Possessiveness and Determination (535) and Urgency and Maturity (536). |
| Possessiveness, Wastefulness | Never worked: five cards in the pile never happened; Wastefulness given away or held. |
| Nostalgia | Took Urgency back (536 round 2). |
| Vitality, Maturity, Gratitude, Optimism | Not played in six games. |
| Ardor | 19 with three red moods, 22 with four, 28 and 40 with five; 35 in 535. |
| Dominance | Removed Kinship and Perseverance for free (537). Held in hand in 539. |
| Rashness | Free play in 535 round 3 and 536 round 1 (Ardor on turn one). |
| Shock | Joy (534 round 4) and Urgency (537 round 5). |
| Compulsion | Took Kinship (535, used by R), Wastefulness twice. |
| Frenzy | A 6 on turn one (539), then discarded as written. |
| Hellbent, Covetousness | Hellbent never 7; Covetousness never played. |

## Session 2e: G Green anthems against W White numbers (3 games)

**Source.** The simulator exports of games 540 to 542 (8 November). The first tester (P1) played W in 540 and 542 and G in 541. The other seat was a practice bot (G) in 540
and the second tester in the other two games (W in 541, G in 542). Both decks are the ones from sessions 2a and 2c (W has Grudge and Elusiveness).

### Summary

| | |
|---|---|
| Result | **G won 2 of 3**: 540 (3 to 0, G played by the bot) and 541 (3 to 1). W won 542 (3 to 1), its first win in nine games. Rounds: G 7, W 4. |
| Scores by round, G | 540: 3, 7, 15. 541: 6, 7, 22, 27. 542: 3, 3, 9, 13. |
| Scores by round, W | 540: 2, 3, 10. 541: 3, 11, 14, 17. 542: 2, 8, 14, 14. |
| Game length | 3, 4 and 4 rounds. |
| Biggest turn | **4 plays** (540 round 3, W: Grudge, Elusiveness, Fairness, Largesse; 10 against 15, a loss). W's longest turn so far. |

### Insights

1. **Vitality and Fulfillment worked together the first time they were played.** In 541 G played Vitality in round 2 and Fulfillment in round 3. Vitality adds 2 to each green mood at the start of each of
   G's turns, which made Honesty 8, and Fulfillment scores each mood worth 6 or more an extra time, so Honesty alone counted 16. G scored 22 in round 3 and 27 in round 4 with only four moods, against W's 14 and 17. Vitality had not been played in any earlier game (Fulfillment had, in 534 and 535), so this is the first
   evidence for Vitality. The combination (one mood at 6 or more, +2 a turn, doubled) is large for two 1-value cards, and W did not answer it (it never drew Pacifism).
2. **W's four-play turn lost.** In 540 round 3 Grudge (G had won two rounds) gave two extra plays and Affinity a third, so W played Grudge, Elusiveness, Fairness and Largesse. That is 0, 1, 1 and 5 points, and W's 10 lost to G's 15 (Determination 6, Vindication 6 and Carelessness 3). Largesse also gave G a card.
   The longest W turn so far was worth 7 points of new moods, because W's extra-play cards are low-value cards; this repeats the E1 and session 2c finding that the engine needs bodies.
3. **W won once by using Pacifism and Orderliness.** In 542 round 2 W played Affinity, then Pacifism (a 1 matching Affinity, so Affinity's play came back) on G's Resolve, then Orderliness (odd): 8 against 3 in a turn of three plays. Orderliness (odd) raised Affinity, Pacifism and
   later Temperance (6 with fewer cards in hand), and Pacifism kept Resolve suppressed for the rest of the game, which took G's comeback card out. W scored 14 in rounds 3 and 4 with no cards left in hand.
4. **W ran out of cards again.** In 542 W had played its last card by round 3 and passed in rounds 3 and 4 (a Grudge extra play was available each time). It won round 4 by 14 to 13 with the board alone. Grudge's extra plays used: 2 of 2 in 540, 1 of 3 in 542 (R2 only), as before.
5. **G missed a stronger line in 542 round 4 (a question, not a finding).** G held Nostalgia and had Urgency in play. Nostalgia gives an extra play, and two plays in a round make Urgency a 6, so Nostalgia then Vindication would have scored 16 against W's 14
   instead of Vindication alone at 13, which would have won the round. G also held Optimism and Gratitude.
6. **Honesty was a 6 on turn one again** (541 round 1: 6 against W's 3). Determination was a 6 in 540 and 542, and Vindication a 6 in 540 round 3.
7. **Carelessness milled Urgency and Kinship in 540 round 3**, the third game where the milled cards were part of G's plan (535, 536, 540). G won anyway.
8. **Rudeness was drawn for the first time (541) and not played.** W held it in rounds 3 and 4 and played Discernment and Familiarity instead. Against G it has little to stop: G's extra plays are Joy, Nostalgia and Thrift, and its after-playing effects are Honesty's 6 and Carelessness's mill. Levelheadedness and Solidarity stayed in the deck in all three games. Elusiveness was played once as a 1-point extra play (540) and
   never needed (G has no discard effects on moods).
9. **G has no removal, so W's boards stayed intact.** W's 14 in 542 rounds 3 and 4 and its 17 in 541 came from boards of five or six moods. G's answer to a W board is size, while B and R answer a G board by removing its moods.

### Questions for the testers

- Game 542 round 4: did you see the Nostalgia then Vindication line (Urgency as a 6 for 16 against 14)? Or was Nostalgia, Optimism or Gratitude a worse play than it looks?
- Game 541: you held Rudeness in rounds 3 and 4. How does it read against G, and when would you play it?
- Game 540 round 3: would a different order of the four plays (Largesse first) have changed anything, or was Largesse giving G a card a cost you considered?
- Vitality and Fulfillment (541): did 22 and 27 against 14 and 17 feel too strong for a pair of 1-value cards? Does the color prompt at the start of each turn get tedious in a one-color deck?
- Affinity (542 round 2): did "the first time each turn you play a mood with the same number as another of your moods" read clearly when Pacifism (a 1) set it off after Affinity (a 1)?
- Fun and clarity for Vitality, Fulfillment, Grudge and the W deck against a deck with no removal.

### Game logs

**Game 540.** W (P1, seat 0) against G (bot, seat 1); W went first. G won 3 to 0.
- Scores: W 2, G 3; W 3, G 7; W 10, G 15.
- Longest turn: 4 plays (W in round 3: Grudge, Elusiveness, Fairness, Largesse).
- Decided: Determination, Vindication and Carelessness (15) against W's four low-value plays.

**Game 541.** G (P1, seat 0) against W (second tester, seat 1); W went first. G won 3 to 1.
- Scores: G 6, W 3; G 7, W 11; G 22, W 14; G 27, W 17.
- Longest turn: 2 plays (W in round 2: Confidence, then Reverence).
- Decided: Vitality and Fulfillment in rounds 3 and 4 (22 and 27). W held Affinity and Rudeness at the end.

**Game 542.** W (P1, seat 0) against G (second tester, seat 1); W went first. W won 3 to 1.
- Scores: W 2, G 3; W 8, G 3; W 14, G 9; W 14, G 13.
- Longest turn: 3 plays (W in round 2: Affinity, Pacifism, Orderliness).
- Hands: W had an empty hand from round 3 (passed in rounds 3 and 4).
- Decided: Pacifism on Resolve in round 2, Orderliness (odd), and round 4 by 14 against 13.

### Notes by card (G against W)

| Card | What the games showed |
|---|---|
| Vitality | +2 a turn to green moods; 22 and 27 with Fulfillment (541). First time played. |
| Fulfillment | Doubled Honesty at 8 (16): the 22 and 27 rounds. |
| Honesty | A 6 on turn one (541). |
| Determination, Vindication | 6 each by round 3 (540, 542). |
| Resolve | Suppressed by Pacifism for three rounds (542). |
| Urgency | A 3 (542); a 6 was available with Nostalgia in round 4. |
| Carelessness | Milled Urgency and Kinship (540). |
| Nostalgia, Optimism, Gratitude | Held in hand (542). |
| Grudge | 2 extras used of 2 (540), 1 of 3 (542); the extras need cards. |
| Affinity | A third play in 540 and 542 (Elusiveness and Pacifism matched). |
| Orderliness | Odd: +3 in 542 (Affinity, Pacifism, Temperance). |
| Pacifism | Kept Resolve suppressed (542); the 1 that set off Affinity. |
| Largesse | 5 points, gave G a card (540). |
| Rudeness | Drawn once (541), held. |
| Elusiveness, Fairness | Played as 1-point extras (540), no effect used. |
| Levelheadedness, Solidarity | Not drawn. |

## Session 2f: R Red pile against W White numbers (3 games)

**Source.** The simulator exports of games 543 to 545 (8 and 9 November). The first tester (P1) played R in 544 and W in 543 and 545. The other seat was a practice bot (R) in 543 and the second tester in the other two
games (W in 544, R in 545). The decks are the ones from sessions 2b and 2c (W has Grudge and Elusiveness).

### Summary

| | |
|---|---|
| Result | **R won 2 of 3**: 543 (3 to 2, R played by the bot) and 544 (3 to 0). W won 545 (3 to 2). Rounds: R 8, W 5. |
| Scores by round, R | 543: 3, 6, 16, 21, 21. 544: 2, 10, 16. 545: 7, 7, 1, 4, 7. |
| Scores by round, W | 543: 5, 6, 6, 12, 15. 544: 1, 3, 11. 545: 6, 7, 9, 11, 11. |
| Game length | 5, 3 and 5 rounds. |
| Biggest turn | 3 plays (544 round 1, R: Whimsy, Rashness, Dominance, 2 points because Pacifism suppressed Whimsy; 545 round 1, W: Familiarity, Modesty, Discernment, 6 points). |

### Insights

1. **Levelheadedness was played for the first time and did what it says (543 round 2).** W and R each had three moods. R's moods were worth 10 (Compulsion 3, Confidence 2, Impatience 5) against W's 7, and with every mood scoring 2 both scored 6. It only affects the round it is played, and in round 3 R's Rashness
   discarded it (a 1). It favors the player with more moods, which is why a W deck with extra plays should like it; here the count was level.
2. **Compulsion handed R one of W's own enablers.** In 543 round 1 W gave Confidence, and R played it in round 2 for a free play of Impatience (a 5): R scored 6 with three moods. Confidence is not tied to W's colors, and R's deck has 4-to-6 cards of its own (Impatience 5, Frenzy 6), so W's free-play cards work as well for R.
3. **Equanimity became a 6 in two games, with R's red zeros helping.** It counts the even numbers on every player's moods, and R's Rashness, Adrenaline and Competitiveness are 0s. In 543 round 4 it was a 6 (W 12), and in 544 round 3 it was 7 with Orderliness (odd), making 11. Before this it had never reached 6 in the W games (session 2c).
4. **Dominance was a free removal again (544 round 2).** Exuberance (a 6 with three other red moods) was played, and Dominance put W's Pacifism (a 1) into the discard pile, which also freed the suppressed Whimsy. R scored 10 against 3. This is the second game where Dominance does most of R's removal (537).
5. **FOMO's 7 was paid for with R's hand (545).** R played Rashness then FOMO on turn one (a 7, with Competitiveness as the cost) and kept it in round 2 by discarding Ruthlessness, scoring 7 and 7 against W's 6 and 7. In round 3 R had no cards left: FOMO went into the discard pile (no card to
   pay) and R passed with nothing to play, scoring 1 against W's 9. R then drew one card a round and scored 4 and 7. So FOMO won two rounds and left R with an empty hand for the rest of the game, the cost the checklist asked about. 
6. **Covetousness had its first real uses.** At the start of R's turns in 545 it took W's Elusiveness (round 3) and Fairness (round 5), both worth 1, a swing of 2 each time. It cost W cards that W had paid plays for. The stolen Fairness did not suppress anything for R in the round it was taken.
7. **Belligerence did not sweep in 545 round 5.** W had four moods of value 2 (Familiarity, Modesty, Discernment, Confidence), and Belligerence would have put all of them into the discard pile (W 11 would have become Temperance's 3 against R's 7). The log shows no choice for it. In the simulator that "you may" is an opt-in checkbox at play time, so the log cannot tell a declined effect
   from a checkbox that was not ticked. We need the tester to say which it was; if players miss the checkbox, the "may" effects with big payoffs need a clearer prompt.
8. **W's Rudeness was cycled away, not played.** In 545 round 1 Discernment (the third play of a three-play turn) put Rudeness on the bottom of the deck and drew Elusiveness. Rudeness has now been held or looted away in every game it was drawn (541, 545); it is the card W wants to get rid of.
9. **W ran out of cards again in 543.** W passed in rounds 4 and 5 with an empty hand (three Grudge extra plays unused, none used all game). In 545 W's wins in 545 came from boards of four or five moods that R could not match once its hand was empty.
10. **Frenzy was a 6 (544 round 3) and went to the discard pile after scoring, as written.** R's 16 against 11 was Exuberance 6, Frenzy 6 and Whimsy, Rashness, Dominance.

### Questions for the testers

- Game 545 round 5: Belligerence was played with four of W's moods in range. Did you decline the sweep, or did you not see the checkbox? (Both answers are useful.)
- Game 543 round 1: you gave Confidence to Compulsion. Was it the weakest card in hand, and did you expect R to use it?
- Game 545 rounds 2 and 3: was keeping FOMO by discarding Ruthlessness worth it in hindsight? Did the 7 feel fair for the cost?
- Game 543 round 2: how did Levelheadedness read when you played it, and would you have wanted it later (R had more moods than W in rounds 3 to 5)?
- Covetousness: did taking 1-value moods feel worth a play? Was it clear when the stolen mood's own ability applies?
- Fun and clarity for Levelheadedness, FOMO, Covetousness, Dominance and Equanimity (counting both players' moods).

### Game logs

**Game 543.** W (P1, seat 0) against R (bot, seat 1); R went first. R won 3 to 2.
- Scores: W 5, R 3; W 6, R 6; W 6, R 16; W 12, R 21; W 15, R 21.
- Longest turn: 2 plays (W in round 1: Familiarity, Solidarity; R in rounds 2 and 3).
- Hands: W had an empty hand in rounds 4 and 5 (three unused Grudge plays).
- Decided: Rashness and Exuberance in round 3 (16), Ruthlessness and R's seven moods in rounds 4 and 5.

**Game 544.** R (P1, seat 0) against W (second tester, seat 1); R went first. R won 3 to 0.
- Scores: R 2, W 1; R 10, W 3; R 16, W 11.
- Longest turn: 3 plays (R in round 1: Whimsy, Rashness, Dominance).
- Decided: Dominance removing Pacifism in round 2, Exuberance and Frenzy as 6s in round 3.

**Game 545.** W (P1, seat 0) against R (second tester, seat 1); R went first. W won 3 to 2.
- Scores: W 6, R 7; W 7, R 7; W 9, R 1; W 11, R 4; W 11, R 7.
- Longest turn: 3 plays (W in round 1: Familiarity, Modesty, Discernment).
- Hands: R had an empty hand from round 3 (FOMO dropped, one pass).
- Decided: FOMO's cost (R out of cards), Covetousness on Elusiveness and Fairness, Belligerence played without the sweep in round 5.

### Notes by card (R against W)

| Card | What the games showed |
|---|---|
| Levelheadedness | First play (543 round 2): two three-mood boards both scored 6; discarded by Rashness next round. |
| Compulsion | Took W's Confidence (543); R used it. |
| Equanimity | A 6 in 543 round 4 and 544 round 3 (R's 0-value moods count). |
| Dominance | Removed Pacifism for free (544 round 2). |
| FOMO | 7 and 7 in rounds 1 and 2 (545), then dropped with no card to pay. |
| Covetousness | Took Elusiveness and Fairness (545). |
| Belligerence | Played with four targets and no sweep (545 round 5). |
| Rashness | Extra play every time (544, 545); discarded Levelheadedness (543). |
| Frenzy | A 6, then discarded after scoring (544). |
| Rudeness | Looted to the bottom by Discernment (545). |
| Discernment | Loot in a three-play turn (545 round 1). |
| Grudge | Three extra plays granted and unused (543). |
| Pacifism | Suppressed Whimsy until Dominance removed it (544). |
| Exuberance | A 6 in both games it was played (543 round 3, 544 round 2). |

## Session 3a: PW White even numbers against PU Blue Reverie engine (5 games)

**Source.** The simulator exports of games 546 to 550 (9 November), the first games with the Power Duel decks (15 cards, one mythic; see `design/playtest-decks.md`, session 3). The first
tester (P1) played PU in 546, 548 and 550 and PW in 547 and 549. The other seat was a practice bot (PW) in 546 and the second tester in the other four games (PW in 548 and 550, PU in 547 and 549).
PW is the white even-numbers deck with Orderliness as its mythic; PU is the blue Reverie deck.

### Summary

| | |
|---|---|
| Result | **PW won 3 of 5** (546 against P1, 548 and 549); PU won 547 and 550. Rounds: PW 11, PU 9. Round scores: 3 to 1 (546), 0 to 3 (547), 3 to 0 (548), 3 to 2 (549), 2 to 3 (550). |
| Scores by round, PW | 546: 0, 4, 7, 11. 547: 0, 2, 7. 548: 5, 5, 9. 549: 2, 2, 7, 12, 16. 550: 1, 1, 4, 7, 13. |
| Scores by round, PU | 546: 2, 3, 6, 9. 547: 2, 7, 9. 548: 1, 3, 6. 549: 0, 5, 8, 9, 12. 550: 0, 1, 9, 10, 13. |
| Game length | 3 to 5 rounds, 4.0 on average (547 and 548 ended 3 to 0 after three rounds). |
| Biggest turn | 2 plays (both decks; PU played Impulse and a second mood every turn from round 3 in game 550). Highest scores: 16 (PW, 549 round 5) and 13 each (550 round 5). |

### Insights

1. **Neither build-around mythic did anything.** Orderliness stayed in the deck in all five games. Reverie was drawn in three games and never worked: in 547 it was played in round 3 with an empty discard
   pile (nothing happened, a 2); in 546 it was discarded to Reflection in round 4; in 550 it was put on the bottom of the deck as Resignation's cost in round 3. With one mythic in a 15-card deck, about eight of the 15 cards
   are seen in a game, so the mythic shows up in about half the games, and both decks won and lost without it. The format needs a deck that works without its mythic, or a way to find it.
2. **Deflection answered Temperance every time (546, 547, 548).** PW opened with Temperance (a 5 when it holds fewer cards than the opponent) in three games, and PU's Deflection bounced it and locked the name for a turn: 0 against 2 (546, 547) and 5 against 3 (548 round 2). A 2-value bounce that
   also locks a replay was good against a one-mood board.
3. **Equanimity counts both boards, so PU's even numbers help PW.** In 546 round 4 PU played Resignation (a 6, even) and PW's Equanimity became a 6 (four even moods): PW scored 11 against 9. PU's Deflection, Fear, Impulse, Reverie and Resignation are all even.
   Equanimity was part of PW's best turns in 546 and 548.
4. **Impartiality (odd) is strong against PU.** In 549 round 1 it suppressed Rumination (1) and Desperation (3), the two moods PU had just played with two plays: 2 against 0. Most of PU's cards print an odd number (1s and 3s). In 550 PW held Impartiality for the last two rounds (it was drawn after round 3) while PU's board
   had three odd moods (Panic 1, Elusiveness 1, Reminiscence 3).
5. **Rumination was declined every time it was offered (six prompts in 548 and 549).** Its start-of-turn choice is a bounce of your own mood, so with Panic or Deflection it could re-buy a bounce every turn without spending a card. No game used it. PU's low-value openers also cost tempo (548 round 1: Rumination 1 against PW's 5).
6. **PU's one strong line was Panic on its own board and Impulse (550).** After Pacifism suppressed Resignation (0 against 1 in round 1), PU played Panic on Resignation and on PW's Equanimity, which freed Resignation from the suppression and replayed it next to Impulse in round 3: 9 against 4. From then on
   Impulse (which returns to hand after scoring) gave PU two plays a turn and 2 points a round with no card cost; PU scored 9, 10 and 13 against PW's 4, 7 and 13 and won the game.
7. **Scores were low (a round 5 of 12 to 16) compared with the 20-card decks (24 to 40).** Neither deck got its scaling card, and 15-card games ended in three rounds twice. The games looked like ordinary decks, not engines.
8. **Fairness was never played again** (held at the end of 547 and 549), and PW's Affinity was held in three games (546, 547, 550). W's utility cards sit in hand when the board is small.

### Questions for the testers

- Game 548 (and 549): Rumination was declined every turn. Did you see a use for it (re-buying Panic or Deflection each turn), or did the prompt not read as a bounce of your own mood?
- Game 547 round 3 and game 550 round 3: Reverie was played with an empty pile and then put on the bottom as a cost. Was Reverie hard to use, or was it just the least useful card in hand? Game 546: why discard it to Reflection?
- Game 547 round 3: after Modesty, PW played Temperance (3) with Solidarity in hand. Solidarity would have been a 6 (four other 2s: Reassurance, Modesty, Deflection, Reverie), 10 against 9. Was that seen, or was Temperance chosen for another reason?
- Game 550 rounds 4 and 5: PW held Impartiality (odd) with PU's odd moods worth 5 points. Why not play it?
- Does a 15-card deck with one mythic feel right? Should a Power Duel deck have some way to find its mythic?
- Fun and clarity for Deflection, Impartiality, Impulse and Equanimity (counting both players' moods).

### Game logs

**Game 546.** PU (P1, seat 0) against PW (bot, seat 1); PW went first. PW won 3 to 1.
- Scores: PU 2, PW 0; PU 3, PW 4; PU 6, PW 7; PU 9, PW 11.
- Longest turn: 2 plays (PW in round 2: Familiarity, Discernment).
- Decided: Deflection on Temperance (round 1), Equanimity as a 6 in round 4 (Resignation's 6 counted), Reverie discarded to Reflection.

**Game 547.** PW (P1, seat 0) against PU (second tester, seat 1); PW went first. PU won 3 to 0.
- Scores: PW 0, PU 2; PW 2, PU 7; PW 7, PU 9.
- Longest turn: 2 plays (PW in round 3: Modesty, Temperance).
- Decided: Deflection on Temperance, Detachment (5) in round 2, Reverie played with an empty pile.

**Game 548.** PU (P1, seat 0) against PW (second tester, seat 1); PU went first. PW won 3 to 0.
- Scores: PU 1, PW 5; PU 3, PW 5; PU 6, PW 9.
- Longest turn: 2 plays (PW in round 1: Modesty, Equanimity).
- Decided: Modesty then Equanimity in round 1; Rumination declined in rounds 2 and 3; PU held four cards at the end.

**Game 549.** PW (P1, seat 0) against PU (second tester, seat 1); PU went first. PW won 3 to 2.
- Scores: PW 2, PU 0; PW 2, PU 5; PW 7, PU 8; PW 12, PU 9; PW 16, PU 12.
- Longest turn: 2 plays (PU in round 1: Desperation, Rumination; PW in rounds 3, 4 and 5).
- Decided: Impartiality (odd) in round 1, Panic on Reverence in round 2, Modesty then Temperance and Familiarity then Discernment in rounds 4 and 5.

**Game 550.** PU (P1, seat 0) against PW (second tester, seat 1); PU went first. PU won 3 to 2.
- Scores: PU 0, PW 1; PU 1, PW 1; PU 9, PW 4; PU 10, PW 7; PU 13, PW 13.
- Longest turn: 2 plays (PU in rounds 3, 4 and 5: Impulse with Resignation, Elusiveness and Reminiscence).
- Decided: Pacifism on Resignation and Panic on both players' moods in round 2, then Impulse every turn.

### Notes by card (PW against PU)

| Card | What the games showed |
|---|---|
| Orderliness | Not drawn in five games. |
| Reverie | Played once with no pile cards (547); discarded to Reflection (546); put on the bottom as a cost (550). |
| Deflection | Bounced Temperance in all three games it was played (546, 547, 548). |
| Equanimity | A 6 in 546 round 4 (Resignation's 6 counted); part of PW's best turns in 546 and 548. |
| Impartiality | Suppressed Rumination and Desperation (549 round 1); held unused in 550. |
| Rumination | Declined six times; played as a 1-point mood. |
| Panic | Bounced both its own suppressed Resignation and PW's Equanimity (550 round 2). |
| Impulse | Two plays a turn and 2 points a round from round 3 (550). |
| Resignation | A 6 (546 round 4, 550 rounds 3 to 5); suppressed by Pacifism in 550 round 1. |
| Detachment | A 5 in 547 round 2 (7 against 2). |
| Temperance | PW's usual first play: bounced by Deflection three times. |
| Solidarity | Held in 547 when it would have been a 6; a 4 in 548 round 3. |
| Fairness, Affinity | Not played (held at the end of 547 and 549). |
| Reflection | Discarded Fear and Reverie to loot (546). |

## Session 3b: PW White even numbers against PB Black Neglect pressure (6 games)

**Source.** The simulator exports of games 551 to 556 (9 November), the second Power Duel pairing (15 cards, one mythic). The first tester (P1) played PB in 551, 553 and 555 and PW in 552, 554 and 556. The other seat was a practice
bot (PW) in 551 and the second tester in the other five games (PW in 553 and 555, PB in 552, 554 and 556). PW is the white even-numbers deck (Orderliness); PB is the black hand-pressure deck (Neglect).

### Summary

| | |
|---|---|
| Result | **PB won 4 of 6** (552, 554, 555, 556); PW won 551 (against P1, PW played by the bot) and 553, both 3 to 0. Rounds: PB 12, PW 10. |
| Scores by round, PW | 551: 5, 9, 5. 552: 2, 7, 14, 14. 553: 9, 14, 9. 554: 2, 5, 10. 555: 4, 6, 3, 1, 0. 556: 0, 3, 3, 8. |
| Scores by round, PB | 551: 2, 5, 5. 552: 5, 10, 12, 16. 553: 1, 4, 6. 554: 5, 10, 13. 555: 3, 5, 7, 9, 15. 556: 0, 6, 9, 9. |
| Game length | 3 to 5 rounds, 3.7 on average (551, 553 and 554 ended after three rounds). |
| Biggest turn | 3 plays (553 round 1, PW: Familiarity, Modesty, Humility, 9 against 1; 556 round 3, PW: Modesty, Levity, Fairness, 3 points; PB's biggest was 2 plays). Highest scores: 16 (PB, 552) and 15 (PB, 555 round 5). |

### Insights

1. **Neglect decided the one game where it ran, and the PW player's wins were the reason.** In 555 PW won rounds 1 and 2, so it drew no cards, and its hand was empty by round 3. Neglect (a 2) then removed PW's best mood before scoring in rounds 3, 4 and 5 (Humility, Discernment, Fairness), with Nosiness taking PW's last card in round 4 and
   Vengeance a mood in round 5: PB won 7 to 3, 9 to 1 and 15 to 0. In 553 it also fired once (round 3, after PW had passed with no cards): it removed Reverence (a 5), but PW still won 9 to 6 with three moods. The round winner draws nothing at the end of the round, so the leader's hand runs dry first and Neglect punishes it; this is the same
   effect as Hellbent (Q9).
2. **Neglect ran in only two of six games.** It was discarded as Dejection's cost in 554 (round 1), and stayed in the deck in 551, 552 and 556. In a 15-card deck with one mythic the mythic is seen in about half the games, as in session 3a.
3. **PB's 5s start fast.** Dejection (a black 5, each player discards a card) and Resentment (colorless 5, needs a black mood) gave PB 10 points by round 2 in 552 and 554 (5 against 2 in round 1, then 10 against 7 in 552 and 10 against 5 in 554). PW's own gate, Reverence, is the matching play. Dejection is symmetric: PW discarded Impartiality both times, and PB discarded Remorse (552) and its own Neglect (554).
4. **Hate and Vengeance answered PW's best mood every game.** Hate put Temperance on the bottom of the deck (556 round 1: 0 against 0) and Solidarity (552 round 4: PB won 16 to 14); Vengeance discarded Temperance (551), Solidarity (556) and Pacifism (555). Temperance is PW's usual first play, and it has now been answered in five of the games where it was played (three times by Deflection in session 3a, then Vengeance in 551 and Hate in 556).
5. **PW's engine works when it draws a starter.** The two PW wins both had Familiarity (551, 553: Familiarity then Discernment, and Familiarity, Modesty, Humility for 9 against 1). In 554 PW drew none of Familiarity, Modesty, Affinity or Levity and played one mood a turn, losing 3 to 0. PW's wins and losses followed the extra-play cards, as in the 20-card games.
6. **Orderliness was played for the first time (554 round 2, even)** and was a +1 on Reassurance: 5 against 10. It was not enough on its own.
7. **PB held many cards.** At the end PB held five cards in 553 (including Dejection, a 5, unplayed all game while PB opened with Opportunism, a 1), four in 551, three in 556. PB's own extra play is Remorse (once). It plays one mood a round like PW without the extra-play cards, so its hand grows (Composure
   became a 6 in 552 and 556) but it does not use it.
8. **Fairness worked once (556 round 4).** It suppressed Resentment (5) at the start of PW's turn, so PB scored 9 (Composure 6, Vengeance 3, Hate 0) instead of 14, but PW lost 8 to 9 anyway.
9. **Opportunism took a discard once** (553 round 2: PW's Pacifism went to Suspicion and into PB's hand) and the card was never played.

### Questions for the testers

- Game 554 round 1: PB discarded Neglect (its mythic) to Dejection. Was that the weakest card in hand, or was Neglect hard to see a plan for?
- Game 553: PB opened with Opportunism (1) and held Dejection all game. Why not Dejection in round 1 (a 5 against PW's 9)?
- Game 555 round 1: PW kept Levity in play (0, 1 with Humility) instead of bottoming it to draw. Was that a choice? Levity's draw would have kept PW's hand from running dry before Neglect.
- Game 552: PW held Equanimity from round 1 to round 4 and played other cards. Was it the least useful (it needs four even moods)?
- Game 556 round 1: PW opened with Temperance again (bottomed by Hate). Is it the best first play, or the default? Would you hold it?
- Neglect (555): how did it read and play? Choosing the mood to discard, and the opponent's empty hand being a before-scoring condition: clear? Too strong for a 2?
- Fun and clarity for Dejection, Resentment, Hate, Vengeance and Neglect.

### Game logs

**Game 551.** PB (P1, seat 0) against PW (bot, seat 1); PW went first. PW won 3 to 0.
- Scores: PB 2, PW 5; PB 5, PW 9; PB 5, PW 5.
- Longest turn: 2 plays (PW in round 2: Familiarity, Discernment; PB in round 2: Remorse, Schadenfreude).
- Decided: Temperance as a 5 in round 1, Nosiness on Humility, Pacifism on Schadenfreude and Vengeance on Temperance in round 3.

**Game 552.** PW (P1, seat 0) against PB (second tester, seat 1); PB went first. PB won 3 to 1.
- Scores: PW 2, PB 5; PW 7, PB 10; PW 14, PB 12; PW 14, PB 16.
- Longest turn: 2 plays (PW in rounds 2 and 3: Levity then Reverence, Modesty then Solidarity).
- Decided: Dejection and Resentment (10 by round 2), Hate on Solidarity in round 4 (16 against 14).

**Game 553.** PB (P1, seat 0) against PW (second tester, seat 1); PB went first. PW won 3 to 0.
- Scores: PB 1, PW 9; PB 4, PW 14; PB 6, PW 9.
- Longest turn: 3 plays (PW in round 1: Familiarity, Modesty, Humility).
- Hands: PW had no cards in round 3 (Neglect fired, removing Reverence); PB held five cards at the end.
- Decided: PW's three-play first turn (9 against 1).

**Game 554.** PW (P1, seat 0) against PB (second tester, seat 1); PB went first. PB won 3 to 0.
- Scores: PW 2, PB 5; PW 5, PB 10; PW 10, PB 13.
- Longest turn: 1 play every turn.
- Decided: Dejection and Resentment again (10 by round 2); PW drew no extra-play card.

**Game 555.** PB (P1, seat 0) against PW (second tester, seat 1); PW went first. PB won 3 to 2.
- Scores: PB 3, PW 4; PB 5, PW 6; PB 7, PW 3; PB 9, PW 1; PB 15, PW 0.
- Longest turn: 2 plays (PW in round 1: Levity, Humility).
- Hands: PW's hand was empty from round 3; Neglect fired in rounds 3, 4 and 5.
- Decided: Neglect, Nosiness and Vengeance in rounds 3 to 5.

**Game 556.** PW (P1, seat 0) against PB (second tester, seat 1); PW went first. PB won 3 to 1.
- Scores: PW 0, PB 0; PW 3, PB 6; PW 3, PB 9; PW 8, PB 9.
- Longest turn: 3 plays (PW in round 3: Modesty, Levity, Fairness).
- Decided: Hate on Temperance (round 1), Composure as a 6 and Vengeance on Solidarity (round 3), Fairness on Resentment in round 4 (8 against 9).

### Notes by card (PW against PB)

| Card | What the games showed |
|---|---|
| Neglect | Fired in rounds 3 to 5 of 555 (removed Humility, Discernment, Fairness) and once in 553 (Reverence); discarded as a cost in 554; not drawn in three games. |
| Dejection | A 5 on turn one in 552 and 554 (and symmetric: PB discarded Neglect once). Held unplayed in 553. |
| Resentment | A 5 in round 2 of 552, 554 and 555. |
| Hate | Bottomed Temperance (556) and Solidarity (552); the 16 to 14 in 552 round 4. |
| Vengeance | Discarded Temperance, Pacifism and Solidarity (551, 555, 556). |
| Nosiness | Took Humility (551) and Modesty (555 round 4). |
| Opportunism | Took a discarded Pacifism (553), never played. |
| Composure | A 6 in 552 and 556. |
| Temperance | PW's opener; answered by Hate (556) and Vengeance (551). |
| Familiarity and Modesty chains | 9 against 1 (553 round 1); absent in 554. |
| Orderliness | First played (554 round 2, even): +1 on Reassurance. |
| Fairness | Suppressed Resentment (556 round 4); a 1 elsewhere. |
| Equanimity | Held unplayed in 552. |
| Levity | Kept in play in 555 (no draw), bottomed to draw in 552 and 556. |

## Session 3c: PW White even numbers against PR Ardor red pile (6 games)

**Source.** The simulator exports of games 557 to 562 (9 November), the third Power Duel pairing (15 cards, one mythic). The first tester (P1) played PR in 557, 559 and 561 and PW in 558, 560 and 562. The other seat was a practice
bot (PW) in 557 and the second tester in the other five games (PW in 559 and 561, PR in 558, 560 and 562). PR is the red Ardor deck; PW is the white even-numbers deck. The round scores in these games match the new Ardor text ("other red moods", Q13):
for example, four red moods gave +3 each in game 560 round 3, not +4.

### Summary

| | |
|---|---|
| Result | **PW won 4 of 6** (557, 558, 559 and 562); PR won 560 and 561. Rounds: PW 15, PR 9. Round scores in the games: 3 to 0 (557, 558), 3 to 1 (559), 2 to 3 (560), 1 to 3 (561), 3 to 2 (562). |
| Scores by round, PW | 557: 7, 12, 14. 558: 9, 14, 19. 559: 4, 5, 10, 11. 560: 4, 12, 15, 18, 19. 561: 5, 4, 7, 12. 562: 1, 6, 10, 10, 16. |
| Scores by round, PR | 557: 0, 7, 12. 558: 6, 7, 10. 559: 3, 9, 5, 11. 560: 8, 8, 11, 31, 24. 561: 0, 5, 32, 37. 562: 7, 12, 2, 5, 8. |
| Game length | 3 to 5 rounds, 4.0 on average. |
| Biggest turn | 3 plays (PR in 561 rounds 2 and 3; PW in 558 round 1: Familiarity, Modesty, Temperance, 9 against 6). **Highest scores: PR 37 (561 round 4) and 32 (561 round 3), 31 (560 round 4).** |

### Insights

1. **Ardor won both games it appeared in, and the scores are still very large.** It was drawn in two of six games (560, 561) and PR won both. Four red moods gave 11 (560 round 3, with Exuberance suppressed), five gave 31 (560 round 4) and 24 (round 5, suppressed Exuberance), six gave 32 (561 round 3) and seven gave 37
   (561 round 4, Ruthlessness suppressed by Fairness). PW scored 18 and 19 in 560 and 7 and 12 in 561. The "other red moods" change takes one point from each red mood (40 would have been about 35), but the payoff still grows with the square of the red count, and 561's 32 came from only
   three rounds. The change did not stop the snowball once PR had five or more red moods.
2. **PR's chain, not Ardor alone, builds the red count.** In 561 round 3 PR played Whimsy (revealing Zeal), Zeal, and Ardor (Adrenaline's extra play): three plays and six red moods, 32 against 7. In round 2 it played Compulsion, Levity (stolen from PW by Compulsion) and Shock. Adrenaline, Whimsy and Rashness gave PR two or three plays a turn
   in 560 and 561; PR mostly made one play a turn in 558 and 562 and lost both.
3. **White has no answer to Ardor.** Suppression keeps abilities (value 0 only), so Pacifism and Impartiality do nothing to Ardor itself; they hit single moods (Exuberance in 560, Compulsion in 561). Fairness suppressed the highest mood each turn and was the best answer: in 562 it held Zeal and then Vindictiveness
   back, and PR scored 2, 5 and 8 in rounds 3 to 5. PW has no discard or bounce effect; a mono-white deck loses to a fast Ardor unless it wins the first three rounds.
4. **FOMO drained PR's hand again, and PR lost both games it played it (558, 562).** In 562 PR discarded Adrenaline (round 1) and Verve (round 2) to FOMO, a 7 in rounds 1 and 2 (7 and 12 points); in round 3 it had no cards in hand, FOMO went to the discard pile, and PR passed with nothing to play. It scored 2, 5 and 8. In 558
   PR discarded Exuberance and then Impatience (a 5) to keep FOMO, and lost 3 to 0. With the 545 game this is three FOMO games and three losses for the deck that played it; in the two PR wins FOMO was not in play. In a 15-card deck its cost is larger.
5. **PR's turn-one plays were weak.** PR opened with Adrenaline (0) in 557 and 561 and with Verve (1) in 559, and lost round 1 each time (0 against 7, 0 against 5, 3 against 4). PW's chains score 5 to 9 in round 1 (Modesty then Temperance 7; Familiarity, Modesty, Temperance 9). The engine cards are worth little by themselves.
6. **Compulsion gave PR a free play again (561 round 2).** PW gave Levity, and PR played it to draw and take an extra play: Compulsion, Levity, Shock in one turn. As with Confidence in session 2f, W's free-play cards work for the opponent.
7. **Orderliness worked when it showed up.** In 558 round 3 (even) PW scored 19 against 10, with Familiarity, Modesty and Humility each +1; in 562 (odd) it raised Affinity and Fairness. It was drawn in two of six games.
8. **Equanimity counts both boards and PR's 2-value red cards help it.** In 559 round 3 it was a 6 (Discernment, Reassurance, Whimsy and Shock are even): PW 10 against 5. In 559 round 3 PR passed holding Exuberance, which would have been a 6 (11 against 10) with its three red moods.

### Questions for the testers

- Game 559 round 3: PR passed holding Exuberance (a 6 with Verve, Whimsy and Shock out: 11 against PW's 10). Why? Was it a decision or a mis-click?
- Games 558 and 562: PR discarded Adrenaline, Verve, Exuberance and Impatience to FOMO. Did the 7 feel worth the cards, and did you plan the hand running dry in round 3?
- Game 561: PW gave Levity to Compulsion. Was it the weakest card in hand, and did you see the free play coming? Which card would you give instead?
- Game 561 rounds 3 and 4: Ardor with six and seven red moods. Did white have any answer, and what would you want white to have against it?
- Game 562 rounds 3 and 4: PW passed with Equanimity in hand (it would have been a 6 with four even moods). Why not play it?
- Ardor at five to seven red moods (31 and 37, after the change to "other"): does it feel too fast, or is it right for a mythic that took three rounds of chaining?
- Fun and clarity for Ardor, Fairness (suppressing each turn), Orderliness and FOMO in a 15-card deck.

### Game logs

**Game 557.** PR (P1, seat 0) against PW (bot, seat 1); PR went first. PW won 3 to 0.
- Scores: PR 0, PW 7; PR 7, PW 12; PR 12, PW 14.
- Longest turn: 2 plays (PW in round 1: Modesty, Temperance; PR in rounds 2 and 3).
- Decided: Adrenaline as a turn-one 0, Modesty then Temperance (7), Reverence in round 2; Belligerence was played without a sweep.

**Game 558.** PW (P1, seat 0) against PR (second tester, seat 1); PW went first. PW won 3 to 0.
- Scores: PW 9, PR 6; PW 14, PR 7; PW 19, PR 10.
- Longest turn: 3 plays (PW in round 1: Familiarity, Modesty, Temperance).
- Decided: PW's three-play first turn, FOMO's cost (Exuberance, then Impatience), Orderliness (even) in round 3 (19).

**Game 559.** PR (P1, seat 0) against PW (second tester, seat 1); PR went first. PW won 3 to 1.
- Scores: PR 3, PW 4; PR 9, PW 5; PR 5, PW 10; PR 11, PW 11.
- Longest turn: 2 plays (both sides).
- Decided: PR passed in round 3 holding Exuberance; Equanimity as a 6 in round 3; Pacifism on Shock in round 4.

**Game 560.** PW (P1, seat 0) against PR (second tester, seat 1); PW went first. PR won 3 to 2.
- Scores: PW 4, PR 8; PW 12, PR 8; PW 15, PR 11; PW 18, PR 31; PW 19, PR 24.
- Longest turn: 2 plays (both sides, rounds 1 and 2).
- Decided: Ardor and Verve with five red moods (31) in round 4, Impatience in round 5 (24 against 19).

**Game 561.** PR (P1, seat 0) against PW (second tester, seat 1); PR went first. PR won 3 to 1.
- Scores: PR 0, PW 5; PR 5, PW 4; PR 32, PW 7; PR 37, PW 12.
- Longest turn: 3 plays (PR in rounds 2 and 3).
- Decided: Compulsion, Levity and Shock in round 2; Whimsy, Zeal and Ardor with six red moods in round 3 (32 against 7).

**Game 562.** PW (P1, seat 0) against PR (second tester, seat 1); PR went first. PW won 3 to 2.
- Scores: PW 1, PR 7; PW 6, PR 12; PW 10, PR 2; PW 10, PR 5; PW 16, PR 8.
- Longest turn: 2 plays (PR in round 2, PW in rounds 2 and 3).
- Hands: PR's hand was empty in round 3 (FOMO dropped, one pass).
- Decided: FOMO's cost (Adrenaline, Verve), Fairness suppressing Zeal and Vindictiveness in rounds 3 to 5.

### Notes by card (PW against PR)

| Card | What the games showed |
|---|---|
| Ardor | Drawn in 560 and 561, both PR wins: 11 (four red), 31 and 24 (five), 32 (six), 37 (seven). Suppression does not turn it off. |
| Adrenaline | Free extra play in 561 (Compulsion, Levity, Shock; Whimsy, Zeal, Ardor); a turn-one 0 in 557 and 561. |
| Whimsy, Rashness | Extra play every time (558 to 562); the chain behind PR's big turns. |
| FOMO | 7 in rounds 1 and 2 of 562, then dropped with no card to pay; PR lost 558 and 562. |
| Compulsion | Took PW's Levity and PR used it (561 round 2). |
| Belligerence | Played without a sweep (557 round 2). |
| Orderliness | 19 against 10 in 558 round 3 (even); odd in 562. |
| Fairness | Suppressed Zeal, Zeal and Vindictiveness (562 rounds 3 to 5) and Ruthlessness (561 round 4). |
| Familiarity, Modesty chains | 9 against 6 (558 round 1), 7 against 0 (557 round 1). |
| Equanimity | A 6 in 559 round 3; held in 562 rounds 3 and 4. |
| Pacifism, Impartiality | Hit single moods (Shock, Compulsion, Exuberance); no effect on Ardor. |
| Exuberance | A 6 in 560 (rounds 2, 4); held while PR passed in 559 round 3. |

## Session 3d: PW White even numbers against PG Green Fulfillment anthems (4 games)

**Source.** The simulator exports of games 563 to 566 (9 November), the fourth Power Duel pairing (15 cards, one mythic). The first tester (P1) played PG in 563 and 565 and PW in 564 and 566. The other seat was a practice bot (PW) in 563 and (PG) in 566, and the second tester
in 564 (PG) and 565 (PW). PG is the green Fulfillment anthem deck; PW is the white even-numbers deck.

### Summary

| | |
|---|---|
| Result | **PG won 3 of 4** (563 and 565 by 3 to 0 and 3 to 1, 564 by 3 to 2); PW won 566 (3 to 1, against the PG bot). Rounds: PG 10, PW 6. |
| Scores by round, PG | 563: 6, 10, 15. 564: 3, 12, 0, 20, 25. 565: 1, 7, 8, 18. 566: 3, 8, 23, 5. |
| Scores by round, PW | 563: 4, 9, 13. 564: 4, 9, 9, 18, 24. 565: 3, 6, 6, 11. 566: 8, 14, 20, 19. |
| Game length | 3, 5, 4 and 4 rounds, 4.0 on average. |
| Biggest turn | 3 plays (PW in 566 round 1: Modesty, Familiarity, Solidarity, 8 against 3). PG made 2 plays a turn three times (564 round 5, 565 round 3, 566 round 2). Highest scores: 25 (PG, 564 round 5) and 24 (PW), 23 (PG, 566 round 3). |

### Insights

1. **Impartiality (odd) was the best card in the matchup.** PG's moods nearly all print an odd number (the 3/6 cards print 3, Contentment 5, Kinship and Vitality 1), and Impartiality suppresses every other odd mood until the end of the round. In 564 round 3 it suppressed Resolve, Determination and Contentment: PG 0 against PW 9. In 566 round 4
   it suppressed Vitality, Joy, Kinship and Resolve (and PW's own Equanimity): PG 5 against PW 19. Both were round wins for PW that PG could not answer. It checks the printed number, not the value, so a 6-valued Resolve is still suppressed. Against PW's own board the cost was small (Humility in 564, Equanimity in 566).
2. **The suppressed Vitality still worked.** In 565 round 3 Impartiality suppressed Vitality (a 1) and Urgency, but Vitality's start-of-turn bonus still happened (+2 to each green mood), and PG won 8 to 6. As expected, suppression only sets the value to 0.
3. **Neither mythic did much.** Fulfillment stayed in the deck in all four games, and Orderliness was played in two (563 round 3, 566 round 2, both even, +1 on the 2s), held in 565 and left in the deck in 564. PG won three games without its mythic, which is consistent with sessions 3a to 3c.
4. **Maturity and Vitality were the PG engine in 565.** Maturity (played in round 2) grew 2, 4, 6, and with Vitality's +2 PG scored 7, 8 and 18 against PW's 6, 6 and 11. Maturity prints a 2, so Impartiality (odd) does not touch it, and white had no way to remove it (no discard or bounce). This is the first game where Maturity was played.
5. **Close games, decided by small margins.** Round scores in the long games were 6 to 4, 10 to 9, 15 to 13 (563) and 25 to 24 (564 round 5, PG won by one point). PW's engine keeps up with PG until PG's 6-valued moods come online.
6. **Honesty was a 6 on turn one again** (563 round 1: 6 against 4). In 564 Resolve and Determination were 6s by round 2 (12 against 9), and in round 4 PG scored 20 with Resolve, Determination, Contentment and Joy.
7. **The PW bot's Impartiality did nothing in 563 round 1.** PW played it first (odd) with no odd mood on the board; PG played after it, so the suppression had nothing to hit. This is the same kind of choice as the Orderliness parity in 527: the bot picks a parity without looking at the board. Turn order matters for Impartiality, since it only affects moods already in play.

### Questions for the testers

- Game 564 round 3: PG played Contentment (a 5) into Impartiality. Did you see the odd suppression coming? Would PG have held its odd moods back, and would you change how you build around odd-numbered cards?
- Game 566 round 4: Impartiality (odd) beat PG's board 19 to 5. Is it too strong against a deck whose cards print 3s, or fair for an uncommon you have to draw and play after they commit?
- Game 565: PW held Orderliness from round 3 to round 4 and played Pacifism instead. Why? Did white have an answer to Maturity?
- Game 564 round 5: PG won 25 to 24 with Perseverance and Urgency. What would PW have done differently with its last play (Reverence), and did the hand (Temperance) matter?
- Fun and clarity for Impartiality (printed number, odd or even, all other moods), Vitality and Maturity.

### Game logs

**Game 563.** PG (P1, seat 0) against PW (bot, seat 1); PW went first. PG won 3 to 0.
- Scores: PG 6, PW 4; PG 10, PW 9; PG 15, PW 13.
- Longest turn: 2 plays (PW in round 1: Modesty, Impartiality, with nothing to suppress).
- Decided: Honesty as a 6 on turn one, Vindication as a 6 by round 3.

**Game 564.** PW (P1, seat 0) against PG (second tester, seat 1); PW went first. PG won 3 to 2.
- Scores: PW 4, PG 3; PW 9, PG 12; PW 9, PG 0; PW 18, PG 20; PW 24, PG 25.
- Longest turn: 2 plays (PW in rounds 1 and 2, PG in round 5: Perseverance, Urgency).
- Decided: Impartiality (odd) in round 3 (9 against 0), PG's Resolve, Determination, Contentment and Joy in round 4 (20), round 5 by one point.

**Game 565.** PG (P1, seat 0) against PW (second tester, seat 1); PW went first. PG won 3 to 1.
- Scores: PG 1, PW 3; PG 7, PW 6; PG 8, PW 6; PG 18, PW 11.
- Longest turn: 2 plays (PG in round 3: Nostalgia, Urgency).
- Decided: Vitality and Maturity (2, 4, 6) in rounds 2 to 4; Impartiality suppressed Vitality and Urgency in round 3.

**Game 566.** PW (P1, seat 0) against PG (bot, seat 1); PG went first. PW won 3 to 1.
- Scores: PW 8, PG 3; PW 14, PG 8; PW 20, PG 23; PW 19, PG 5.
- Longest turn: 3 plays (PW in round 1: Modesty, Familiarity, Solidarity).
- Decided: PW's three-play first turn (8 against 3), PG's Resolve and Vitality in round 3 (23), Impartiality (odd) in round 4 (19 against 5).

### Notes by card (PW against PG)

| Card | What the games showed |
|---|---|
| Impartiality | Odd: suppressed Resolve, Determination and Contentment (564, 9 against 0) and Vitality, Joy, Kinship and Resolve (566, 19 against 5); did nothing when played first in 563. |
| Fulfillment | Not drawn in four games. |
| Orderliness | Played in 563 and 566 (even); held in 565; not drawn in 564. |
| Vitality | +2 each turn, still worked when suppressed (565 round 3). |
| Maturity | First play (565): 2, 4, 6 with Vitality; not touched by odd suppression. |
| Honesty | A 6 on turn one (563). |
| Resolve, Determination | 6s from round 2 (564); suppressed by Impartiality. |
| Urgency | A 6 in 564 round 5 (two plays); suppressed in 565 round 3. |
| Modesty, Familiarity, Solidarity chain | 8 against 3 (566 round 1). |
| Equanimity | A 6 in 566 (four even moods); suppressed by PW's own Impartiality in round 4. |
| Pacifism | Suppressed Restlessness (565 round 4). |

## Session 3e: PU Blue Reverie engine against PB Black Neglect pressure (6 games)

**Source.** The simulator exports of games 567 to 572 (10 November), the fifth Power Duel pairing (15 cards, one mythic). The first tester (P1) played PB in 567, 569 and 571 and PU in 568, 570 and 572. The other seat was a practice bot (PU) in 567 and 571, a
practice bot (PB) in 570 and 572, and the second tester in 568 (PB) and 569 (PU). PU is the blue Reverie deck; PB is the black Neglect deck.

### Summary

| | |
|---|---|
| Result | **PB won 4 of 6** (567, 568, 569 and 570); PU won 571 (3 to 0, against P1's PB) and 572 (3 to 2, against the PB bot). Rounds: PB 14, PU 12. |
| Scores by round, PU | 567: 5, 7, 10, 14. 568: 2, 8, 9, 6, 9. 569: 6, 8, 9, 11. 570: 3, 8, 8, 9, 11. 571: 6, 8, 5. 572: 6, 7, 10, 12, 15. |
| Scores by round, PB | 567: 3, 9, 14, 14. 568: 2, 2, 7, 9, 10. 569: 3, 11, 13, 15. 570: 2, 8, 11, 16, 14. 571: 1, 3, 5. 572: 5, 11, 11, 5, 8. |
| Game length | 3 to 5 rounds, 4.3 on average. |
| Biggest turn | 2 plays (PU almost every turn, from Impulse; PB in 568 round 3 and 570 round 4, from Remorse). Highest scores: PB 16 (570 round 4), PU 15 (572 round 5). |

### Insights

1. **PU's Impulse engine empties its own hand, and Neglect punishes that.** Impulse (a 2 that returns to hand after scoring) gave PU two plays a turn in 567 and 568 and, with Rapport as the extra play, left it with no cards at scoring. Neglect fired twice: in 568 round 4 PU had played Impulse and Rapport with nothing left, and Neglect removed
   Resignation (a 6): 6 against 9, and PB won the game 10 to 9 in round 5. In 571 round 3 the PU bot had played Fear and passed with no cards: Neglect removed Desperation and the score was 5 to 5. Impulse is still in play at the before-scoring trigger, so the engine itself leaves the hand empty.
2. **Neglect was seen in five of six games but played in two.** PB held it unplayed in 569 (PU's hand held two cards), 572 (the PB bot never played it; it passed twice and ended with four cards in hand) and 567 round 4 (see 3). Played, it removed Resignation (568) and Desperation (571). When PU has cards in hand it is just a 2.
3. **PB's Longing recursion was the smartest line.** In 567 round 4 PB discarded Neglect to Longing and took Hate and Neglect back from the pile, so Longing drew two cards for one. PU's hand was empty that round and Neglect, if played, would have removed Resignation (6) for 13 against 8, but PB won 14 to 14 anyway, and PB won the game 3 to 1.
4. **PB's 5s were the scoring engine again.** Dejection (a black 5) and Resentment (colorless 5) gave 11 and 13 in 569 rounds 2 and 3, and 16 in 570 round 4 (Remorse, then Resentment as the extra play). Composure was a 6 in 570 and 572 because PU keeps few cards in hand (PB scored 11 in 570 round 3 and in 572 rounds 2 and 3). Dejection is symmetric: PU discarded Admiration (567), Elusiveness (569) and Fear (572).
5. **Reverie worked for the first time, and was answered.** In 568 round 1 it put Fear back on the deck and drew Resignation; in 570 rounds 2 and 4 it moved Detachment and Resignation from the pile to the bottom and drew Resignation and Rapport. In 568 round 2 PB's Hate put the Reverie on the bottom of the deck. The engine needs cards in the pile (Nosiness, Dejection and Suspicion fed it), so PB's discard cards help PU.
6. **Deflection decided 572.** It bounced Composure (a 6) in round 4 (12 against 5) and the name lock stopped PB replaying it in round 5. It also bounced Opportunism (571) and Resentment (570). It is PU's best answer to PB's 5s and 6s.
7. **PB's openers are weak.** PB opened with Opportunism (a 1) in 571 (1 against 6) and held five cards at the end (Brooding, Longing, Opportunism, Pettiness, Remorse), as in session 3b. PB's best rounds came after Dejection or Resentment.
8. **The bots played oddly.** The PB bot passed in 572 rounds 3 and 4 with playable cards (Neglect, Opportunism) in hand and ended with four cards; the PU bot played Impulse every turn.

### Questions for the testers

- Game 567 round 4: PB played Longing (discard Neglect, take Hate and Neglect back) instead of Neglect with PU's hand empty. Was the recursion the plan, or did you see that Neglect would have removed Resignation?
- Game 568 round 4: PU played Impulse and Rapport and ended with no cards in hand. Was Neglect's before-scoring check seen, and would you have held a card?
- Game 569: PB held Neglect from round 2 to round 4. Was PU's two-card hand the reason, or did the 5s look better?
- Game 571: PB opened with Opportunism and held five cards. What was the plan for Longing, Remorse and Pettiness?
- Reverie (568, 570): how did it feel when it worked? Was Hate the right answer to it?
- Fun and clarity for Impulse (it returns after scoring), Neglect, Longing and Deflection's name lock.

### Game logs

**Game 567.** PB (P1, seat 0) against PU (bot, seat 1); PB went first. PB won 3 to 1.
- Scores: PB 3, PU 5; PB 9, PU 7; PB 14, PU 10; PB 14, PU 14.
- Longest turn: 2 plays (PU in every round: Impulse and a second mood).
- Decided: Suspicion and Dejection made Schadenfreude a 6 in rounds 2 and 3; Longing recursion in round 4.

**Game 568.** PU (P1, seat 0) against PB (second tester, seat 1); PB went first. PB won 3 to 2.
- Scores: PU 2, PB 2; PU 8, PB 2; PU 9, PB 7; PU 6, PB 9; PU 9, PB 10.
- Longest turn: 2 plays (PU in rounds 2 to 5, PB in round 3).
- Decided: Hate on Reverie (round 2), Neglect on Resignation in round 4 (PU's hand empty), round 5 by one point.

**Game 569.** PB (P1, seat 0) against PU (second tester, seat 1); PU went first. PB won 3 to 1.
- Scores: PB 3, PU 6; PB 11, PU 8; PB 13, PU 9; PB 15, PU 11.
- Longest turn: 1 play every turn.
- Decided: Dejection and Resentment (5s) in rounds 2 and 3; PB held Neglect unplayed.

**Game 570.** PU (P1, seat 0) against PB (bot, seat 1); PU went first. PB won 3 to 2.
- Scores: PU 3, PB 2; PU 8, PB 8; PU 8, PB 11; PU 9, PB 16; PU 11, PB 14.
- Longest turn: 2 plays (PU in round 2, PB in round 4).
- Decided: Reverie and Desperation in round 2, Vengeance on Resignation in round 3, Remorse then Resentment in round 4 (16).

**Game 571.** PB (P1, seat 0) against PU (bot, seat 1); PU went first. PU won 3 to 0.
- Scores: PB 1, PU 6; PB 3, PU 8; PB 5, PU 5.
- Longest turn: 2 plays (PU in round 1: Desperation, Anticipation).
- Decided: Deflection on Opportunism in round 2; Neglect on Desperation in round 3 (5 to 5).

**Game 572.** PU (P1, seat 0) against PB (bot, seat 1); PB went first. PU won 3 to 2.
- Scores: PU 6, PB 5; PU 7, PB 11; PU 10, PB 11; PU 12, PB 5; PU 15, PB 8.
- Longest turn: 1 play every turn (PB passed in rounds 3 and 4).
- Decided: Deflection on Composure in round 4 (12 against 5), Reminiscence in round 5.

### Notes by card (PU against PB)

| Card | What the games showed |
|---|---|
| Neglect | Played in 568 (removed Resignation) and 571 (removed Desperation); held in 567, 569 and 572; fires when Impulse leaves PU's hand empty. |
| Impulse | Two plays and 2 points a turn; leaves the hand empty at scoring. |
| Reverie | Drew in 568 round 1 and 570 rounds 2 and 4; Hate put it on the bottom (568). |
| Deflection | Composure (572, decisive), Opportunism (571), Resentment (570). |
| Dejection, Resentment | 5s that made PB's best rounds (569, 570). |
| Composure | A 6 in 570 and 572. |
| Longing | Discard Neglect, take Hate and Neglect back (567). |
| Hate | Bottomed Reverie (568); discarded and retrieved (567). |
| Resignation | A 6 (572 rounds 1 to 5, 568 round 2); removed by Neglect and Vengeance. |
| Rapport | A double loot in 572 round 3; PU's last card in 568 round 4. |
| Opportunism | Opened with a 1 and bounced (571). |

## Session 3f: PU Blue Reverie engine against PR Ardor red pile (2 games)

**Source.** The simulator exports of games 573 and 574 (10 November), the sixth Power Duel pairing (15 cards, one mythic). The first tester (P1) played PR in 573 and PU in 574. The other seat was a practice bot (PU) in 573 and the second tester (PR) in 574.
Two games is a small sample. PU is the blue Reverie deck; PR is the red Ardor deck (Ardor now counts only the other red moods, Q13).

### Summary

| | |
|---|---|
| Result | **One win each**: PR won 573 (3 to 2, against the PU bot) and PU won 574 (3 to 0, against the second tester's PR). Rounds: PR 3, PU 5. |
| Scores by round, PR | 573: 0, 11, 30, 49, 20. 574: 6, 5, 2. |
| Scores by round, PU | 573: 3, 11, 9, 10, 11. 574: 6, 6, 6. |
| Game length | 5 and 3 rounds. |
| Biggest turn | 2 plays (PR in 573 rounds 2 to 4, PU in 573 round 2). **The highest score of any play test so far: 49 for PR in 573 round 4**, then 30 in round 3. |

### Insights

1. **Ardor scored 30 and 49 in 573, after the change to "other red moods".** In round 3 PR played Shock then Ruthlessness (Adrenaline's extra play) for five red moods and 30 points against PU's 9. In round 4 it played Frenzy then Impatience: six red moods, Ardor +5 on each, Verve's +2 on the Frenzy played that round (Frenzy alone scored 13),
   and Impatience, for 49 against 10. PU, a bot, had no answer: Panic bounced Ruthlessness only in round 5 (PR still scored 20). The change takes a point from each red mood, but a six-mood board with Adrenaline, Verve and Frenzy still makes a score no other deck reaches.
2. **PR's record is all or nothing on Ardor.** PR has won every game in which it played Ardor (560, 561, 573) and lost all five in which it did not (557, 558, 559, 562, and 574, where Ardor sat in hand). Ardor's evidence for Q13: 30 (five red moods), 31 (five), 32 (six), 37 (seven) and 49 (six, with Verve and Frenzy) since the change, against 7 to 18 for the opponent.
   This is the strongest evidence yet that the "other" change is not enough; Q13's option B (one for every two other red moods) or a cap are the next steps. Two of the three wins were against white, which has no removal, and one against a bot.
3. **PU won 574 with one mood and no answer needed.** Resignation (a 6) scored 6 in all three rounds. PR's removal can only reach cheap moods: Rashness took Reflection (a 1) and Shock took Deflection (a 2), but Shock hits moods worth 3 or less, Rashness 1 or less and Belligerence 2 or less, so the 6 was untouchable.
   Detachment (a 5) dodges the red removal the same way, and Anticipation does when it is a 6. Resignation was the only mood left on PU's board, and it won 6 to 6, 6 to 5 and 6 to 2.
4. **PR held its engine in 574.** PR ended with Ardor, Adrenaline, Belligerence and Impatience in hand after three rounds, and played Frenzy, Rashness with Impatience, and Shock. Adrenaline (drawn after round 2) then Ardor would have been a free play, but Ardor with two or three red moods is small. PU's answers (Deflection bouncing Impatience, a 5) cost PR a turn.
5. **Adrenaline was a turn-one 0 again (573 round 1: 0 against 3).** It then gave PR a free extra play in rounds 2 to 4. As in sessions 3c and 3e, PR's early rounds are weak and its late rounds decide the game.
6. **PU's bot declined Rumination twice (573 rounds 4 and 5) and played Panic only in round 5.** Rumination plus Panic would have bounced PR's Shock and Ruthlessness every turn; this is the line the session 3a notes asked the testers about.

### Questions for the testers

- Game 573: Ardor with six red moods scored 49 (and 30 with five). Does a round that large feel right after the "other red moods" change, or is Ardor still too fast? Which of the Q13 fallbacks would you pick (one for every two other red moods, or a cap)?
- Game 574: PR held Ardor and Adrenaline for three rounds. Was waiting for more red moods the plan, or did you not see a good play? Would Adrenaline then Ardor have been worth it?
- Game 574: Resignation, a 6, was out of reach of red's removal. Is that a problem for red, or a fair reward for PU's 6-cost play (it needs a card put on the bottom of the deck)?
- Fun and clarity for Ardor (and Verve's +2 on each red mood played this round) and Frenzy.

### Game logs

**Game 573.** PR (P1, seat 0) against PU (bot, seat 1); PR went first. PR won 3 to 2.
- Scores: PR 0, PU 3; PR 11, PU 11; PR 30, PU 9; PR 49, PU 10; PR 20, PU 11.
- Longest turn: 2 plays (PU in round 2: Desperation, Detachment; PR in rounds 2 to 4: Ardor then Verve, Shock then Ruthlessness, Frenzy then Impatience).
- Decided: Ardor with five red moods (30) in round 3, with six and Verve's bonus (49) in round 4.

**Game 574.** PU (P1, seat 0) against PR (second tester, seat 1); PU went first. PU won 3 to 0.
- Scores: PU 6, PR 6; PU 6, PR 5; PU 6, PR 2.
- Longest turn: 2 plays (PR in round 2: Rashness, Impatience).
- Decided: Resignation (a 6) untouched by red's removal; Deflection on Impatience in round 3; PR held Ardor and Adrenaline.

### Notes by card (PU against PR)

| Card | What the games showed |
|---|---|
| Ardor | 30 (five red) and 49 (six red, Verve, Frenzy) in 573; held unplayed in 574. PR is 3 to 0 when it plays Ardor and 0 to 5 when it does not. |
| Adrenaline | A turn-one 0 (573); a free extra play in rounds 2 to 4. |
| Verve | +2 on each red mood played that round: Frenzy scored 13 in 573 round 4. |
| Frenzy | 6 or more, discarded after scoring as written. |
| Shock, Rashness | Killed Reminiscence, Deflection and Reflection; cannot reach Resignation, Detachment or a 6. |
| Resignation | A 6 in all three rounds of 574; out of reach of red's removal. |
| Deflection | Bounced Impatience (574) and then died to Shock. |
| Panic | Bounced Ruthlessness in 573 round 5 only. |
| Rumination | Declined twice (573). |

## Session 3g: PU Blue Reverie engine against PG Green Fulfillment anthems (4 games)

**Source.** The simulator exports of games 575, 577, 578 and 579 (10 and 11 November), the seventh Power Duel pairing (15 cards, one mythic). The zip also held game 576, an unrelated one-round game ("Discard Midrange" against "G Green anthems", no plays, over in 26 seconds), which is left out.
The first tester (P1) played PG in 575 and 578 and PU in 577 and 579. The other seat was a practice bot (PU) in 575 and 578 and the second tester (PG) in 577 and 579. PU is the blue Reverie deck; PG is the green Fulfillment deck.

### Summary

| | |
|---|---|
| Result | **PG won 3 of 4** (575, 577 and 578, each 3 to 2); PU won 579 (3 to 1). Rounds: PG 10, PU 9. |
| Scores by round, PG | 575: 6, 2, 4, 14, 17. 577: 3, 6, 16, 27, 40. 578: 2, 9, 17, 23, 41. 579: 6, 4, 4, 6. |
| Scores by round, PU | 575: 2, 3, 8, 11, 14. 577: 5, 10, 13, 19, 20. 578: 6, 11, 14, 20, 21. 579: 3, 5, 6, 6. |
| Game length | 5, 5, 5 and 4 rounds, 4.75 on average. |
| Biggest turn | 2 plays (PU in every round of 577 from Impulse, and in 578 round 4 and 579 round 4; PG in 577 round 3). **Highest scores: PG 41 (578 round 5) and 40 (577 round 5), both with Fulfillment.** |

### Insights

1. **PU led early and PG overtook it in rounds 4 and 5.** PU won rounds 1 and 2 in 577 and 578 (5 and 10, 6 and 11) and had the better board until round 3. PG scored 2 to 9 early and 17 to 41 late: Maturity grows 2 each turn, and Fulfillment makes each mood of 6 or more score twice. In 577 round 4 PG scored 27 and in round 5 40 (PU 19 and 20); in 578 round 5 PG scored 41
   against 21 with Maturity at 10, Vindication at 6 and Fulfillment played that round. The PG wins were decided in rounds 4 and 5.
2. **Fulfillment with Maturity reaches the same scores as Ardor, one or two rounds later.** 40 and 41 in round 5 are close to the Ardor rounds (30 to 49 in rounds 3 and 4, session 3f). The difference is time: Maturity needs about four turns to pass 6, so PG is behind until round 4. It is a slower shape than Ardor, and the first time Fulfillment has been drawn in the Power Duel games (it did not appear in session 3d).
3. **PU's engine scored but could not catch up.** In 577 the PU player played Impulse and a second mood every turn (5, 10, 13, 19, 20 points); PU's moods are worth 2 to 6 each, so it grows by one mood a round. The PU bots mostly played one mood a turn (575, 578) and never answered Maturity or Fulfillment, although Panic (575 round 2) bounced Honesty once.
4. **The one PU win was a tempo lock (579).** PU bounced PG's only mood every round: Deflection on Honesty (round 2), Panic on Vindication (round 3), and Fear to take Deflection back into hand and play it again on Vindication (round 4). PG scored 6, 4, 4 and 6 and ended with six cards in hand (Kinship, Maturity, Nostalgia, Restlessness, Vindication, Vitality)
   and one mood in play, while PU scored 3, 5, 6 and 6 and won three rounds. Bounce plus Deflection's name lock beats a deck that plays one mood a turn.
5. **Honesty was a 6 on turn one again** (575 and 579 round 1: 6 against 2 and 3), but PG's openers are weak in the long run: bounce takes it back (Panic in 575, Deflection in 579) and it must be played again, revealing the hand again.
6. **Reverie did nothing again.** It was played once as the first play with an empty pile (575 round 1: 2 points, no draw) and was in PU's hand at the end of 579. Rapport and Impulse carried the draw engine in 577.

### Questions for the testers

- Game 579: PG held six cards and replayed the bounced mood each round. Was replaying Honesty or Vindication the plan, or did the name lock leave no other play? Maturity, Vitality or Restlessness would have started the growth. What would you play against a bounce lock?
- Game 577: PU put Panic on the bottom of the deck with Rapport in round 1 and never bounced PG's board; PG scored 27 and 40. Was bounce held back for a reason, and could PU have answered Maturity and Fulfillment in time?
- Fulfillment and Maturity at 40 and 41 in round 5 (with PG behind until round 4): is that the right shape for a mythic anthem, or too much? It was reached against bot or no-answer boards in 577 and 578.
- Fun and clarity for Maturity (permanent growth), Fulfillment and Deflection's name lock.

### Game logs

**Game 575.** PG (P1, seat 0) against PU (bot, seat 1); PU went first. PG won 3 to 2.
- Scores: PG 6, PU 2; PG 2, PU 3; PG 4, PU 8; PG 14, PU 11; PG 17, PU 14.
- Longest turn: 1 play every turn.
- Decided: Honesty as a 6 and again after Panic bounced it (round 4), Maturity and Vitality in the last two rounds.

**Game 577.** PU (P1, seat 0) against PG (second tester, seat 1); PU went first. PG won 3 to 2.
- Scores: PU 5, PG 3; PU 10, PG 6; PU 13, PG 16; PU 19, PG 27; PU 20, PG 40.
- Longest turn: 2 plays (PU every round: Impulse and Rapport, Detachment, Reminiscence, Resignation, Admiration; PG in round 3: Kinship, Maturity).
- Decided: Fulfillment with Maturity in rounds 4 and 5 (27 and 40).

**Game 578.** PG (P1, seat 0) against PU (bot, seat 1); PG went first. PG won 3 to 2.
- Scores: PG 2, PU 6; PG 9, PU 11; PG 17, PU 14; PG 23, PU 20; PG 41, PU 21.
- Longest turn: 2 plays (PU in round 4: Desperation, Reminiscence).
- Decided: Maturity played in round 1 and never answered (2 to 10), Resolve as a 6 in rounds 3 and 4, Fulfillment in round 5 (41).

**Game 579.** PU (P1, seat 0) against PG (second tester, seat 1); PU went first. PU won 3 to 1.
- Scores: PU 3, PG 6; PU 5, PG 4; PU 6, PG 4; PU 6, PG 6.
- Longest turn: 2 plays (PU in round 4: Fear, Deflection).
- Hands: PG held six cards at the end with one mood in play.
- Decided: the bounce lock (Deflection, Panic, Fear then Deflection again).

### Notes by card (PU against PG)

| Card | What the games showed |
|---|---|
| Fulfillment | Played in 577 and 578 (rounds 4 and 5): 27, 40 and 41. First time drawn in a Power Duel game. |
| Maturity | Grew to 10 by round 5 in 578 and was never answered; part of the 40 and 41. |
| Honesty | A 6 on turn one (575, 579); bounced and replayed. |
| Resolve, Vindication | 6s in rounds 3 to 5 of 578. |
| Deflection | Bounce plus name lock on Honesty and Vindication (579); won the game. |
| Panic | Bounced Honesty (575) and Vindication (579); put on the bottom by Rapport in 577. |
| Fear | Returned Deflection to hand to play it again (579 round 4). |
| Impulse | Two plays a turn in 577 (5, 10, 13, 19, 20). |
| Reverie | Played with an empty pile (575 round 1); held at the end of 579. |
| Rumination | In play as a 1 (575, 578); no use. |

## Session 3h: PB Black Neglect pressure against PR Ardor red pile (5 games)

**Source.** The simulator exports of games 581 to 585 (10 and 11 November; game 580 is not in the zip), the eighth Power Duel pairing (15 cards, one mythic). The first tester (P1) played PR in 581, 583 and 585 and PB in 582 and 584. The other seat was a practice bot (PB) in 581 and 585 and the second tester in the other three games
(PB in 583, PR in 582 and 584). PB is the black Neglect deck; PR is the red Ardor deck (Ardor counts the other red moods, Q13).

### Summary

| | |
|---|---|
| Result | **PB won all five** (581, 583 and 585 against P1's PR; 582 and 584 as P1's PB), each 3 to 1 in rounds except 584 (3 to 2). Rounds: PB 15, PR 6. |
| Scores by round, PB | 581: 3, 8, 2, 5. 582: 3, 8, 13, 14. 583: 5, 10, 13, 16. 584: 3, 6, 11, 11, 16. 585: 0, 3, 6, 6. |
| Scores by round, PR | 581: 0, 5, 3, 3. 582: 3, 8, 14, 11. 583: 0, 12, 2, 13. 584: 5, 5, 7, 12, 12. 585: 2, 0, 5, 5. |
| Game length | 4, 4, 4, 5 and 4 rounds, 4.2 on average. |
| Biggest turn | 2 plays (PB in 581 round 2 and 585 round 3, from Remorse; PR in 581 rounds 2 and 3, 583 round 2, 584 rounds 1 and 4). Highest scores: PB 16 (583 round 4, 584 round 5), PR 14 (582 round 3). |

### Insights

1. **PB's cheap removal kept PR's engine from building, and Ardor never snowballed.** Ardor appeared in two games (583 and 585): PR scored 12 and 13 in 583 (rounds 2 and 4, with three red moods) and 0 to 5 in 585. Vengeance removed PR's highest mood each time (Exuberance in 583 round 3 and 584 round 2, Shock in 585 round 2), Hate bottomed Impatience (581) and Zeal (585), and Suspicion and Nosiness made PR discard Adrenaline (584), Belligerence (581),
   Rashness (582) and Zeal (583). In both games PR never had more than three red moods in play, so Ardor stayed small. Together with session 3f this makes PR 3 to 2 when it plays Ardor: it won against white and a blue bot, and lost both games against black.
2. **This is evidence for Q14 that the current Ardor text may be fine.** Q14's suggested path was to play PB against PR before changing Ardor. Here Ardor games reached 13 at most, so the 30 to 49 rounds depend on the opponent having no cheap removal. The PR against PG pairing is still unplayed.
3. **PR's hand ran dry.** PR passed or had no cards to play in 581 (rounds 2 and 4), 583 (rounds 3 and 4) and 584 (round 5, an automated pass), with Adrenaline's extra plays unused. FOMO and Zeal cost cards (FOMO's cost was Zeal in 581 and Shock in 583), and PB's Suspicion and Nosiness take more.
4. **PB's 5s were its scoring again.** Dejection and Resentment gave PB 8, 13 and 14 in 582, 10, 13 and 16 in 583, and 11 and 16 in 584 with three or four moods. Schadenfreude was a 6 in 581 round 2 (Nosiness made PR discard).
5. **The black testers discarded Neglect to Dejection again (583 round 1).** This is the third game (with 554 and 567 round 4 via Longing). Neglect was never played in these five games (held in 581's hand at the end, discarded in 583), although PR's hand was empty in several rounds, where it would have removed PR's best mood.
6. **The best PR line was the FOMO sacrifice (581 round 3).** PR played FOMO (a 7, paying Zeal), then Vindictiveness with Adrenaline's extra play: it put FOMO into the pile and removed Schadenfreude (lower value), winning the round 3 to 2. FOMO again acted as a cost, not as a 7 that stayed.
7. **Rashness and Shock handled PB's small moods.** Rashness removed Remorse (581) and Opportunism (584), and Shock removed Longing (585 round 1). PB's moods are cheap, which red's removal can reach, but each removal cost PB only a small mood and PB just played the next card.
8. **The PB bot played well:** it used Vengeance and Hate on PR's best mood each time, and Remorse then Schadenfreude for a free 6.

### Questions for the testers

- Game 583 round 1: PB discarded Neglect to Dejection. Was it the weakest card in hand? This has happened in 554, 567 and now 583: is Neglect hard to build a plan around, or just worth less than the other cards?
- Game 585: PR held Belligerence, Composure, Ruthlessness and Vindictiveness at the end, and played Ardor alone in round 2 into Vengeance. What was the plan, and would Adrenaline have changed it?
- Game 581 round 3: the FOMO then Vindictiveness line. Was it planned?
- Does PB's mix of Suspicion, Nosiness, Vengeance and Hate feel too good against red? Should red have a way to rebuild after losing its engine cards?
- Fun and clarity for Vengeance (the opponent chooses among its highest moods) and Hate.

### Game logs

**Game 581.** PR (P1, seat 0) against PB (bot, seat 1); PR went first. PB won 3 to 1.
- Scores: PR 0, PB 3; PR 5, PB 8; PR 3, PB 2; PR 3, PB 5.
- Longest turn: 2 plays (PB in round 2: Remorse, Nosiness; PR in rounds 2 and 3).
- Hands: PR passed in rounds 2 and 4 with extra plays unused.
- Decided: Remorse then Nosiness then Schadenfreude as a 6 in round 2; PR's FOMO then Vindictiveness in round 3 (3 to 2).

**Game 582.** PB (P1, seat 0) against PR (second tester, seat 1); PB went first. PB won 3 to 1.
- Scores: PB 3, PR 3; PB 8, PR 8; PB 13, PR 14; PB 14, PR 11.
- Longest turn: 1 play every turn.
- Decided: Dejection and Resentment (5s) in rounds 2 and 3; PR won round 3 with Frenzy.

**Game 583.** PR (P1, seat 0) against PB (second tester, seat 1); PB went first. PB won 3 to 1.
- Scores: PR 0, PB 5; PR 12, PB 10; PR 2, PB 13; PR 13, PB 16.
- Longest turn: 2 plays (PR in round 2: Ardor, Exuberance).
- Decided: Dejection (PB discarded Neglect) in round 1; Vengeance on Exuberance in round 3 (2 to 13).

**Game 584.** PB (P1, seat 0) against PR (second tester, seat 1); PR went first. PB won 3 to 2.
- Scores: PB 3, PR 5; PB 6, PR 5; PB 11, PR 7; PB 11, PR 12; PB 16, PR 12.
- Longest turn: 2 plays (PR in rounds 1 and 4).
- Decided: Suspicion on Adrenaline (round 1), Vengeance on Exuberance (round 2), Dejection in round 5 against PR's empty hand.

**Game 585.** PR (P1, seat 0) against PB (bot, seat 1); PB went first. PB won 3 to 1.
- Scores: PR 2, PB 0; PR 0, PB 3; PR 5, PB 6; PR 5, PB 6.
- Longest turn: 2 plays (PB in round 3: Remorse, Schadenfreude).
- Decided: Vengeance on Shock in round 2 (Ardor alone was a 0), Hate on Zeal in round 4.

### Notes by card (PB against PR)

| Card | What the games showed |
|---|---|
| Vengeance | Removed Exuberance (583, 584) and Shock (585); the answer to PR's best mood each time. |
| Hate | Bottomed Impatience (581) and Zeal (585). |
| Suspicion, Nosiness | Made PR discard Adrenaline, Rashness, Belligerence and Zeal. |
| Dejection, Resentment | 5s that gave PB 8 to 16 with three or four moods. |
| Neglect | Never played; discarded to Dejection (583), held (581). |
| Schadenfreude | A 6 in 581 round 2 and in 585 round 3 (a 3 elsewhere). |
| Remorse | Free extra play (581, 585); Rashness removed it once. |
| Ardor | 12 in 583 round 2, 0 to 1 in 585; never reached three red moods. |
| Adrenaline | A turn-one 0 (581, 583); discarded by Suspicion (584). |
| FOMO | A cost again; FOMO then Vindictiveness won 581 round 3. |
| Rashness, Shock | Removed Remorse, Opportunism and Longing. |
| Vindictiveness | Removed FOMO and Schadenfreude (581 round 3). |

## Session 3i: PB Black Neglect pressure against PG Green Fulfillment anthems (5 games)

**Source.** The simulator exports of games 586 to 590 (11 November), the ninth Power Duel pairing (15 cards, one mythic). The first tester (P1) played PG in 586, 588 and 590 and PB in 587 and 589. The other seat was a practice bot (PB) in 586 and the second tester in the other four games
(PG in 587 and 589, PB in 588 and 590). PB is the black Neglect deck; PG is the green Fulfillment deck.

### Summary

| | |
|---|---|
| Result | **PG won 3 of 5** (586 against the PB bot, 3 to 1; 587, 3 to 2; 588, 3 to 0); PB won 589 (3 to 2) and 590 (3 to 0). Rounds: PG 11, PB 9. |
| Scores by round, PG | 586: 3, 13, 15, 24. 587: 5, 5, 9, 14, 23. 588: 5, 6, 12. 589: 0, 2, 7, 12, 12. 590: 0, 2, 7. |
| Scores by round, PB | 586: 3, 6, 11, 14. 587: 3, 6, 11, 12, 18. 588: 3, 6, 11. 589: 0, 5, 8, 9, 15. 590: 3, 8, 11. |
| Game length | 4, 5, 3, 5 and 3 rounds, 4.0 on average. |
| Biggest turn | 2 plays (PG in 586 round 2, 587 round 1, 588 rounds 1 and 3; PB in 588 round 3, from Remorse). Highest scores: PG 24 (586 round 4) and 23 (587 round 5); PB 18 (587 round 5). |

### Insights

1. **PB answered PG's first good mood almost every time.** Vengeance (587 round 2, 588 round 2, 589 round 5, 590 round 1) removed Determination, Vindication, Restlessness and Honesty, and Hate bottomed Determination in 589 round 1. PG's Determination and Honesty never scored in these games.
   PG won when it had three or more moods before the removal arrived (586: 13 in round 2 with Resolve a 6, Joy and Kinship; 24 in round 4 with five moods) and lost when its first mood was removed (589 and 590 round 1, then 2 in round 2 of both: 0, 2, 7 in 590). PB's own curve was nearly the same in three games (3, 6, 11 in 586, 587 and 588).
2. **Fulfillment decided the one game where it ran, but it ran once.** It was in play only in 587 round 5: PG scored 23 against 18, of which Fulfillment itself was 1 and the extra score of Vindication (a 6) was 6; without it PG would have had 17 against 18 and lost the game. It was discarded by the bot's Nosiness in 586 (the bot picked it out of a two-card hand), and stayed in the deck in 588, 589 and 590. It is the same as session 3d: a mythic seen in about half the games.
3. **The shared discard pile works for black as recursion.** In 587 round 5 Brooding took PG's Determination (removed by Vengeance in round 2) back to PB's hand, and PB played it as a 6 (Suspicion, Vengeance and Brooding make three black moods); in 590 round 3 Longing discarded Composure and took PG's Honesty and Determination, one removed by Vengeance and one discarded to Dejection. PB's removal feeds its recursion with the opponent's best cards.
   The game ended before PB could play them in 590, and PB lost round 5 in 587 anyway (18 to 23).
4. **Suspicion helped PG twice.** In 587 and 588 round 1 PB played Suspicion, and PG discarded a 2 (Perseverance, Vindication) and replayed it from the pile with Thrift (a 0 to 3 card from the discard pile) in the same turn: 5 against 3 both times. Suspicion against a Thrift deck gave it a free play.
5. **Neglect was never played, and it had two chances.** It was in PB's hand at the end of 586 (bot), 587, 588 and 589, and in the deck in 590. PG's hand was empty before scoring only in the last round of 586 (round 4, 14 to 24) and 588 (round 3). The tester in 588 played Remorse and Dejection that round; with Neglect in place of Dejection PB would have had 8 and PG 8 after losing a 4-point mood (Joy or Thrift), a tie that the first player (PG) wins. So Neglect would not have changed the result.
   PG's hand was 1 to 5 cards through the rest of the games: PG plays one card a turn and draws only when it loses a round, so it keeps cards. This repeats session 3h (Neglect never played against PR either) and matches session 3b: Neglect fires against engine decks that empty their hand, not against a deck that plays one mood a turn.
6. **Martyrdom worked with a free sacrifice (589 round 5).** PB sacrificed Hate (a 0) at the start of its turn, PG discarded Vitality, and Vengeance on Restlessness gave PB 15 against 12 and the game. Martyrdom is a good card for black when it has a 0 to feed it. Pettiness was never played (held in 586 and 587).
7. **PG's Joy extra plays gave it bursts.** Joy's extra play next turn gave two plays in 586 round 2 (Resolve, Kinship: 13 against 6) and 588 round 3 (Kinship, Vitality: but Vitality's start-of-turn trigger had already passed, so it did nothing that round). Kinship is a 1 that adds 1 to each green mood, so it needs a third green mood.
8. **590 was PG's weakest game.** It played Honesty (revealing four cards), Maturity and Joy in three turns, and ended with Kinship, Perseverance and Vindication in hand, because the one play a turn left them unplayed. PB won with Vengeance, Dejection and Longing (a 3-play game).
9. **The PB bot played well in 586.** Nosiness took Fulfillment out of PG's hand; it never played Neglect, Martyrdom or Pettiness (it held them to the end).

### Questions for the testers

- Games 587 and 588 round 1: after Suspicion, did you discard Perseverance / Vindication on purpose to replay it with Thrift? Is the interaction fun, or does Suspicion feel bad against Thrift?
- Game 587: Fulfillment was drawn after round 2 and played in round 5. Was it waiting for more 6s, or did the other plays look better? Did Fulfillment feel strong when it ran?
- Games 587 to 589: Neglect was held. Did you see the PG hand sizes (3 to 5 cards) as a reason not to play it? Is there a deck where you would play it on turn one?
- Game 588 round 3: Remorse then Dejection when PG's hand was empty. Was Neglect considered?
- Game 589 rounds 1 to 3: PG played Determination into Hate, then low moods. Was the plan to play the 6s later?
- Game 590 round 3: Longing took Honesty and Determination. Did taking the opponent's cards from the pile feel good? Is "black recursion from the shared pile" something you want more or less of?
- Pettiness (a missed turn for a player) was never played. Is it unplayable, or just not drawn at the right time?
- Fun and clarity for Brooding and Longing taking the opponent's cards, and Martyrdom.

### Game logs

**Game 586.** PG (P1, seat 0) against PB (bot, seat 1). PG won 3 to 1.
- Scores: PG 3, PB 3; PG 13, PB 6; PG 15, PB 11; PG 24, PB 14.
- Longest turn: 2 plays (PG in round 2: Resolve, Kinship with Joy's extra play).
- Hands: PG's hand was empty at the end; PB ended with Martyrdom, Neglect and Pettiness.
- Decided: Nosiness took Fulfillment in round 3; Resolve a 6 in round 2 (13 to 6); PG's five moods in round 4 (24 to 14).

**Game 587.** PB (P1, seat 0) against PG (second tester, seat 1). PG won 3 to 2.
- Scores: PB 3, PG 5; PB 6, PG 5; PB 11, PG 9; PB 12, PG 14; PB 18, PG 23.
- Longest turn: 2 plays (PG in round 1: Thrift, then Perseverance from the discard pile).
- Decided: Suspicion into Thrift in round 1; Vengeance on Determination in round 2 (6 to 5); Fulfillment in round 5 (23 to 18) against PB's Brooding then Determination from the pile.

**Game 588.** PG (P1, seat 0) against PB (second tester, seat 1). PG won 3 to 0.
- Scores: PG 5, PB 3; PG 6, PB 6; PG 12, PB 11.
- Longest turn: 2 plays (PG in rounds 1 and 3; PB in round 3: Remorse, Dejection).
- Decided: Suspicion into Thrift in round 1; Vengeance on Vindication in round 2 (6 to 6, PG went first); round 3 by one point, with PG's hand empty and Neglect held.

**Game 589.** PB (P1, seat 0) against PG (second tester, seat 1). PB won 3 to 2.
- Scores: PB 0, PG 0; PB 5, PG 2; PB 8, PG 7; PB 9, PG 12; PB 15, PG 12.
- Longest turn: 1 play every turn.
- Decided: Hate on Determination in round 1 (0 to 0); Martyrdom (sacrificing Hate) and Vengeance on Restlessness in round 5.

**Game 590.** PG (P1, seat 0) against PB (second tester, seat 1). PB won 3 to 0.
- Scores: PG 0, PB 3; PG 2, PB 8; PG 7, PB 11.
- Longest turn: 1 play every turn.
- Decided: Vengeance on Honesty in round 1; Dejection in round 2 (PG discarded Determination); Longing in round 3 took Honesty and Determination from the pile.

### Notes by card (PB against PG)

| Card | What the games showed |
|---|---|
| Vengeance | Removed Determination, Vindication, Restlessness and Honesty (587, 588, 589, 590); the answer to PG's first good mood. |
| Hate | Bottomed Determination (589 round 1); sacrificed to Martyrdom (589 round 5). |
| Suspicion | Gave PG a free replay with Thrift in 587 and 588 round 1. |
| Nosiness | The bot took Fulfillment from PG's hand (586 round 3). |
| Dejection | A 5 (588, 590); PG's hand was already empty in 588 round 3. |
| Brooding, Longing | Took PG's removed Determination (587 round 5) and Honesty and Determination (590 round 3) back from the shared pile. |
| Martyrdom | Worked in 589 round 5 with Hate as the sacrifice. |
| Neglect | Never played (held in four games, in the deck in one); PG's hand was empty only in the last round of 586 and 588. |
| Pettiness | Never played (held in 586 and 587). |
| Remorse | Free extra play (588 round 3); put PG's Vindication on the bottom of PG's deck. |
| Fulfillment | Played once (587 round 5, 23 to 18); discarded by Nosiness in 586. |
| Thrift | Replayed Perseverance and Vindication (a 2 each) from the pile in 587 and 588 round 1. |
| Joy | Extra plays in 586 round 2 and 588 round 3. |
| Vitality | Played as an extra play in 588 round 3, after its trigger: no effect that round. |
| Resolve, Restlessness | 6s in 586 (rounds 2 and 4). |
| Determination, Honesty | Removed each time they were played (587, 589, 590). |

## Session 3j: PR Ardor red pile against PG Green Fulfillment anthems (2 games)

**Source.** The simulator exports of games 591 and 592 (11 November), the tenth and last Power Duel pairing (15 cards, one mythic). The first tester (P1) played PG in 591 and PR in 592; the other seat was a practice bot in both games (PR in 591, PG in 592).
PR is the red Ardor deck (Ardor counts the other red moods, Q13); PG is the green Fulfillment deck.

### Summary

| | |
|---|---|
| Result | **One win each**: PG won 591 (3 to 2, P1 against the PR bot) and PR won 592 (3 to 2, P1 against the PG bot). Rounds: PR 5, PG 5. |
| Scores by round, PG | 591: 0, 2, 13, 20, 18. 592: 3, 6, 6, 13, 17. |
| Scores by round, PR | 591: 2, 7, 10, 16, 16. 592: 3, 5, 11, 11, 22. |
| Game length | 5 and 5 rounds, 5.0 on average. |
| Biggest turn | 2 plays (PG in 591 round 3, from Thrift; PR in 592 round 5, from Adrenaline). Highest scores: PR 22 (592 round 5), PG 20 (591 round 4). |

### Insights

1. **Neither mythic was drawn, so Q14 got no new data.** Ardor and Fulfillment stayed in the deck in both games (Maturity and Vitality too in 591). PR is now 3 to 2 in the five Power Duel games where it played Ardor (560, 561, 573 won; 583, 585 lost) and 1 to 9 in the ten where it did not.
   The one win without it is this session's 592. The question "does Ardor still break games against a deck with no removal in it" is still open: PG has no answers to red moods, so it is the pairing that matters most.
2. **PR's chain won 592 without Ardor.** In round 5 Adrenaline gave the extra play, and Verve then Frenzy scored 22 against 17: Frenzy was an 8 (6, plus Verve's 2) and Verve a 3, with Exuberance a 6 (Shock, Zeal and Frenzy are red). Frenzy goes to the pile after scoring, so the 8 was a one-round payoff. Zeal had put FOMO on the bottom in round 1 to draw Exuberance; FOMO never came back.
3. **Shock removed PG's first mood in both games.** It hit Honesty (591 round 1, PR 2 against 0) and Restlessness (592 round 2). These are 3s that need a condition (a 6 later), so cheap removal is strong against PG's openings. This supports the Shock choice in the PB splash and the Rashness and Shock lines in the PW and PU splash decks (Q9).
4. **Thrift answered Shock in 591.** In round 3 PG played Thrift and then Honesty again from the discard pile, and Honesty was a 6 with the hand revealed: 13 against 10. As in session 3i (Thrift after Suspicion), Thrift turns a removal spell into a free replay of any 0 to 3 card.
5. **The PR bot's Vindictiveness in 591 round 5 was a 9-point swing.** It put Compulsion (3) into the pile to remove Kinship. Kinship gave each of PG's four other green moods +1 and was itself a 2, and with its +1 PG's values (4, 7 and 7) had three different values, so Restlessness was a 6. By my count PG would have scored about 27; without Kinship it scored 18 against PR's 16, and PG won the game by 2.
   Kinship is a single point of failure for PG's conditional 6s: removing it also takes Restlessness (and Determination) back down.
6. **Compulsion gave PR a dead card (591 round 3).** PG chose Contentment to give away, and PR could not play it without a green mood; PR ended the game holding it. The victim chooses the card, so a colorless gate card of the victim's own color is a free discard. This is how Compulsion works, but it shows it is weak against decks with gate cards.
7. **The bots held their engine cards.** The PG bot (592) held Maturity from round 1 to the end of the game (with Joy), playing Restlessness, Resolve, Urgency, Kinship and Vindication instead, and the PR bot (591) ended with Verve, Zeal and Contentment in hand. Maturity (2, then +2 every turn) would have been a 4 in round 2.
8. **Plain-deck records over all ten pairings:** PB 15 to 7, PG 10 to 5, PW 10 to 11, PU 6 to 11, PR 4 to 11 (all games with the plain lists, bots included, sessions 3a to 3j). PR is weakest mainly because of PB (0 to 5) and PW (2 to 4).
   PG's wins against PB, PW and PU came without it ever being the favorite on removal: green has none, and its best lines were the extra plays (Joy, Thrift) and Kinship.

### Questions for the testers

- Game 591 round 3: you gave away Contentment to Compulsion. Was that on purpose (a card PR could not play)? Did Compulsion feel weak because of it?
- Game 591 round 1: Honesty as the first play went into Shock. Would you open with something else against red?
- Game 591 round 5: did you see Vindictiveness (sacrificing Compulsion) coming? Is Kinship too easy to turn off?
- Game 592 round 1: Zeal put FOMO on the bottom to draw Exuberance. Was that to avoid FOMO's cost?
- Game 592 round 5: was the Adrenaline, Verve, Frenzy line planned? How did Frenzy as an 8 read?
- Neither Ardor nor Fulfillment appeared. Do you want more PR against PG games before deciding Q14?

### Game logs

**Game 591.** PG (P1, seat 0) against PR (bot, seat 1). PG won 3 to 2.
- Scores: PG 0, PR 2; PG 2, PR 7; PG 13, PR 10; PG 20, PR 16; PG 18, PR 16.
- Longest turn: 2 plays (PG in round 3: Thrift, then Honesty from the pile).
- Hands: PG ended with Urgency; PR with Contentment (unplayable), Verve and Zeal.
- Decided: Shock on Honesty (round 1); Compulsion took Contentment and Thrift replayed Honesty as a 6 (round 3, 13 to 10); Vindictiveness on Kinship (round 5, 18 to 16).

**Game 592.** PR (P1, seat 0) against PG (bot, seat 1). PR won 3 to 2.
- Scores: PR 3, PG 3; PR 5, PG 6; PR 11, PG 6; PR 11, PG 13; PR 22, PG 17.
- Longest turn: 2 plays (PR in round 5: Verve, Frenzy with Adrenaline's extra play).
- Hands: PR ended with Rashness; PG with Joy and Maturity (never played).
- Decided: Shock on Restlessness (round 2); Exuberance as a 6 (round 3); Adrenaline, Verve and Frenzy in round 5 (22 to 17).

### Notes by card (PR against PG)

| Card | What the games showed |
|---|---|
| Shock | Removed Honesty (591 round 1) and Restlessness (592 round 2), PG's first mood each time. |
| Thrift | Replayed Honesty from the pile as a 6 (591 round 3). |
| Honesty | A 6 when played from the pile (hand revealed); removed by Shock as the first play. |
| Kinship | +1 to four other green moods in 591; its removal cost PG about 9 points. |
| Vindictiveness | Compulsion (3) for Kinship in 591 round 5. |
| Compulsion | PG gave Contentment (dead for PR). |
| Adrenaline, Verve, Frenzy | 22 in 592 round 5 (Frenzy 8, Verve 3); Frenzy went to the pile after scoring. |
| Exuberance | A 6 with Shock and Zeal in 592 round 3 (11 against 6). |
| Zeal | Put FOMO on the bottom and drew Exuberance (592 round 1). |
| Impatience | A 5 in 591 round 2 (7 against 2). |
| Ardor, FOMO | Not played (in the deck both games). |
| Fulfillment, Maturity, Vitality | Not played (Maturity held by the PG bot in 592). |
| Resolve, Urgency, Perseverance | Resolve a 6 in 592 round 2; Perseverance +2 twice in 591. |

## Session 3k: PW Even numbers splash against PU Reverie discard (2 games)

**Source.** The simulator exports of games 593 and 594 (12 November), the first games of two of the new variant decks (see `design/playtest-decks.md`): **PW Even numbers splash** (white with Rashness, Hate, Determination and Rapport; Reverence as the gate) and **PU Reverie discard** (blue and black, Reverie).
The first tester (P1) played PU in 593 and PW in 594; the other seat was a practice bot in both games (PW in 593, PU in 594).

### Summary

| | |
|---|---|
| Result | **One win each**: PU won 593 (3 to 1, P1 against the PW bot) and PW won 594 (3 to 1, P1 against the PU bot). Rounds: PU 4, PW 4. |
| Scores by round, PU | 593: 0, 8, 8, 10. 594: 5, 0, 11, 13. |
| Scores by round, PW | 593: 2, 7, 8, 6. 594: 2, 8, 14, 14. |
| Game length | 4 and 4 rounds, 4.0 on average. |
| Biggest turn | 2 plays (PW in 593 round 2: Modesty, Equanimity; PW in 594 round 2: Familiarity, Impartiality; the PU bot in 594 round 3: Remorse, Rapport). Highest scores: PW 14 (594 rounds 3 and 4), PU 13 (594 round 4). |

### Insights

1. **Impartiality (odd) is PW's best card against this PU list.** PU's bodies are mostly odd: Suspicion 3, Dejection 5, Detachment 5, Desperation 3, Rapport 3, Schadenfreude 3. In 593 round 1 Impartiality suppressed Suspicion (PU 0 against 2), and in 594 round 2 it suppressed Suspicion and Dejection (PU 0 against 8). PW won both rounds. PU's even cards (Deflection, Nosiness, Impulse, Reverie, Hate, Fear, Remorse) are the ones it misses.
2. **The discard fuel works: Reverie never ran, but the pile was never empty.** Dejection and Suspicion put three cards into the pile by round 3 in both games (593: Solidarity, Rapport, Detachment; 594: Rashness, Desperation, Levity). Reverie stayed in the deck in both games (it is the single mythic, seen in about half the games), so the line "Reverie needs a pile" is still untested with Reverie in play.
3. **PU's hand attack drained PW's small hand, and PW's splash cards were the discards.** PW's hand was 1 card after round 2 (593) and 0 after round 3 (594). The PW cards that went into the pile were Solidarity and Rapport (593) and Rashness and Levity (594), not the white core.
   PW's splash was played once (Determination in 594 round 3, a 6 with three white moods: 14 against 11); Hate and Reverence stayed in the deck and Rapport, Rashness and Levity were discarded.
4. **Deflection's name lock decided 593 round 4.** PU bounced Orderliness (PW's only card in hand), PW could not replay it, played Familiarity and passed with Orderliness in hand: 10 against 6. This is the same lock that answered Temperance in session 3a (546 to 548) and decided 572 in session 3e.
5. **594 was decided by one point (14 to 13) with PW passing in round 4.** PW had no cards in hand and passed; the PU bot played Impulse and then passed with Fear and Nosiness in hand (Nosiness had no target, since PW's hand was empty). PW's three white moods (Orderliness, Familiarity, Impartiality) and Determination scored 14 in rounds 3 and 4.
6. **Orderliness appeared in both games.** In 593 round 3 (even) it raised Modesty and Impartiality (PW 8, a tie with PU's 8, which the first player, PU, won) and was bounced the next round. In 594 it was PW's first play (a 2 into Dejection's 5: PW lost round 1, 2 against 5) and gave Familiarity and Impartiality +1 later.
7. **The PU bot spent round 2 of 594 on a suppressed Suspicion.** It had Dejection in play and PW's Impartiality suppressed both: PU scored 0. Otherwise the bot played well (Dejection first turn for a 5, Remorse then Rapport twice in round 3).

### Questions for the testers

- Game 593 round 1: PU opened with Suspicion (an odd 3) into a PW bot that played Impartiality. Would you open with an even card (Deflection, Nosiness, Impulse) against white?
- Game 593 round 3: Hate on Equanimity (a 3, not yet a 6) instead of waiting for Orderliness. Was Orderliness known to be in PW's hand?
- Game 594 round 1: PW opened with Orderliness alone (a 2) and discarded Rashness to Dejection. What else was in the hand, and why discard Rashness (594 round 1) and Levity (round 2)?
- Game 594 round 4: PW passed with no cards. Would Hate or Reverence have changed the last round if they had been drawn?
- Does Impartiality feel too strong against PU's odd-valued black cards, or is that the point of the card?
- Fun and clarity for Deflection's name lock (593 round 4) and for Rapport's second loot.

### Game logs

**Game 593.** PU (P1, seat 0) against PW (bot, seat 1). PU won 3 to 1.
- Scores: PU 0, PW 2; PU 8, PW 7; PU 8, PW 8; PU 10, PW 6.
- Longest turn: 2 plays (PW in round 2: Modesty, then Equanimity).
- Hands: PW had 1 card after round 2 and ended with Orderliness (blocked by Deflection); PU ended with Rumination and Schadenfreude.
- Decided: Impartiality suppressed Suspicion (round 1); Dejection and Suspicion won round 2 (8 to 7); Hate on Equanimity (round 3, 8 to 8 tie); Deflection on Orderliness (round 4, 10 to 6).

**Game 594.** PW (P1, seat 0) against PU (bot, seat 1). PW won 3 to 1.
- Scores: PW 2, PU 5; PW 8, PU 0; PW 14, PU 11; PW 14, PU 13.
- Longest turn: 2 plays (PW in round 2: Familiarity, Impartiality; the PU bot in round 3: Remorse, Rapport).
- Hands: PW had no cards from round 3 and passed in round 4; PU ended with Fear and Nosiness.
- Decided: Impartiality suppressed Suspicion and Dejection (round 2, 8 to 0); Determination a 6 (round 3, 14 to 11); round 4 by one point.

### Notes by card (PW splash against PU Reverie discard)

| Card | What the games showed |
|---|---|
| Impartiality | Suppressed Suspicion (593 round 1) and Suspicion and Dejection (594 round 2): PW won both rounds. |
| Dejection, Suspicion | PU's 5 and 3 for hand pressure; PW discarded Rapport, Solidarity, Rashness and Levity. Both odd, so Impartiality hits them. |
| Deflection | Bounced Orderliness and locked its name (593 round 4). |
| Orderliness | Even in 593 round 3 (PW 8) and 594; first play alone in 594 (a 2). |
| Determination | A 6 in 594 round 3 (three white moods). |
| Hate | PU's Hate bottomed Equanimity (593 round 3); PW's Hate never drawn. |
| Rashness, Rapport, Levity | Discarded by PW (594, 593, 594). |
| Reverie | Not drawn in either game; the pile held 3 cards by round 3. |
| Remorse, Rapport | The PU bot's round 3 in 594: Remorse then both Rapport loots. |
| Impulse, Nosiness, Fear | The PU bot held Nosiness (no target) and Fear after Impulse in 594 round 4. |
| Equanimity, Modesty | Modesty's extra play carried Equanimity (a 3) in 593 round 2. |

## Session 3l: PW Even numbers splash against PB Neglect splash (6 games)

**Source.** The simulator exports of games 595 to 600 (12 and 13 November), the first games of the PB variant against the PW variant (see `design/playtest-decks.md`): **PW Even numbers splash** (white with Rashness, Hate, Determination and Rapport; Reverence as the gate) and **PB Neglect splash** (black with Resignation, Rashness, Fear and Shock; Brooding and Neglect kept).
The first tester (P1) played PB in 595, 597 and 599 and PW in 596, 598 and 600. The other seat was a practice bot in 595 (PW), 599 (PW) and 600 (PB), and the second tester in the other three games (PB in 596 and 598, PW in 597).

### Summary

| | |
|---|---|
| Result | **PB won 4 of 6** (596 and 598 against P1's PW, 599 as P1's PB, 600 against P1's PW; 3 to 1, 3 to 0, 3 to 2 and 3 to 2); PW won 595 (3 to 2, the bot against P1's PB) and 597 (3 to 1, against P1's PB). Rounds: PB 15, PW 11. |
| Scores by round, PB | 595: 0, 6, 8, 13, 16. 596: 0, 8, 10, 10. 597: 0, 2, 4, 7. 598: 6, 3, 8. 599: 0, 8, 6, 9, 14. 600: 0, 5, 10, 13, 15. |
| Scores by round, PW | 595: 2, 7, 7, 11, 18. 596: 4, 4, 5, 6. 597: 2, 0, 8, 7. 598: 3, 3, 8. 599: 4, 7, 4, 11, 11. 600: 6, 6, 6, 11, 14. |
| Game length | 5, 4, 4, 3, 5 and 5 rounds, 4.3 on average. |
| Biggest turn | 3 plays (PW in 596 round 1, 599 round 4 and 600 round 1; PB in 597 round 2). Highest scores: PW 18 (595 round 5), PB 16 (595 round 5) and 15 (600 round 5), PW 14 (600 round 5). |

### Insights

1. **PW's Impartiality won round 1 in every game it was played, and PB scored 0 in all five.** In 595, 596, 599 and 600 it chose odd and suppressed PB's only mood (Brooding 1, Resentment 5, Suspicion 3, Dejection 5); in 597 it chose even and suppressed Resignation (a 6). PB scored 6 in round 1 only in 598, where PW had no Impartiality.
   PB's moods are mostly odd (Suspicion, Dejection, Resentment, Schadenfreude, Vengeance, Longing, Brooding) and a turn-one play is a single mood, so the parity is always known. This repeats session 3k (PU's odd Suspicion and Dejection). PB still won three of those five games (596, 599, 600), so it is a tempo loss, not a deck-loser.
2. **PB's answers to Impartiality were Shock and Rashness plays.** Shock removed Impartiality in 597 round 2 (PW 0 against 2) and Familiarity (596 round 3, 600 round 5) and Humility (595 round 3). Shock was played in four of the six games and took a PW mood every time, always a cheap white mood (Humility 3, Familiarity 2, Impartiality 2).
   PB's 597 round 2 was the best turn of the session: Rashness removed PW's Hate, Remorse put Hate back on PW's deck and drew Shock, and Shock removed Impartiality.
3. **Both decks' Hate and Rashness decided rounds.** PW's Hate bottomed PB's Resignation twice (597 and 598 round 2) and Resentment (599 round 3); PB's Hate bottomed Determination (600 round 2) and Rapport (596 round 4). In 598 PW's Rashness removed PB's Rashness. PB's Resignation (a 6, even) was a turn-one 6 once (598 round 1, 6 against 3) and was removed or suppressed the other times.
4. **PW's Reverence was stuck in 598 because its early plays were not white.** PW played Levity (bottomed for a card), Determination, Hate and Rashness in rounds 1 to 3 (no white mood in play until Humility in round 3) and ended with Reverence, Equanimity, Rapport and Discernment in hand (4 cards, lost 8 to 8, a tie that PB, the first player, won).
   With a splash PW's early plays are often not white, and Reverence, Equanimity (even numbers) and the white chain all want white moods in play.
5. **Neglect had targets only in the games where it was not drawn.** PW's hand was empty before scoring in 599 (rounds 4 and 5) and 600 (rounds 2 to 5); Neglect was in the deck both times. In 596 and 597, where PB drew it, PW still had two to five cards. It was played once (597 round 3, a 2 against a hand of three). PW's three-play turns (596 round 1, 599 round 4, 600 round 1) are what empty its hand.
6. **PB's early scores were low.** In 597 PB scored 0, 2, 4 and 7 with Resignation, Rashness, Remorse, Shock, Neglect and Vengeance, and lost 1 to 3 in rounds. Rashness and Remorse print 0, Neglect and Shock 2: PB's splash tempo cards are free plays but not bodies.
7. **Brooding took the opponent's removed mood again.** In 595 round 4 it took PW's Humility (removed by Shock) back to PB's hand, and PB played it as the extra +1 for its 0 to 2 moods: 13 against 11. Nosiness then took Orderliness (PW's mythic) out of PW's hand in round 5, and PW still won 18 to 16 with Equanimity (a 6, four or more even moods).
8. **Orderliness was seen in three games and mattered once.** It was PW's round 4 play in 596 (a 6 for PW), was discarded by Nosiness in 595, and stayed in PW's hand at the end of 597. Fear (PB) was never played (held in 600, in the deck elsewhere).
9. **PB's variant did as well as the plain PB** (4 to 2 against PW's variant, as against the plain PW), while PW's variant is now 3 to 5 over its first eight games (1 to 1 against PU Reverie discard, 2 to 4 here).

### Questions for the testers

- Round 1: Impartiality left PB at 0 in five games. Do you see a turn-one line against it (two moods of different parity, or holding a mood back)? Is it too strong, or is the odd-or-even guess the point of the card?
- Game 597 round 1: Resignation (a 6) cost Resentment (a 5 that needed a black mood). Why that card, and would you play Resignation later instead, when PW's Hate and Impartiality are spent?
- Game 598: PW kept Reverence, Rapport, Discernment and Equanimity in hand to the end. Was the order of plays (Levity, Determination, Hate, Rashness) planned? Would you play white moods first so that Reverence works?
- Neglect: it was in the deck exactly when PW's hand was empty (599 and 600). Does the deck need a second way to put cards on the table, or is this just luck?
- Fear was never played. Would you swap it for Composure or Anticipation (see the PB splash notes)?
- Fun and clarity for Hate against Hate, Rashness against Rashness, and Remorse putting the opponent's Hate back on its deck (597 round 2).

### Game logs

**Game 595.** PB (P1, seat 0) against PW (bot, seat 1). PW won 3 to 2.
- Scores: PB 0, PW 2; PB 6, PW 7; PB 8, PW 7; PB 13, PW 11; PB 16, PW 18.
- Longest turn: 2 plays (PW in round 1: Levity, Impartiality).
- Hands: PB ended with Dejection and Resignation; PW with Rapport.
- Decided: Impartiality (odd) on Brooding in round 1; Shock on Humility (round 3); Brooding took Humility back (round 4); Nosiness took Orderliness (round 5); Equanimity a 6 gave PW 18.

**Game 596.** PW (P1, seat 0) against PB (second tester, seat 1). PB won 3 to 1.
- Scores: PW 4, PB 0; PW 4, PB 8; PW 5, PB 10; PW 6, PB 10.
- Longest turn: 3 plays (PW in round 1: Rashness, Familiarity, Impartiality).
- Hands: PW ended with Solidarity; PB with Dejection and Neglect.
- Decided: Rashness on Remorse and Impartiality (odd) on Resentment (round 1, 4 to 0); Vengeance on Temperance (round 2); Shock on Familiarity (round 3); Hate on Rapport (round 4).

**Game 597.** PB (P1, seat 0) against PW (second tester, seat 1). PW won 3 to 1.
- Scores: PB 0, PW 2; PB 2, PW 0; PB 4, PW 8; PB 7, PW 7.
- Longest turn: 3 plays (PB in round 2: Rashness, Remorse, Shock).
- Hands: PW ended with Humility and Orderliness; PB with Hate.
- Decided: Impartiality (even) on Resignation (round 1); PB's three-play turn in round 2; Modesty then Equanimity (round 3, 8 to 4); Vengeance on Equanimity (round 4, 7 to 7).

**Game 598.** PW (P1, seat 0) against PB (second tester, seat 1). PB won 3 to 0.
- Scores: PW 3, PB 6; PW 3, PB 3; PW 8, PB 8.
- Longest turn: 2 plays (both players in rounds 1 and 3).
- Hands: PW ended with Reverence, Equanimity, Rapport and Discernment; PB with no cards.
- Decided: Rashness then Resignation (a 6) in round 1; Hate on Resignation (round 2); round 3 tied 8 to 8 with PW's four cards unplayed.

**Game 599.** PB (P1, seat 0) against PW (bot, seat 1). PB won 3 to 2.
- Scores: PB 0, PW 4; PB 8, PW 7; PB 6, PW 4; PB 9, PW 11; PB 14, PW 11.
- Longest turn: 3 plays (PW in round 4: Familiarity, Rashness, Temperance).
- Hands: PW had no cards from round 4 (and passed in round 5); PB ended with Brooding and Remorse.
- Decided: Impartiality (odd) on Suspicion (round 1); Vengeance on Equanimity and Hate on Resentment (round 3, 6 to 4); Dejection against PW's empty hand (round 5, 14 to 11).

**Game 600.** PW (P1, seat 0) against PB (bot, seat 1). PB won 3 to 2.
- Scores: PW 6, PB 0; PW 6, PB 5; PW 6, PB 10; PW 11, PB 13; PW 14, PB 15.
- Longest turn: 3 plays (PW in round 1: Familiarity, Modesty, Impartiality).
- Hands: PW had no cards from round 2 and passed in round 3; PB ended with Brooding and Fear.
- Decided: Impartiality (odd) on Dejection (round 1); Hate on Determination (round 2); Resentment (round 3, 10 to 6); Shock on Familiarity (round 5, 15 to 14).

### Notes by card (PW splash against PB splash)

| Card | What the games showed |
|---|---|
| Impartiality | Won round 1 in five games (PB 0 each time): odd against Brooding, Resentment, Suspicion and Dejection; even against Resignation. |
| Shock (PB) | Removed Humility, Familiarity (twice) and Impartiality; played in four games. |
| Hate (both) | PW's: Resignation (twice) and Resentment; PB's: Determination and Rapport. |
| Rashness (both) | Free extra plays; PB's removed Hate (597), PW's removed Remorse (596) and PB's Rashness (598). |
| Resignation | A turn-one 6 once (598), suppressed (597) or bottomed (597, 598) otherwise; held in 595. |
| Fear | Never played (held in 600, in the deck in the other games). |
| Neglect | Played once (597 round 3, no target); in the deck when PW's hand was empty (599, 600). |
| Brooding | Took Humility (removed by Shock) back and played it (595 round 4). |
| Nosiness | Took Orderliness out of PW's hand (595 round 5). |
| Remorse | Free play (596, 597 round 2, 600) and put the opponent's Hate or Rapport back on its deck. |
| Vengeance | Removed Temperance (596), Equanimity (597, 599); a 3 in 598. |
| Orderliness | PW's round 4 play in 596; discarded by Nosiness (595); in hand at the end of 597. |
| Reverence | A 5 in 595, 597 and 600; stuck in hand in 598 (no white mood in play). |
| Equanimity | A 6 in 595 round 5 (18); removed by Vengeance in 597 and 599. |
| Determination | A 3 in 598 and 600 (never a 6 here; Hate bottomed it in 600). |
