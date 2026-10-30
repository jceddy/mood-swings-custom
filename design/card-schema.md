# Card files

Each card is one YAML file in `cards/`, named after the card (`cards/quiet-resolve.yaml`).
The spreadsheet script reads every file there.

```yaml
slot: W-C03            # skeleton slot id (design/skeleton.yaml); omit for an unslotted idea
name: Quiet Resolve
color: white           # white | blue | black | red | green | colorless
rarity: common         # common | uncommon | rare | mythic
base_value: 1          # 0-12; the printed value
alt_value: null        # the conditional value, if any
to_play: false         # has a "To play this card, ..." cost
while_in_play: false   # has a "While in play, ..." ability
after_playing: true    # has an "After playing this mood, ..." effect
rules_text: >-
  After playing this mood, ...
status: idea           # idea | draft | playtest | final
reprint_of: null       # exact name from the original pool, if this is a reprint
impl_tier: 1           # 1 = composes existing simulator effect primitives
                       # 2 = needs a new engine primitive
                       # 3 = paper only (not planned for the simulator)
designer: ""
notes: ""
```

Conventions follow the original pool: text uses "mood" for cards in play, values are printed in the top-right corner,
and a card's abilities are exactly the combination of to-play / while-in-play / after-playing timings.

`python scripts/build_xlsx.py` flags: unknown slots, a card's color or rarity not matching its slot, two cards claiming
one slot, duplicate names, unknown `reprint_of` names, and more reprints than the cap.
