# Mythic build-around axes and partner plan

Status: **tentative**. Q5 in `open-questions.yaml` is still open. Each color keeps one build-around mythic slot (M01); the other
two mythics are flexible. This file plans about 14 partner slots per axis. The slot IDs come from `skeleton.yaml`; no partner cards
exist yet unless a card name is given. Pool counts come from a text search of the baseline, so they are approximate.

## The five axes

| Color | M01 slot | Axis | Mythic so far | Pool cards that already fit |
|---|---|---|---|---|
| White | `W-M01` | Numbers: printed odd and even values | Orderliness | about 20 |
| Blue | `U-M01` | Recycle the discard pile and play many moods | Reverie | extra-play cards, pile fuel |
| Black | `B-M01` | Hand pressure: hand size and hand attacks | Neglect | about 19 |
| Red | `R-M01` | Playing red moods | Dominance | extra-play cards, high-value red moods |
| Green | `G-M01` | Replay from the discard pile, re-trigger after-playing effects | Reinvigoration | pile plays, pile fuel |

The axes were chosen to stay distinct. Blue and green both use the discard pile, but in opposite directions (blue drains it, green
plays from it), so black does not take a third pile axis.

## White: numbers (`W-M01`, Orderliness)

**Idea.** Printed values and parity matter. Restraint (`W-M02`) switches off mood-granted extra plays, so white's M01 should reward
caring about values, not be a play-grant engine. The mythic is Orderliness: choose odd or even numbers on entry, and each of your other
moods with a chosen number in its top right corner gets +1. Number control (suppress and lock out a chosen number) was considered and
could fit `W-M03`.

**Already in the pool:** Courage (5+), Dignity (discard a 0-3), Friendliness (even), Kindness (odd), Repentance (choose a number),
Meekness (suppress 5+), Encouragement and Idealism (dice), Validation (plays a 0 or 1); elsewhere Shock, Rage, Anger, Hostility,
Rebellion (value thresholds), Spite (even), Anxiety (odd), Cheer and Delight (parity discards), Embarrassment (4-6 discard), Denial
and Rejection (same value), Worry (3 or less).

| Slot | Role in the skeleton | What it would do for the axis |
|---|---|---|
| `W-C04` | play-grant | Familiarity (written): extra play if it matches the number of one of your moods |
| `W-U01` | play-grant-restricted | Modesty (written): extra play for a 0, 1, 2, or 3 |
| `W-U02` | play-grant-restricted-2 | Confidence (written): extra play for a 4, 5, or 6 |
| `W-U03` | numbers-pairs | Solidarity (written): value up for each other mood with a 2 (replaced a targeted suppress, too close to Pacifism) |
| `W-U04` | suppress-mass | Impartiality (written): suppress all other moods of the chosen type until the end of the round |
| `W-U05` | deck-hand-flow | Discernment (written): cycle away cards of the chosen type |
| `W-U06` | value-boost | Humility (written): +1 to your 0s, 1s and 2s |
| `W-U07` | conditional-value | Equanimity (written): 6 if four or more moods have even numbers |
| `R-C03` | interaction-lite | Shock (reprint): removal at value 3 or less |
| `R-U01` | sweeper-small | Belligerence (written): sweep your opponents' moods of value 2 or less |
| `R-U02` | sweeper-numeric | Intuition (written): name a number, sweep every other mood with it |
| `R-U03` | removal-highest | Righteousness (written): the leaders lose their highest value mood |
| `B-C03` | interaction-lite | Malevolence (written): a flexible Spite: remove an odd or even mood |
| `G-C07` | utility-small | Cheer/Delight-style discard by value |
| `U-U03` | hand-manipulation | Turmoil (written): a chosen player cycles every odd or even card in hand |

**Risks.** Value-threshold cards are narrow, so the axis needs reliable ways to show numbers on the board. Printed values are
visible, so paper tracking is not an issue.

## Blue: recycle the discard pile and play many moods (`U-M01`, Reverie)

**Idea.** Each play draws a card by sending a discard-pile card to the bottom of the deck. The axis wants plenty of plays (extra
plays) and plenty of fuel in the pile.

| Slot | Role in the skeleton | What it would do for the axis |
|---|---|---|
| `U-C01` | ally-count | Rapport (written): loot, repeatable |
| `U-C04` | play-grant | Fear (reprint): puts a mood in hand, extra play |
| `U-C05` | card-flow | Reminiscence (written): pile card to the bottom, draw a card |
| `U-U07` | play-grant-risky | Impulse (written): extra play, this mood returns to hand after scoring |
| `U-R03` | hand-engine | Reflection (written): discard a card to draw a card on each play, fueling the pile |
| `U-R04` | bounce-engine | Rumination (written): recycle one of your moods each round |
| `U-M02` | flexible mythic | Premonition (written): draw, bottom, extra play |
| `B-C04` | play-grant | Remorse (written): a pile card to the bottom of the deck, draw a card, extra play |
| `B-C07` | utility-small | Suspicion (reprint): fills the pile with hand discards |
| `B-C02` | enemy-count | Disdain (written): removal fills the pile |
| `R-C03` | interaction-lite | Shock (reprint): removal fills the pile |
| `R-R05` | flex | FOMO (written): discards every round |
| `W-C01` | ally-count | Camaraderie (written): extra play |
| `G-C04` | play-grant | Joy (reprint): banked extra play |

**Risks.** The pile is a depleting resource and green wants it full. Restraint shuts off extra plays and the axis leans on them.

## Black: hand pressure (`B-M01`, Neglect)

**Idea.** Hand size and hand attacks. The mythic is Neglect: at the start of each of your turns, each opponent with no cards in their
hand puts one of their moods into the discard pile. It rewards every card that empties or drains hands, and it taxes opponents even when
it never triggers, since they must keep a card in hand. Hand sizes are public, so scaling by hand size was also possible. A discard
engine that makes opponents discard each time they play was considered and rejected as too oppressive.

**Already in the pool:** Vanity (your own empty hand), Suspicion (hand discard), Paranoia (reveal and bottom a card), Guile (discard
two), Ambition, Intimidation, Curiosity, Confusion, Doubt; elsewhere Compulsion, Animosity, Sloth (+1 per card in hand), Cheer,
Delight, Fascination, Bliss, Embarrassment, Dignity.

| Slot | Role in the skeleton | What it would do for the axis |
|---|---|---|
| `B-C04` | play-grant | Remorse (written): pile to deck, draw, extra play (replaced the Ambition reprint) |
| `B-C05` | card-flow | Hate (reprint) |
| `B-C06` | conditional-3 | Schadenfreude (written): rewards discards and removal |
| `B-C07` | utility-small | Suspicion (reprint): hand discard |
| `B-U06` | conditional-value | Composure (written): 6 if you have the most cards in hand |
| `B-U07` | hand-disruption | Nosiness (written): reveal their hand, discard a card of your choice |
| `B-M02` | flexible mythic | Entitlement (written): reveal your hand or lose your best mood |
| `R-C07` | utility-small | Compulsion (reprint): take a card |
| `R-R05` | flex | FOMO (written): hand discards every round |
| `R-U07` | conditional-value | Ruthlessness (written): 5 if an opponent has no cards in hand |
| `G-C02` | enemy-count | Wariness (written): gives a card away |
| `G-U07` | hand-reveal-gift | hand-reveal gift effect |
| `G-R02` | scaling-value | (slot now used by Vindication, rounds-won scaling; no longer a hand-pressure partner) |
| `U-U04` | tempo-shift | (slot re-roled to Overconfidence, a tempo shift; no longer a hand-pressure partner) |

Black's list is mostly filled already; six of the 14 are written or marked. The open need is payoffs.

## Red: playing red moods (`R-M01`, Dominance)

**Idea.** Each red mood you play can remove a weaker opposing mood, so the axis wants many red plays and red moods with high
values. Because the comparison is against the played mood, high-value red moods raise the reach and cheap red plays raise the
frequency. Red extra plays also feed it.

**Already in the pool:** red extra plays (Bravado, Gluttony, Thrill, Stubbornness), red high-value moods (Chaos 6, Fury 4, Boredom 4,
Infatuation, Excitement, Frustration, Triumph, Glee, Embarrassment, Animosity as conditionals).

| Slot | Role in the skeleton | What it would do for the axis |
|---|---|---|
| `R-C01` | ally-count | Fervor (written): extra play with a price |
| `R-C04` | play-grant | Rashness (written): removes an opponent's cheap mood, extra play |
| `R-C05` | card-flow | Zeal (reprint): keeps red cards in hand |
| `R-C06` | conditional-3 | Exuberance (written): 6 if you have two other red moods |
| `R-C08` | high-value-cost | Frenzy (written): 6, leaves the discard pile after scoring |
| `R-U05` | play-grant-drawback | Gluttony-style extra play |
| `R-U07` | conditional-value | value 3 to 5 conditional |
| `R-R03` | scoring-engine | Verve (written): +2 to each red mood you played this round |
| `R-M02` | flexible mythic | Ardor (written): each red mood gets +1 for every red mood you have |
| `R-R04` | tempo-engine | Adrenaline (written): first red play each turn grants an extra play |
| `R-R05` | flex | FOMO (written): value 7, with an upkeep |
| `G-U01` | play-grant | Thrift (written): extra play from the pile for a 0, 1, 2, or 3 |
| `G-U02` | play-grant-2 | Optimism (written): re-trigger another of your moods' after-playing effect |
| `U-C04` | play-grant | Fear (reprint): puts a mood in hand, extra play |
| `W-U01` | play-grant-restricted | extra play restricted by color (red) |

**Risks.** Restraint shuts off extra plays. Dominance wants opposing moods with lower values, which White's value-boost cards
(`W-U06`) work against.

## Green: replay from the discard pile (`G-M01`, Reinvigoration)

**Idea.** Put your board into the discard pile, then replay moods from the whole pile with their after-playing effects happening
again. The axis wants discard-pile plays, fuel for the pile, and cheap moods with strong after-playing effects.

**Already in the pool:** Grace and Harmony (extra plays from the pile), Melancholy and Angst (black, play from the pile), Nostalgia,
Altruism and Cynicism (pickups), Bravado, Hostility, Rebellion, Self-Loathing, Envy, Exhilaration (put moods into the pile).

| Slot | Role in the skeleton | What it would do for the axis |
|---|---|---|
| `G-C01` | ally-count | Warmth (written): pickup from the pile |
| `G-C05` | card-flow | Nostalgia (reprint): pickup plus an extra play |
| `G-U01` | play-grant | Thrift (written): extra play from the pile for a 0, 1, 2, or 3 |
| `G-U02` | play-grant-2 | Optimism (written): re-trigger another of your moods' after-playing effect |
| `G-U08` | flex | Perseverance (written): not a pile card; grows by 2 after scoring while you are behind in rounds |
| `G-R01` | play-grant-engine | Resilience (written): a cheap extra play from the pile each turn |
| `G-M02` | flexible mythic | Wistfulness (written): a pile play grant, and pile plays repeat their after-playing effect |
| `G-M03` | flexible mythic | Fulfillment (written): not a pile card; moods worth 6 or more score an extra time, a payoff for green's 3 to 6 cycle |
| `G-R03` | pile-fuel | Wastefulness (written): puts the top card of the deck into the pile each round |
| `G-R05` | time-scaling | Maturity (written): value grows each round (not a pile card any more) |
| `B-C04` | play-grant | Remorse (written): moves a pile card to the deck, so it needs pile fuel |
| `B-U05` | graveyard | Longing (written): trade a hand card for up to two from the pile |
| `B-R01` | graveyard-engine | Brooding (written): rummage the pile each round |
| `R-C04` | play-grant | Rashness (written): removal fills the pile, extra play |
| `R-U06` | removal-trade | Vindictiveness (written): trade one of your moods to remove a weaker one |
| `U-R02` | copy-effect | Admiration (written): runs a pile mood's after-playing effect |

**Risks.** Reinvigoration's play lock means it works best alone on its turn. Blue's Reverie drains the pile it wants, and Restraint
shuts off extra plays.

## Cross-axis notes

- **Slots that serve more than one axis:** `B-C04` (Remorse: black, blue, green), `B-C07` (Suspicion: black, blue), `R-C04` (Rashness:
  red, green), `R-R05` (FOMO: red, black, blue), `R-C03` (Shock: white, blue). Their value is high; avoid cutting them.
- **Extra-play density.** Red, blue and green axes all lean on extra plays, and white's Restraint (`W-M02`) is a deliberate counter.
  Watch for too many extra-play commons (Camaraderie, Fervor, Wariness, Joy, Fear, Nostalgia, Levity, Remorse and Rashness are already planned).
- **Discard pile.** Blue drains it and green plays from it. That is a built-in interaction, not a conflict, but both need fuel from
  the other colors.
- **Hand size.** Blue's draws (Reverie, Premonition, Rapport) make opposing hand-pressure better, and black's pressure punishes
  hand-heavy blue decks.
- **Unity (`X-M01`, colorless mythic)** cuts across all five axes: it is a payoff for any deck that stacks one color. Extra-play axes
  (red, blue, green) reach five moods fastest, and Restraint counters it.
- **Unfilled partner slots:** white's list is the emptiest, so white needs the most new design.
