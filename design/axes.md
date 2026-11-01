# Mythic build-around axes and partner plan

Status: **tentative**. Q5 in `open-questions.yaml` is still open. Each color keeps one build-around mythic slot (M01); the other
two mythics are flexible. This file plans about 14 partner slots per axis. The slot IDs come from `skeleton.yaml`; no partner cards
exist yet unless a card name is given. Pool counts come from a text search of the baseline, so they are approximate.

## The five axes

| Color | M01 slot | Axis | Mythic so far | Pool cards that already fit |
|---|---|---|---|---|
| White | `W-M01` | Numbers: printed odd and even values | Routine | about 20 |
| Blue | `U-M01` | Recycle the discard pile and play many moods | Recollection | extra-play cards, pile fuel |
| Black | `B-M01` | Hand pressure: hand size and hand attacks | Neglect | about 19 |
| Red | `R-M01` | Playing red moods | Dominance | extra-play cards, high-value red moods |
| Green | `G-M01` | Replay from the discard pile, re-trigger after-playing effects | Resurgence | pile plays, pile fuel |

The axes were chosen to stay distinct. Blue and green both use the discard pile, but in opposite directions (blue drains it, green
plays from it), so black does not take a third pile axis.

## White: numbers (`W-M01`, Routine)

**Idea.** Printed values and parity matter. Restraint (`W-M02`) switches off mood-granted extra plays, so white's M01 should reward
caring about values, not be a play-grant engine. The mythic is Routine: choose odd or even numbers on entry, and each of your other
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
| `R-U01` | sweeper-small | sweep by low value |
| `R-U02` | sweeper-numeric | sweep by chosen value |
| `R-U03` | removal-highest | removal of the highest value |
| `B-C03` | interaction-lite | parity removal, Spite-like |
| `G-C07` | utility-small | Cheer/Delight-style discard by value |
| `U-U03` | hand-manipulation | hand effect that cares about values |

**Risks.** Value-threshold cards are narrow, so the axis needs reliable ways to show numbers on the board. Printed values are
visible, so paper tracking is not an issue.

## Blue: recycle the discard pile and play many moods (`U-M01`, Recollection)

**Idea.** Each play draws a card by sending a discard-pile card to the bottom of the deck. The axis wants plenty of plays (extra
plays) and plenty of fuel in the pile.

| Slot | Role in the skeleton | What it would do for the axis |
|---|---|---|
| `U-C01` | ally-count | Rapport (written): loot, repeatable |
| `U-C04` | play-grant | Fear (reprint): puts a mood in hand, extra play |
| `U-C05` | card-flow | a different kind of card flow from Rapport's loot |
| `U-U07` | play-grant-risky | extra play with a risk |
| `U-R03` | hand-engine | hand-based engine |
| `U-R04` | bounce-engine | bouncing and replaying moods |
| `U-M02` | flexible mythic | Foresight (written): draw, bottom, extra play |
| `B-C04` | play-grant | Ambition (reprint): discards a card, extra play |
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
| `B-C04` | play-grant | Ambition (reprint): discard for an extra play |
| `B-C05` | card-flow | Hate (reprint) |
| `B-C06` | conditional-3 | Schadenfreude (written): rewards discards |
| `B-C07` | utility-small | Suspicion (reprint): hand discard |
| `B-U06` | conditional-value | value based on hand sizes |
| `B-U07` | hand-disruption | Paranoia-style hand disruption |
| `B-M02` | flexible mythic | Coercion (written): reveal your hand or lose your best mood |
| `R-C07` | utility-small | Compulsion (reprint): take a card |
| `R-R05` | flex | FOMO (written): hand discards every round |
| `R-U07` | conditional-value | value depends on an opponent's hand size (Animosity-style) |
| `G-C02` | enemy-count | Wariness (written): gives a card away |
| `G-U07` | hand-reveal-gift | hand-reveal gift effect |
| `G-R02` | scaling-value | value per card in hand (Sloth-style) |
| `U-U04` | hand-manipulation-2 | hand manipulation |

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
| `R-C04` | play-grant | Bravado (reprint): sacrifices a mood for an extra play |
| `R-C05` | card-flow | Zeal (reprint): keeps red cards in hand |
| `R-C06` | conditional-3 | red conditional that reaches 5 or 6 |
| `R-C08` | high-value-cost | 5-6 value red mood: raises Dominance's reach |
| `R-U05` | play-grant-drawback | Gluttony-style extra play |
| `R-U07` | conditional-value | value 3 to 5 conditional |
| `R-R03` | scoring-engine | scoring engine that rewards many red moods |
| `R-R04` | tempo-engine | tempo engine |
| `R-R05` | flex | FOMO (written): value 7, with an upkeep |
| `G-U01` | play-grant | extra play, perhaps restricted to a color |
| `G-U02` | play-grant-2 | second extra-play card |
| `U-C04` | play-grant | Fear (reprint): puts a mood in hand, extra play |
| `W-U01` | play-grant-restricted | extra play restricted by color (red) |

**Risks.** Restraint shuts off extra plays. Dominance wants opposing moods with lower values, which White's value-boost cards
(`W-U06`) work against.

## Green: replay from the discard pile (`G-M01`, Resurgence)

**Idea.** Put your board into the discard pile, then replay moods from the whole pile with their after-playing effects happening
again. The axis wants discard-pile plays, fuel for the pile, and cheap moods with strong after-playing effects.

**Already in the pool:** Grace and Harmony (extra plays from the pile), Melancholy and Angst (black, play from the pile), Nostalgia,
Altruism and Cynicism (pickups), Bravado, Hostility, Rebellion, Self-Loathing, Envy, Exhilaration (put moods into the pile).

| Slot | Role in the skeleton | What it would do for the axis |
|---|---|---|
| `G-C01` | ally-count | Warmth (written): pickup from the pile |
| `G-C05` | card-flow | Nostalgia (reprint): pickup plus an extra play |
| `G-U01` | play-grant | Harmony-style extra play from the pile |
| `G-U02` | play-grant-2 | second pile-play grant |
| `G-U08` | flex | pile-related flex |
| `G-R01` | play-grant-engine | Hope-style engine |
| `G-R03` | discard-play-engine | Grace-style engine |
| `G-R05` | flex | pile-related flex |
| `B-C04` | play-grant | Ambition (reprint): puts a card in the pile |
| `B-U05` | graveyard | bigger recursion than Yearning's swap |
| `B-R01` | graveyard-engine | Melancholy-style engine |
| `R-C04` | play-grant | Bravado (reprint): sacrifices a mood into the pile |
| `R-U06` | removal-trade | trades your mood for removal, filling the pile |
| `U-R02` | copy-effect | copy effect that cares about after-playing text |

**Risks.** Resurgence's play lock means it works best alone on its turn. Blue's Recollection drains the pile it wants, and Restraint
shuts off extra plays.

## Cross-axis notes

- **Slots that serve more than one axis:** `B-C04` (Ambition: black, blue, green), `B-C07` (Suspicion: black, blue), `R-C04` (Bravado:
  red, green), `R-R05` (FOMO: red, black, blue), `R-C03` (Shock: white, blue). Their value is high; avoid cutting them.
- **Extra-play density.** Red, blue and green axes all lean on extra plays, and white's Restraint (`W-M02`) is a deliberate counter.
  Watch for too many extra-play commons (Camaraderie, Fervor, Wariness, Joy, Bravado, Ambition, Fear are already planned).
- **Discard pile.** Blue drains it and green plays from it. That is a built-in interaction, not a conflict, but both need fuel from
  the other colors.
- **Hand size.** Blue's draws (Recollection, Foresight, Rapport) make opposing hand-pressure better, and black's pressure punishes
  hand-heavy blue decks.
- **Unity (`X-M01`, colorless mythic)** cuts across all five axes: it is a payoff for any deck that stacks one color. Extra-play axes
  (red, blue, green) reach five moods fastest, and Restraint counters it.
- **Unfilled partner slots:** white's list is the emptiest, so white needs the most new design.
