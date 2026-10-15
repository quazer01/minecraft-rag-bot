# 10 — Brewing & Status Effects

## Setup
- **Brewing stand**: blaze rod + 3 cobblestone. Fuel: **blaze powder** (1 powder = 20 brewing operations).
- **Glass bottles** (3 glass → 3 bottles) filled with water from a source block or cauldron.
- Brew 3 potions at once.
- **Nether wart** (grows on soul sand, found in fortresses) is the base for almost everything.

## Brewing flow
```
Water bottle ──(Nether wart)──► Awkward potion ──(effect ingredient)──► Base potion
Base potion ──(Redstone)──► longer duration
Base potion ──(Glowstone)──► level II (shorter)
Base potion ──(Fermented spider eye)──► corrupted / inverted version
Any potion ──(Gunpowder)──► Splash potion ──(Dragon's breath)──► Lingering potion
Arrows (8) + lingering potion (crafting) ──► Tipped arrows
```

## Potion recipes (from Awkward Potion)
| Potion | Ingredient | Duration (base / + redstone / II) |
|---|---|---|
| Swiftness | Sugar | 3:00 / 8:00 / 1:30 (Speed II) |
| Leaping | Rabbit's foot | 3:00 / 8:00 / 1:30 |
| Strength | Blaze powder | 3:00 / 8:00 / 1:30 |
| Healing | Glistering melon slice | Instant (II stronger) |
| Regeneration | Ghast tear | 0:45 / 1:30 / 0:22 |
| Poison | Spider eye | 0:45 / 1:30 / 0:21 |
| Fire Resistance | Magma cream | 3:00 / 8:00 / — |
| Water Breathing | Pufferfish | 3:00 / 8:00 / — |
| Night Vision | Golden carrot | 3:00 / 8:00 / — |
| Slow Falling | Phantom membrane | 1:30 / 4:00 / — |
| Turtle Master | Turtle shell | 0:20 / 0:40 / 0:20 (Slowness IV + Resistance III; II = Slowness VI + Resistance IV) |
| Wind Charged (1.21) | Breeze rod | 3:00 — releases a wind burst on death |
| Weaving (1.21) | Cobweb | 3:00 — spawns cobwebs on death |
| Oozing (1.21) | Slime block | 3:00 — spawns 2 slimes on death |
| Infested (1.21) | Stone | 3:00 — chance to spawn silverfish when hurt |

## Corrupted potions (add Fermented Spider Eye)
| From | Becomes |
|---|---|
| Water bottle | Weakness (1:30 / 4:00) |
| Swiftness or Leaping | Slowness (1:30 / 4:00; Slowness IV 0:20 with glowstone) |
| Healing or Poison | Harming (instant damage) |
| Night Vision | Invisibility (3:00 / 8:00) |

Fermented spider eye = spider eye + brown mushroom + sugar.

## Other potions
- **Mundane / Thick potions** — no effect (water + redstone/glowstone etc.).
- **Potion of Luck** — Creative/commands only (Java).
- **Potion of Decay** — Bedrock only (Wither effect).
- **Ominous bottle** (1.21) — from ominous vaults/raid captains; drinking gives Bad Omen → triggers raids/ominous trials.
- **Milk** — removes all effects. **Honey bottle** — cures Poison.
- **Suspicious stew** — flowers + mushrooms + bowl; effect depends on flower (e.g. oxeye daisy = Regeneration, cornflower = Jump Boost, poppy = Night Vision, lily of the valley = Poison, wither rose = Wither, blue orchid/dandelion = Saturation, allium = Fire Resistance, azure bluet = Blindness, tulips = Weakness, torchflower = Night Vision, eyeblossom (open) = Blindness/(closed) = Nausea).

## Status effects (all)
### Positive
| Effect | Source examples | What it does |
|---|---|---|
| Speed | Potion, beacon | +20% speed per level |
| Haste | Beacon | Faster mining/attacks |
| Strength | Potion, beacon | +3 melee damage per level |
| Instant Health | Potion | Heals 4 HP per level (damages undead) |
| Jump Boost | Potion, beacon | Higher jumps, less fall damage |
| Regeneration | Potion, golden apple, beacon | Heals over time |
| Resistance | Beacon, enchanted golden apple, turtle master | −20% damage per level |
| Fire Resistance | Potion, enchanted golden apple | Immune to fire/lava |
| Water Breathing | Potion, turtle helmet | Breathe underwater |
| Invisibility | Potion | Invisible (armor still visible) |
| Night Vision | Potion | See in dark |
| Health Boost | Commands | Extra max health |
| Absorption | Golden apples | Yellow bonus hearts |
| Saturation | Suspicious stew | Restores hunger instantly |
| Luck | Commands | Better loot |
| Slow Falling | Potion | Fall slowly, no fall damage |
| Conduit Power | Conduit | Water breathing, night vision, fast mining underwater |
| Dolphin's Grace | Dolphins | Fast swimming |
| Hero of the Village | Winning a raid | Villager discounts |

### Negative
| Effect | Source | What it does |
|---|---|---|
| Slowness | Potion, stray arrows | Slower movement |
| Mining Fatigue | Elder guardian | Very slow mining |
| Instant Damage | Potion | 6 damage per level (heals undead) |
| Nausea | Pufferfish, potent sulfur gas (26.2) | Wobbling screen |
| Blindness | Suspicious stew | Can't see far |
| Hunger | Rotten flesh, husk | Drains hunger |
| Weakness | Potion, parched arrows | −4 melee damage |
| Poison | Spider eye, cave spiders, bees, pufferfish | Damage over time (won't kill) |
| Wither | Wither skeletons, Wither, wither rose | Damage over time (can kill), black hearts |
| Levitation | Shulker bullets | Float upward |
| Glowing | Spectral arrows | Outline visible through walls |
| Unluck | Commands | Worse loot |
| Bad Omen | Killing raid captains (old) / ominous bottle | Starts a raid or ominous trial |
| Raid Omen / Trial Omen | Bad Omen near village / trial spawners | Raid countdown / ominous trial |
| Darkness | Warden, sculk shriekers | Pulsing darkness |
| Infested, Oozing, Weaving, Wind Charged | 1.21 potions | Spawn effects when hit/killed |
| Fatal Poison | Bedrock only | Poison that can kill |

## Beacon
- Pyramid of iron/gold/diamond/emerald/netherite blocks: 1 tier (9 blocks) → 4 tiers (164 blocks).
- Powers: Speed, Haste (tier 1–2), Resistance, Jump Boost (tier 2), Strength (tier 3), Regeneration or level II of a primary (tier 4).
- Range: 20 / 30 / 40 / 50 blocks by tier. Fuel each change with an iron/gold ingot, emerald, diamond or netherite ingot.

## Conduit
Heart of the sea + 8 nautilus shells. Surround with prismarine/sea lantern frame (16–42 blocks) underwater for Conduit Power and attacks on hostile mobs nearby.
