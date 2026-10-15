# 12 — Redstone

Redstone is Minecraft's circuitry system: power sources send a **signal** (strength 0–15) through **redstone dust** to **components** that react.

## Timing
- 1 **game tick** = 0.05 s (20 ticks per second).
- 1 **redstone tick** = 2 game ticks = 0.1 s.
- Repeater delay: 1–4 redstone ticks.

## Signal rules
- Dust carries a signal 15 blocks, losing 1 strength per block.
- **Strongly powered** block: powered directly by a source/repeater/comparator → can power adjacent dust.
- **Weakly powered** block: powered by dust on top/pointing into it → can only activate adjacent mechanisms, not dust.
- Dust "points" into blocks; a single dot of dust powers all 4 sides (right-click to toggle dot/cross shape).
- **Quasi-connectivity** (Java only): pistons, droppers and dispensers can be powered as if they were one block taller ("BUD" behaviour).
- Transparent blocks (glass, slabs placed upper, etc.) let dust go up stairs-like without cutting it; glass can't be powered.

## Power sources
| Source | Output |
|---|---|
| Redstone torch | 15, constant; turns OFF when its attached block is powered (inverter / NOT gate) |
| Block of redstone | 15, constant, can be pushed by pistons |
| Lever | 15, toggle |
| Button | 15; stone button stays on 1 s (20 game ticks), wooden 1.5 s (30 game ticks); wooden buttons can be pressed by arrows |
| Pressure plates | Wood/stone: 15 when stepped on; weighted plates: strength by entity count |
| Tripwire hook | 15 when the string is crossed |
| Daylight detector | 0–15 based on sunlight (invertible for night) |
| Observer | 1-tick pulse when the block it faces changes |
| Detector rail | 15 when a minecart is on it |
| Trapped chest | Strength = number of players opening it |
| Target block | 1–15 depending on accuracy of projectile hit |
| Lectern | Pulse when a page is turned |
| Sculk sensor | Detects vibrations within 8 blocks; strength by distance; calibrated sculk sensor filters frequencies |
| Lightning rod | Pulse when struck by lightning |
| Comparator (reading a container) | Strength by fill level |

## Transmission & logic components
| Component | Function |
|---|---|
| **Redstone dust** | Wire |
| **Repeater** | Restores signal to 15, adds 1–4 tick delay, one-way, can be locked by another repeater from the side |
| **Comparator** | Compare mode: outputs rear signal if ≥ side signal. Subtract mode (front torch lit): rear − side. Reads containers, cauldrons, composters, cake, jukeboxes, item frames (rotation), end portal frames, lecterns, chiseled bookshelves, copper golem statues... |
| **Redstone torch** | Inverter |

## Mechanism components (outputs)
| Component | Action |
|---|---|
| Piston / sticky piston | Pushes up to 12 blocks; sticky pulls back. Can't move obsidian, bedrock, tile entities (chests, furnaces) in Java |
| Slime / honey blocks | Move attached blocks with pistons (slime and honey don't stick to each other) — flying machines |
| Dispenser | Shoots/uses items (arrows, water, lava, fire charges, shears sheep, bone meal, equips armor) |
| Dropper | Drops items / pushes into containers |
| Hopper | Moves items (2.5 items/s). Locked when powered |
| Redstone lamp, copper bulb | Light; copper bulb toggles on each pulse (useful as T flip-flop) |
| Doors, trapdoors, fence gates | Open/close |
| Note block | Plays a note (instrument by block below: wood = bass, sand = snare, glass = clicks, stone = bass drum, gold = bells, clay = flute, packed ice = chime, wool = guitar, bone block = xylophone, iron = iron xylophone, soul sand = cow bell, pumpkin = didgeridoo, emerald = bit, hay = banjo, glowstone = pling, **copper = trumpet (26.1)**, mob head on top = mob sound) |
| TNT | Explodes |
| Rails (powered, activator) | Boost/deactivate minecarts |
| Crafter | Crafts one item per pulse |
| Bell | Rings; reveals nearby raiders with Glowing |

## Classic circuits
**NOT gate**: input → block with redstone torch on it → output.
**OR gate**: two inputs joining into one dust line.
**AND gate**: two inputs into blocks with torches, torches feed a dust line, which goes into a block with an output torch (all inverted).
**XOR**: built with comparators in subtract mode or torch arrangements.
**Clock (pulse generator)**: hopper clock (two hoppers + comparators, adjustable by item count), observer clock (two observers facing each other), repeater loop.
**T flip-flop** (button → toggle): copper bulb, dropper + 2 comparators, or sticky piston + block variants.
**Monostable circuit / pulse limiter**: observer, or comparator subtract trick.
**Memory (RS-NOR latch)**: two cross-wired torches.
**Item filter / sorter**: hopper with a comparator; first slot has filter item + 4/1/1/1/1 filler items (classic "41 items" design). Copper golems (1.21.9) can sort items between chests without redstone.

## Popular builds
- **Piston doors**: 2×2 (simple), 3×3, flush doors, hidden staircases.
- **Automatic farms**: sugar cane/bamboo (observer + piston), pumpkin/melon, kelp, cactus, crop farms with villagers, chicken cookers, cow farms.
- **Mob farms**: dark-room mob grinders, creeper farms, spider/zombie spawner XP farms, guardian farms, witch farms, enderman farm in the End, gold/barter farms in the Nether, raid farms (emeralds, totems), iron golem farms, slime farms.
- **Flying machines**: slime/honey + observer + piston engines for moving across the world or clearing land.
- **TNT duper / world eater** (Java-only exploits used in technical play).
- **Storage systems**: item sorters feeding chests/shulker boxes.
- **Minecart rails**: powered rail every ~34 blocks on flat ground keeps carts at full speed. Ice boat roads in the Nether are faster (blue ice).

## Java vs Bedrock redstone differences
- Bedrock: no quasi-connectivity, pistons can push some containers (chests, furnaces) that Java can't, update order is less predictable, and very short pulses behave differently.
- Java has predictable update order and "zero-tick" quirks (many patched).

## Tips
- Use F3 and look at dust to see signal strength in debug info.
- Use **repeaters** to make one-way connections and extend range.
- Use **target blocks** to redirect dust to them.
- Test circuits in a Creative superflat world.
