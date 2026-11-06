# Play test checklist

Generated from `design/playtest.yaml` by `scripts/build_playtest_md.py`. Edit the yaml, not this file. The
spreadsheet has the same list as the **Playtest** and **Playtest games** sheets, with columns for the results.

## How to run it

- Play on paper first. Proxies can be printed from the Magic Set Editor set file (the new cards have no art, which
  does not matter for testing). The simulator would need engine work first for the cards that need new effects (impl
  tier 2) and cannot run the paper-only cards (impl tier 3: Admiration, Elusiveness, Grudge).
- Build a few themed decks rather than random piles: one per color axis (white numbers, blue recycling, black hand
  pressure, red red moods, green pile replay and 6s) plus one colorless gate deck. Ready-made decklists for the first two
  sessions (extra-play engines, then scaling and anthems), a baseline deck and a game log are in
  `design/playtest-decks.md`.
- Play some 2-player games and at least one with 3 or 4 players (Hurt Feelings, trailing conditions).
- For each card that comes up, write down three things: **strength** (too strong, fair, too weak), **clarity** (was the
  text clear?) and **fun**. If a card is off, note which fallback below you would pick.
- When a card has been tested, move its `status` in `cards/<name>.yaml` from `idea` to `draft` or `playtest`, and record
  the decision in `design/open-questions.yaml` (Q8 for the two Entitlement versions, Q9 for the rest).

## Order

Test tier 1 first, since those cards could break a game. Tier 2 cards are about interactions, tier 3 about cards that may
be too weak, and tier 4 about rules questions.

## Tier 1: Could break the game (test first) (23 cards)

- [ ] **Fulfillment** (green mythic, G-M03): Each of your moods worth 6 or more scores twice. Three conditional moods at 6 can run away.
  - Fallback: A threshold of 7, or score only one such mood an extra time (Enthusiasm style).
- [ ] **Ardor** (red mythic, R-M02): Each of your red moods gets its value increased by the number of red moods you have, a quadratic payoff that may snowball.
  - Fallback: A cap such as "up to three".
- [ ] **Reinvigoration** (green mythic, G-M01): It scales with board size and can replay a whole board (boards grow about one mood per round).
  - Fallback: A cap such as "up to three".
- [ ] **Reverie** (blue mythic, U-M01): It draws on entry and on each later play (about one per round, more with extra plays).
  - Fallback: Once each turn.
- [ ] **Maturity** (green rare, G-R05): Prints 2 and grows by 2 each round (2, 4, 6, 8). Is it too strong when left alone, and do opponents have time to remove it? On paper it needs a counter such as a die.
  - Fallback: Grow by 1.
- [ ] **Vitality** (green rare, G-R06): +2 to every mood of a chosen color each round, including moods played later that round (Q12), is very strong in mono-color decks and rewards extra plays.
  - Fallback: +1.
- [ ] **Overconfidence** (blue uncommon, U-U04): Three plays in one turn, then none. Check the burst against Dominance and Verve decks.
  - Fallback: None chosen yet.
- [ ] **Haunting** (black mythic, B-M03): The burst size next turn with a big pile and a big hand, since each play triggers play engines. Now a 0 whose plays are kept only if you still have it at the start of your next turn, so check it is still playable when opponents can remove it (Rashness, Shock) and not too strong when it survives.
  - Fallback: "Up to three".
- [ ] **Grudge** (white mythic, W-M03): Up to two extra plays each turn when the chosen opponent has 2 round wins. Check the burst against the free-play cycle, Haunting and Affinity, and its replacement effect with Elusiveness.
  - Fallback: None chosen yet.
- [ ] **Rudeness** (white rare, W-R06): Blanks one full turn for every other player. Check the strength against a combo turn.
  - Fallback: Hit only a chosen player.
- [ ] **Levelheadedness** (white rare, W-R01): Every mood scores 2 for a round. Check the swing.
  - Fallback: A cap of 3 per mood.
- [ ] **Affinity** (white rare, W-R02): Another free-play enabler, for decks with duplicate numbers.
  - Fallback: The once-a-turn cap is the safety.
- [ ] **Fear** (blue common, U-C04): One of the five free-play commons (Fear, Nostalgia, Levity, Remorse, Rashness). Five unconditional free extra plays at common, so check how strong extra-play engines get.
  - Fallback: See Levity and Rashness.
- [ ] **Nostalgia** (green common, G-C05): One of the five free-play commons. Pickup from the discard pile plus an extra play.
  - Fallback: See Levity and Rashness.
- [ ] **Levity** (white common, W-C07): A free play that enables extra-play engines.
  - Fallback: Choose between cycling and the extra play.
- [ ] **Remorse** (black common, B-C04): One of the five free-play commons. A card from the discard pile to the bottom of the deck, then draw, plus the extra play.
  - Fallback: See Levity and Rashness.
- [ ] **Rashness** (red common, R-C04): One of the five free-play commons. Removal plus an extra play.
  - Fallback: Remove only a mood with a value of 0.
- [ ] **Reverence** (colorless common, X-C01): Colorless gate common, value 5. The own-mood gate is paid once and then free for the rest of the game, so check 5 against 4.
  - Fallback: Value 4.
- [ ] **Detachment** (colorless common, X-C02): Colorless gate common, value 5. The own-mood gate is paid once and then free, so check 5 against 4.
  - Fallback: Value 4.
- [ ] **Resentment** (colorless common, X-C03): Colorless gate common, value 5. The own-mood gate is paid once and then free, so check 5 against 4.
  - Fallback: Value 4.
- [ ] **Impatience** (colorless common, X-C04): Colorless gate common, value 5. The own-mood gate is paid once and then free, so check 5 against 4.
  - Fallback: Value 4.
- [ ] **Contentment** (colorless common, X-C05): Colorless gate common, value 5. The own-mood gate is paid once and then free, so check 5 against 4.
  - Fallback: Value 4.
- [ ] **FOMO** (red rare, R-R05): Value 7, and paying a card every round drains the hand quickly. Is the mood discarded too soon for 7 to be fair?
  - Fallback: None chosen yet.

## Tier 2: Interactions (18 cards)

- [ ] **Entitlement (restricted)** (black mythic, B-M02): Q8. Hands are often small or empty, so the restricted version fizzles more. Compare it with the unrestricted version.
  - Fallback: Switch to the unrestricted version, or the hybrid that only needs the target to have one or more moods.
- [ ] **Entitlement (unrestricted)** (black mythic, unslotted backup): Q8. The backup version. An opponent with an empty hand cannot decline, so it forces more mood losses. Compare it with the restricted version.
  - Fallback: Switch to the restricted version, or the hybrid that only needs the target to have one or more moods.
- [ ] **Elusiveness** (blue rare, U-R06): Opponents' removal becomes a bounce. Check it against combo decks, and the replacement ordering with Grudge (active player first, then turn order; the controller chooses between their own effects).
  - Fallback: Bounce only moods with a value of 3 or less.
- [ ] **Reassurance** (white uncommon, W-U08): Protects cheap engines from targeted effects (Shrewdness, Covetousness).
  - Fallback: A threshold of 1.
- [ ] **Shrewdness** (blue rare, U-R01): It may be strong against opposing engines now that it only needs a lower or equal value.
  - Fallback: Restore the same-value condition, or require matching printed values.
- [ ] **Covetousness** (red rare, R-R01): A free extra mood every round.
  - Fallback: Only moods with a value of 0.
- [ ] **Opportunism** (black rare, B-R06): It turns discard costs into your cards. Check it against FOMO and Suspicion decks.
  - Fallback: The first card each turn.
- [ ] **Pettiness** (black uncommon, B-U08): A skipped turn for one card.
  - Fallback: Two cards, or block only the first play.
- [ ] **Competitiveness** (red mythic, R-M03): Always one more than the biggest opposing mood that does not have this ability (so two of them settle on the same value). Check its volatility.
  - Fallback: "Equal to" instead of one more.
- [ ] **Gratitude** (green uncommon, G-U06): Needs moods with a current value of 1 or 2 to do anything. Check it against wide boards.
  - Fallback: A value of 3 or less.
- [ ] **Hellbent** (red uncommon, R-U08): The round leader runs their hand dry first (losers draw at the end of a round), so it favors the leader. Check the snowball.
  - Fallback: An alternate value of 6.
- [ ] **Perseverance** (green uncommon, G-U08): Grows by 2 after scoring while you have won fewer rounds than each other player (2, 4, 6 in a 2-player game). Does falling behind become attractive, and is it too strong at match point? Needs a counter on paper.
  - Fallback: Growth of 1, or a value of 1.
- [ ] **Volatility** (red rare, R-R06): Random removal of moods with a value of 1 or less hits your own cheap moods too.
  - Fallback: Opponents' moods only.
- [ ] **Wastefulness** (green rare, G-R03): With Resilience or Thrift it is free plays from the top of the deck, which is card advantage.
  - Fallback: None chosen yet.
- [ ] **Rancor** (red uncommon, R-U04): Mandatory and random, so nobody is prompted. Is a random pick among moods with a value of 3 or less too harsh on cheap engines? The simulator must be able to tell which player controls the effect.
  - Fallback: A value of 1 or less.
- [ ] **Neglect** (black mythic, B-M01): Value 2, and before scoring each opponent with no cards in hand loses a highest value mood (it can trigger the round you play it). The first playtest found the old version far too weak. Is an empty hand reachable without hand disruption, and is it strong enough now?
  - Fallback: Each opponent discards a card from their hand first, and loses the mood only if they can't (before scoring), or a threshold of two or fewer cards.
- [ ] **Heartlessness** (black uncommon, B-U02): It also hits your own board. Check it works when you are behind.
  - Fallback: None chosen yet.
- [ ] **Sentimentality** (black uncommon, B-U04): Check that it does not break the draw rule with a sacrifice engine such as Martyrdom.
  - Fallback: None chosen yet.

## Tier 3: Possibly too weak (6 cards)

- [ ] **Carelessness** (green common, G-C07): Removes two random cards from the deck for pile fuel. Is it too weak?
  - Fallback: One card.
- [ ] **Intuition** (red uncommon, R-U02): Lowered to 1 point after group feedback. Is it still worth playing?
  - Fallback: Raise the value again.
- [ ] **Belligerence** (red uncommon, R-U01): Lowered to 2 points after group feedback. Is it still worth playing?
  - Fallback: Raise the value again.
- [ ] **Candor** (blue uncommon, U-U06): A face-up hand for the whole game may feel oppressive on paper, and the information may matter little against decks that ignore hands.
  - Fallback: None chosen yet.
- [ ] **Defensiveness** (blue uncommon, U-U05): Strips the after-playing effects of opponents' additional moods and spares you. Is it dead against decks without extra plays, and does it need to be symmetric?
  - Fallback: Make it symmetric.
- [ ] **Inspiration** (blue mythic, U-M03): A free card of your choice from the top three cards. Close to Nostalgia, so does it feel like a narrower Nostalgia at mythic rarity?
  - Fallback: The unrestricted extra play, reveal four cards, play up to two of the three, or reveal two cards if too strong.

## Tier 4: Rules and clarity (2 cards)

- [ ] **Admiration** (blue rare, U-R02): What does "this mood" mean when the copied pile mood refers to itself? Proposed ruling is the mood you just played. Paper only (impl tier 3).
  - Fallback: None chosen yet.
- [ ] **Honesty** (green uncommon, G-U07): Showing the hand once may matter more on paper than in digital, and colorless cards in hand make it false.
  - Fallback: None chosen yet.

## Whole-game checks

- [ ] Game length. How many rounds does a game last, and how fast do boards grow (about one mood per round)?
- [ ] Do hands run dry too fast? Hands only refill when you lose a round and through card effects.
- [ ] Color balance. Win rates by color, and mono-color against two-color decks.
- [ ] Axis decks. Do the five axis decks work (white numbers, blue recycling, black hand pressure, red red moods, green pile and 6s)?
- [ ] Extra-play engines. How strong does the pile of free plays, grants and burst turns get when combined?
- [ ] A 3 to 4 player game. Hurt Feelings, the trailing condition of Perseverance, and Rancor and Entitlement with several opponents.
- [ ] Replacement and trigger ordering. Does the rule hold in play (active player first, then turn order; the controller chooses between their own effects)?
- [ ] Paper counters. Can permanent value changes (Maturity, Perseverance) be tracked easily on paper?
