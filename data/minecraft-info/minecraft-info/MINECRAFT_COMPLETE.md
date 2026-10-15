# Minecraft Reference Library — Index

Compiled October 2026. Current versions at time of writing:
- **Java Edition 26.3** ("Wilderness Bound", released 15 Sep 2026)
- **Bedrock Edition 26.50** (same drop)

## Files
| # | File | Contents |
|---|------|----------|
| 01 | `01_overview_and_history.md` | What Minecraft is, creators, timeline, sales, spin-offs, the movie |
| 02 | `02_editions_and_update_history.md` | Java vs Bedrock, every major update from Classic to 26.3, version numbering |
| 03 | `03_survival_guide_and_progression.md` | First night, mechanics (health, hunger, XP), full progression path to beating the game |
| 04 | `04_blocks_ores_materials.md` | Ores and Y-levels, block categories, wood sets, building blocks, light levels |
| 05 | `05_tools_weapons_armor.md` | Material tiers, durability, damage, armor points, special gear (mace, spear, trident, elytra) |
| 06 | `06_crafting_smelting_recipes.md` | Key recipes in text-grid form, smelting, smithing, stonecutter, fuels |
| 07 | `07_mobs.md` | Every mob: passive, neutral, hostile, bosses — health, drops, behaviour |
| 08 | `08_biomes_dimensions_structures.md` | Overworld/Nether/End biomes, all generated structures and their loot |
| 09 | `09_enchanting_and_anvils.md` | Every enchantment, max levels, incompatibilities, anvil mechanics |
| 10 | `10_brewing_and_status_effects.md` | Brewing recipes, durations, all status effects |
| 11 | `11_food_farming_animals_villagers.md` | Food stats, crops, breeding, taming, villager professions and trading |
| 12 | `12_redstone.md` | Signal rules, every component, ticks, classic circuits, farm designs |
| 13 | `13_commands_and_technical.md` | Commands, target selectors, game rules, F3 debug, data packs |
| 14 | `14_tips_tricks_glossary.md` | Pro tips, speedrun basics, community slang/glossary, fun facts |
| ALL | `MINECRAFT_COMPLETE.md` | Every file above merged into one document |

## Notes on accuracy
- Numbers are for **Java Edition** unless marked (Bedrock differs in places; see file 02).
- Health is given in HP (2 HP = 1 heart).
- Minecraft changes several times a year. For the very latest, check minecraft.net and the community Minecraft Wiki (minecraft.wiki).


---

# 01 — Minecraft Overview & History

## What is Minecraft?
Minecraft is a 3D sandbox game made of blocks (each 1 m³). Players explore procedurally generated, effectively infinite worlds; gather resources; craft tools; build; fight monsters; farm; trade; and engineer machines with "redstone" (in-game circuitry). There is no required goal, though Survival mode has an "ending": defeating the Ender Dragon in the End dimension.

- **Developer:** Mojang Studios (Stockholm, Sweden) — owned by Microsoft (Xbox Game Studios)
- **Original creator:** Markus "Notch" Persson
- **Lead designer since late 2011:** Jens "Jeb" Bergensten
- **Genre:** Sandbox, survival, building
- **Engine:** Java Edition is written in Java; Bedrock Edition in C++
- **Status:** Best-selling video game of all time (over 300 million copies sold, announced 2023) with well over 100 million monthly players

## Game modes
| Mode | Description |
|------|-------------|
| **Survival** | Health, hunger, gather everything yourself. The "default" experience. |
| **Creative** | Unlimited blocks, flight, invulnerability. Pure building. |
| **Adventure** | For custom maps; blocks can only be broken/placed with specifically-tagged tools. |
| **Spectator** | Fly through blocks, invisible, can view from mobs' perspective (Java; Bedrock added it later). |
| **Hardcore** | Survival locked on Hard difficulty with one life. On death the world is spectator-only (Java). |

## Difficulties
Peaceful (no hostile mobs, health regenerates, hunger doesn't drop) → Easy → Normal → Hard (starvation can kill, zombies break doors, more mob equipment, villagers always turn into zombie villagers when killed by zombies).

## Timeline of the company and game
| Date | Event |
|------|-------|
| 10–17 May 2009 | Notch builds the first prototype ("Cave Game"); first public version (later called Classic) released 17 May 2009 |
| Late 2009 | Indev, then Infdev (infinite worlds) |
| 30 Jun 2010 | Alpha — Survival mode for sale, the Nether arrives (Halloween Update, Oct 2010) |
| Late 2010 | Mojang founded (Notch, Jakob Porsér, Carl Manneh) |
| 20 Dec 2010 | Beta |
| 18 Nov 2011 | **Full release 1.0** at MineCon 2011 in Las Vegas; the End and the Ender Dragon added |
| Dec 2011 | Notch hands lead development to Jeb |
| 2011–2012 | Pocket Edition (mobile) and Xbox 360 Edition (4J Studios) |
| 15 Sep 2014 | Microsoft announces acquisition of Mojang for US$2.5 billion (closed Nov 2014); Notch leaves |
| 2016 | Education Edition released |
| 2017 | "Better Together" update: Pocket/Windows 10/console versions unified as **Bedrock Edition** with cross-play |
| 2018 | Original Xbox 360/PS3-style "Legacy Console" editions stop getting updates |
| 2019 | Minecraft Earth (AR) — shut down June 2021 |
| 2020 | Mojang AB renamed **Mojang Studios**; Minecraft Dungeons released |
| 2022 | Java and Bedrock sold together as one PC bundle |
| 2023 | Minecraft Legends released; 300 million copies sold milestone |
| 2024 | Mojang announces smaller, more frequent **"game drops"** instead of one big yearly update |
| 4 Apr 2025 | **A Minecraft Movie** (live action, Warner Bros./Legendary) — one of the highest-grossing video game films |
| 2025 | Vibrant Visuals graphics overhaul arrives on Bedrock; four game drops released |
| 2026 | Year-based version numbers (26.1, 26.2, 26.3...) begin |

## Spin-off games and media
| Title | Year | Notes |
|-------|------|-------|
| Minecraft: Story Mode | 2015 | Episodic narrative game by Telltale Games; delisted 2019 |
| Minecraft: Education Edition | 2016 | Classroom version with chemistry, coding (MakeCode, Python) |
| Minecraft Earth | 2019 | Augmented-reality mobile game; closed 2021 |
| Minecraft Dungeons | 2020 | Dungeon-crawler action RPG (Diablo-like) |
| Minecraft Legends | 2023 | Action-strategy game; content updates ended 2024 |
| A Minecraft Movie | 2025 | Dir. Jared Hess; Jack Black (Steve), Jason Momoa, Emma Myers, Danielle Brooks, Sebastian Hansen |
| Minecraft Dungeons II | Announced for 2026 | Sequel announced at Minecraft LIVE 2026 |
| Books | ongoing | Official novels (e.g. *The Island*), guides, comics |
| Theme parks/experiences | 2020s | Minecraft Experience touring exhibits; a Minecraft land at Chessington World of Adventures (UK) announced |

## Key in-game characters & lore
- **Steve** and **Alex** — default player skins. Since 2022 there are 9 default skins (Steve, Alex, Ari, Efe, Kai, Makena, Noor, Sunny, Zuri).
- **Herobrine** — famous community creepypasta ("Removed Herobrine" is a long-running joke in patch notes). Never actually in the game.
- **The Ancient Builders** — implied lost civilisation behind ancient cities, trail ruins, and the Sculk.
- **End Poem** — the text shown after defeating the Ender Dragon, written by Julian Gough (released to the public domain in 2022).
- **C418** (Daniel Rosenfeld) — composer of the classic soundtrack ("Sweden", "Wet Hands", "Subwoofer Lullaby"). Later music by Lena Raine, Kumi Tanioka, Aaron Cherof, Amos Roddy and others.

## Events
- **MineCon** (2011–2016) → **MineCon Earth/Live** (2017–2020) → **Minecraft LIVE** (2021–). Live showcases now happen roughly twice a year.
- **Mob Vote** (2017–2023): the community voted on one new mob per year (e.g. Glow Squid, Allay, Sniffer, Armadillo). Discontinued after 2023 due to community feedback.


---

# 02 — Editions & Complete Update History

## The editions today
| | **Java Edition** | **Bedrock Edition** |
|---|---|---|
| Platforms | Windows, macOS, Linux | Windows, Xbox, PlayStation, Switch, iOS, Android, Fire tablets |
| Language | Java | C++ |
| Cross-play | Java ↔ Java only | All Bedrock platforms together |
| Mods | Huge free modding scene (Fabric, NeoForge, Forge, Quilt) | Add-ons + paid Marketplace |
| Servers | Any community server (Hypixel etc.) | Featured servers + custom servers |
| Redstone | Quasi-connectivity, deterministic, "update order" tricks | No quasi-connectivity, pistons can move more things |
| Graphics extras | Shaders via mods (Iris/OptiFine); experimental Vulkan renderer since 26.2 | Vibrant Visuals (official), RTX ray tracing on Windows |
| Purchase | Bundled with Bedrock on PC ("Java & Bedrock Edition for PC") | |

**Notable gameplay differences (Bedrock vs Java)**
- Bedrock: the Wither has 600 HP (Java 300), different combat timing (no attack cooldown in Bedrock's design), skeletons/zombies differences, slime/bamboo farms behave differently, random seed-based structure placement differs, hoes can't be sweep-attacked etc.
- Bedrock has some unique blocks/features historically (e.g. Education-only chemistry elements, "Allow/Deny/Border" blocks).
- Java has Spectator in full, debug screen (F3), and data packs; Bedrock has add-ons and behavior packs.
- Mojang aims for "parity", so most content now ships to both on the same day.

**Other editions**
- *Minecraft Education* — school version.
- *Legacy Console Edition* (Xbox 360, PS3, Wii U, PS Vita...) — discontinued 2018–2019; had famous mini-games (Battle, Tumble, Glide).
- *Minecraft: Pi Edition* (Raspberry Pi, 2013) — free, for teaching coding.
- *Minecraft China* — NetEase-run version.
- *New Nintendo 3DS Edition* — discontinued.

## Version numbering
- 2011–2025: `1.MAJOR.MINOR` (e.g. 1.21.11). "1.x" became a joke because 2.0 never came.
- **From 2026: year-based** `YY.DROP.HOTFIX`. 26.1 = first drop of 2026, 26.1.1 = first hotfix. Bedrock uses e.g. 26.10, 26.30, 26.50.
- Java 26.1 was the first release that needs **Java 25** and the first shipped **without code obfuscation**, which helps modders.
- Development builds: **snapshots** (Java, e.g. 26.2 snapshot 6), pre-releases, release candidates; Bedrock uses **Preview** builds.

## "Game drops" (since late 2024)
Mojang now ships several smaller themed updates per year ("drops") instead of one huge summer update.

---

## Complete update timeline (Java Edition)

### Pre-release era
| Phase | Date | Highlights |
|---|---|---|
| Classic | May 2009 | Creative building in a browser; 32 blocks; multiplayer |
| Indev | Dec 2009 | Survival elements, crafting, day/night |
| Infdev | Feb 2010 | Infinite worlds |
| Alpha | Jun 2010 | Survival for sale, multiplayer survival, redstone, biomes; Halloween Update added the Nether, pumpkins, Ghasts |
| Beta | Dec 2010 | Weather, beds, pistons (1.7), wolves, Adventure Update (1.8: hunger, XP, sprinting, villages, strongholds, Endermen) |

### Full releases
| Version | Name | Released | Main additions |
|---|---|---|---|
| 1.0 | Adventure Update | 18 Nov 2011 | The End, Ender Dragon, enchanting, brewing, Mooshrooms, Hardcore |
| 1.1 | — | Jan 2012 | Spawn eggs, Superflat worlds, language support |
| 1.2 | — | Mar 2012 | Jungle biome, ocelots/cats, iron golems, world height 256 (Anvil format) |
| 1.3 | — | Aug 2012 | Emeralds and villager trading, desert & jungle temples, ender chests, tripwire, Adventure mode, singleplayer runs an internal server |
| 1.4 | Pretty Scary Update | Oct 2012 | Wither, witches, bats, beacons, anvils, command blocks, item frames, carrots/potatoes, pumpkin pie |
| 1.5 | Redstone Update | Mar 2013 | Comparators, hoppers, droppers, daylight sensors, trapped chests, Nether quartz |
| 1.6 | Horse Update | Jul 2013 | Horses, donkeys, mules, leads, hay bales, carpet, new launcher, resource packs |
| 1.7 | Update that Changed the World | Oct 2013 | Biome overhaul (mesa, roofed forest, mega taiga...), new flowers, stained glass, fishing loot, Realms |
| 1.8 | Bountiful Update | Sep 2014 | Ocean monuments, guardians, rabbits, endermites, slime blocks, banners, armor stands, granite/diorite/andesite, Spectator mode |
| 1.9 | Combat Update | Feb 2016 | Attack cooldown, shields, off-hand, elytra, End cities, shulkers, chorus fruit, tipped arrows, Mending |
| 1.10 | Frostburn Update | Jun 2016 | Polar bears, husks, strays, magma blocks, fossils, structure blocks |
| 1.11 | Exploration Update | Nov 2016 | Woodland mansions, explorer maps, llamas, vindicators, evokers, vexes, totem of undying, shulker boxes, observers |
| 1.12 | World of Color | Jun 2017 | Concrete, glazed terracotta, parrots, advancements (replaced achievements), recipe book |
| 1.13 | Update Aquatic | Jul 2018 | Ocean overhaul, dolphins, turtles, drowned, phantoms, trident, shipwrecks, coral, kelp, swimming, "The Flattening" (block ID overhaul), data packs |
| 1.14 | Village & Pillage | Apr 2019 | New villages and villager jobs, pillagers, ravagers, raids, crossbows, wandering trader, foxes, pandas, bamboo, scaffolding, new job blocks |
| 1.15 | Buzzy Bees | Dec 2019 | Bees, beehives/nests, honey, honeycomb |
| 1.16 | Nether Update | Jun 2020 | Netherite, 4 new Nether biomes, piglins, hoglins, zoglins, striders, bastions, respawn anchor, lodestone, blackstone |
| 1.17 | Caves & Cliffs Pt I | Jun 2021 | Axolotls, goats, glow squid, copper, amethyst, spyglass, lightning rod, powder snow, candles, dripstone |
| 1.18 | Caves & Cliffs Pt II | Nov 2021 | New terrain generator, world height −64 to 320, huge caves, lush & dripstone caves, mountain biomes, new ore distribution |
| 1.19 | The Wild Update | Jun 2022 | Deep Dark, Warden, ancient cities, sculk, mangrove swamps, frogs, allay, recovery compass, chest boats |
| 1.20 | Trails & Tales | Jun 2023 | Cherry grove, camel, sniffer, archaeology (brush, suspicious sand/gravel, pottery sherds), armor trims, smithing templates, bamboo wood, hanging signs, chiseled bookshelves |
| 1.20.5 | Armored Paws | Apr 2024 | Armadillo, wolf armor, 8 new wolf variants, item "components" system |
| 1.21 | Tricky Trials | Jun 2024 | Trial chambers, breeze, bogged, mace, wind charges, trial spawners & vaults, crafter, copper bulbs/doors/grates, tuff variants, Density/Breach/Wind Burst |
| 1.21.2 | Bundles of Bravery | Oct 2024 | Bundles (all colours), Hardcore on Bedrock, minecart/physics tweaks |
| 1.21.4 | The Garden Awakens | Dec 2024 | Pale Garden biome, Creaking & creaking heart, pale oak wood, resin & resin bricks, eyeblossoms, pale moss |
| 1.21.5 | Spring to Life | Mar 2025 | Warm/cold variants of pigs, cows and chickens, firefly bushes, leaf litter, wildflowers, cactus flowers, bushes, dry grass, falling leaves, blue/brown eggs |
| 1.21.6 | Chase the Skies | Jun 2025 | **Happy Ghast** (rideable flying mob for 4 players), dried ghast block, ghastlings, harnesses, Locator Bar, music disc "Tears" |
| 1.21.7 | — | Jun/Jul 2025 | "Lava Chicken" music disc (from the movie) and fixes |
| 1.21.9 | The Copper Age | Sep 2025 | **Copper golem** (sorts items into chests), copper tools & armor, copper chests, copper torches/lanterns/bars/chains, shelves |
| 1.21.11 | Mounts of Mayhem | 9 Dec 2025 | **Spear** (all tiers) + Lunge enchantment, **nautilus** & zombie nautilus (rideable underwater), nautilus armor, camel husk + parched, zombie horses spawn naturally, netherite horse armor |
| **26.1** | **Tiny Takeover** | 24 Mar 2026 | Redesigned baby mobs (models, hitboxes, sounds), **golden dandelion** (freezes baby aging), **craftable name tags** (paper + metal nugget), trumpet note block sound (note block on copper), new direct stonecutter conversions. Bedrock 26.10 |
| **26.2** | **Chaos Cubed** | 16 Jun 2026 | **Sulfur Caves** biome, **sulfur cube** mob (absorbs blocks, behaves like them), sulfur & cinnabar block sets, potent sulfur pools (nausea gas), sulfur springs/geysers, naturally-spawning cave spiders, friends list/party features, experimental Vulkan renderer (Java). Bedrock 26.30 |
| **26.3** | **Wilderness Bound** | 15 Sep 2026 | **Dappled Forest** biome, **poplar** wood set and red/orange/yellow poplar leaves, shelf mushrooms, red shrubs, **abandoned camps**, new explorer maps, **cushions** (sit down!), **straw beds** (skip night without setting spawn; 3 hay bales), wool & concrete stairs/slabs in 16 colours, spectators can use portals. Java moved from GLFW to SDL3; new servers default to an allowlist. Bedrock 26.50 |

### Mounts of Mayhem detail (1.21.11)
- Spear exists in wood, stone, copper, iron, gold, diamond, netherite; charge attacks deal damage based on your speed (works on horses, nautiluses, elytra).
- Nautilus: tamed with pufferfish; lets you ride underwater; zombie nautilus spawns with drowned riders.
- Camel husk spawns in deserts carrying a husk with a spear and a *parched* (desert skeleton variant with Weakness arrows).

### Chaos Cubed detail (26.2)
- Sulfur cube: passive slime-like mob. Give it a block and it absorbs it, taking on behaviour "archetypes" (e.g. bouncy, slow-bouncy, hot, explosive with TNT). Shears release the block and restore its AI. Can be bucketed.
- Sulfur Caves only appear in newly generated chunks.

### Wilderness Bound detail (26.3)
- Dappled Forest generates near cold biomes; exclusive red shrubs and shelf mushrooms (usable for parkour).
- Abandoned camps (tents, chests, barrels) appear in many biomes and adapt to them; loot includes wheat, bread, leather, axes, arrows and explorer maps leading to mansions and monuments.
- Cushions can be placed on flat surfaces and sat on; players have used them to build pixel displays and mini-games.

## Bedrock milestone updates (names match Java)
Pocket Edition milestones: 0.9 (infinite worlds, 2014), 0.12 (Nether-ish, 2015), 0.14 (Overworld Heavy), 0.16 (Boss update), 1.0 Ender Update (2016), 1.2 Better Together (2017). Since then Bedrock follows the same named updates as Java.

## Tech changes worth knowing
- 1.13 "Flattening": numeric IDs replaced by names like `minecraft:oak_planks`.
- 1.18: 384-block-tall world.
- 1.20.5: NBT item tags replaced by **item components** (`/give @s diamond_sword[enchantments={sharpness:5}]`).
- 1.21.11: game rules moved to registry IDs (snake_case names).
- 26.1: requires Java 25; unobfuscated.
- 26.3: SDL3 for windowing/input; server log lines moving to the Management Protocol; allowlist on by default for new servers.


---

# 03 — Survival Guide & Progression

## Core mechanics
| Mechanic | Details |
|---|---|
| **Health** | 20 HP (10 hearts). Regenerates when hunger ≥ 18 (9 drumsticks); fast regen when saturation is full and hunger is 20. |
| **Hunger** | 20 points (10 drumsticks). Hidden **saturation** drains first. Sprinting needs > 6 hunger. At 0 you take starvation damage (kills on Hard; stops at 1 HP on Normal, 10 HP on Easy). |
| **Exhaustion** | Actions (sprinting, jumping, attacking, taking damage, regenerating) add exhaustion; every 4.0 removes one saturation/hunger point. |
| **Oxygen** | 300 ticks (15 s) of air underwater shown as bubbles, then 2 HP damage per second. |
| **Experience (XP)** | Orbs from mobs, mining ores (coal, diamond, emerald, lapis, redstone, quartz, sculk), smelting, breeding, trading, fishing. Used for enchanting and anvils. Level 30 needs 1,395 total XP from 0. |
| **Day/night** | One day = 20 real minutes (10 min day, ~1.5 min dusk/dawn, 7 min night). Hostile mobs spawn at light level 0 (since 1.18) in darkness. |
| **Fall damage** | 1 HP per block above 3 blocks. Water, hay bales (−80%), slime blocks, cobwebs, powder snow, beds (−50%), honey blocks reduce/cancel it. |
| **Light** | Blocks emit 0–15 light. Monsters spawn only on blocks with block light 0. |
| **Respawn** | At your bed / respawn anchor, or world spawn. Items drop where you died and despawn after 5 minutes (while the chunk is loaded). |

## Controls (Java defaults)
WASD move · Space jump · Shift sneak · Ctrl sprint (or double-tap W) · E inventory · Q drop · F swap off-hand · 1–9 hotbar · T chat · / command · F1 hide HUD · F2 screenshot · F3 debug · F5 camera · F11 fullscreen · Tab player list · L advancements · Middle-click pick block.

## The first day (step by step)
1. **Punch a tree** — get ~10–16 logs.
2. Logs → **planks** (1 log = 4 planks) → **crafting table** (4 planks) and **sticks** (2 planks = 4 sticks).
3. Craft a **wooden pickaxe**, mine ~20 cobblestone, then craft **stone pickaxe, axe, sword, shovel**.
4. Craft a **furnace** (8 cobblestone). Smelt logs into **charcoal** if you can't find coal.
5. **Torches**: 1 coal/charcoal + 1 stick = 4 torches.
6. Kill **sheep** for 3 wool → **bed** (3 wool + 3 planks). Sleep to skip the night and set spawn.
7. Kill animals for food (cows, pigs, chickens, sheep) and cook the meat.
8. If no bed by dusk: dig into a hillside, block the entrance, mine while waiting.

## Standard progression path
1. **Wood → stone tools**
2. **Food source**: wheat farm (seeds from grass), animal pens, or a villager village.
3. **Iron**: caves or strip-mining around Y 16 (or mountains near Y 232). Make iron tools, a **shield** (6 planks + 1 iron), **bucket**, and **iron armor** (24 ingots for a full set).
4. **Diamonds**: best around **Y −59** (deepslate layer). Mine for a diamond pickaxe first, then sword/armor. Bring water bucket for lava.
5. **Enchanting table** (2 diamonds, 4 obsidian, 1 book) + 15 bookshelves.
6. **Nether portal**: obsidian frame (minimum 4×5 = 10 obsidian without corners, 14 with) lit with flint and steel. Obsidian forms when water touches a lava source.
7. **Nether**: wear at least one piece of gold armor so piglins stay peaceful. Find a **Nether fortress** (blaze rods, Nether wart, wither skeleton skulls) and **bastion remnants** (gold, netherite upgrade template, loot). Mine **ancient debris** near Y 15 for **netherite**.
8. **Eyes of Ender**: blaze powder + ender pearl (from endermen or piglin bartering). Need about 12+ (some frames may already be filled; some eyes break when thrown).
9. **Find the stronghold**: throw an eye of ender; it flies toward the stronghold. Dig down when it starts dropping in place. The **End portal** room has 12 frames.
10. **The End**: destroy the End crystals on top of the obsidian pillars (some are caged in iron bars — shoot or climb), then fight the **Ender Dragon** (200 HP). Bring bows/arrows, blocks, pumpkin to wear (stops endermen aggro), slow falling or water bucket. Beds explode in the End — speedrunners use this to damage the dragon.
11. **Post-game**: End gateways → outer End islands → **End cities** (elytra, shulker boxes, shulker shells), **Wither** (beacon), raids, trial chambers, ancient cities, building, mega-farms.

## Essential early-game tips
- Never dig straight down; never dig straight up under gravel/sand.
- Carry a **water bucket** at all times (fall saves, lava, fire, building).
- Sleep each night to avoid phantoms (they spawn after 3 in-game days without sleep).
- Creepers: hit and back off; shields block the explosion when facing it.
- Keep valuables in an **ender chest** when travelling (its inventory is per-player and shared across all ender chests).
- Use a **compass** for world spawn, **recovery compass** (echo shards) to find your last death point.
- Mark coordinates (F3 in Java, "Show coordinates" world option in Bedrock).
- Light caves systematically; place torches on one side only so you know the way back.

## Advancements overview (Java)
Five tabs: **Minecraft** (story progression), **Nether**, **The End**, **Adventure**, **Husbandry**. Notable challenges: "How Did We Get Here?" (have every effect at once), "Adventuring Time" (visit all biomes), "Two by Two" (breed every breedable animal), "A Balanced Diet" (eat every food), "Monsters Hunted" (kill every hostile mob), "Arbalistic" (kill 5 mobs with one crossbow shot). Bedrock uses **Achievements** linked to Xbox accounts (disabled if cheats are on).

## Speedrunning basics (Any% Random Seed)
Common route: punch tree → find shipwreck/buried treasure or village for iron → make portal by casting obsidian with lava + water → bastion for pearls via bartering → fortress for blaze rods → triangulate stronghold → "one-cycle" the dragon with beds. World records are under 10 minutes for random seeds on modern versions.


---

# 04 — Blocks, Ores & Materials

## World layout (since 1.18)
- Overworld: **Y −64 to Y 320** (build limit). Sea level **Y 63**.
- **Deepslate** replaces stone below Y 0 (blends between Y 0 and Y 8).
- **Bedrock** (unbreakable) at the bottom (Y −64 to −60) in the Overworld; at top and bottom of the Nether (Y 0–4, 123–127; Nether roof at 128).
- Nether is 128 blocks tall; 1 block in the Nether = **8 blocks** in the Overworld horizontally.

## Ores — where to find them (Java, current generation)
| Ore | Y range | Best Y | Drop | Pickaxe needed |
|---|---|---|---|---|
| **Coal** | 0 to 320 | ~95 (also high mountains) | Coal (XP) | Wood |
| **Copper** | −16 to 112 | ~48 (huge in dripstone caves) | 2–5 raw copper (Fortune boosts) | Stone |
| **Iron** | −64 to 320 | ~16, also ~232 in mountains | Raw iron | Stone |
| **Lapis lazuli** | −64 to 64 | ~0 | 4–9 lapis | Stone |
| **Gold** | −64 to 32 | ~−16 (badlands: up to 256 extra) | Raw gold | Iron |
| **Redstone** | −64 to 15 | ~−59 | 4–5 redstone dust | Iron |
| **Diamond** | −64 to 16 | **−59** (most common near bottom; less air exposure higher) | Diamond | Iron |
| **Emerald** | −16 to 320, mountains only | ~232 | Emerald | Iron |
| **Nether quartz** | Nether 10–117 | anywhere | Quartz | Wood |
| **Nether gold** | Nether 10–117 | anywhere | 2–6 gold nuggets | Wood |
| **Ancient debris** | Nether 8–119 | **~15** (8–22) | Ancient debris (smelt → netherite scrap) | Diamond |

Tips:
- Fortune III multiplies drops of coal, diamond, emerald, lapis, redstone, quartz, copper/iron/gold raw items (not ancient debris).
- **Silk Touch** gets the ore block itself.
- Ancient debris is blast-resistant: beds and TNT are used to "bed mine" for it at Y 15.
- Ore veins: large hidden veins of copper+granite (above Y 0) and iron+tuff (below Y 0) with raw ore blocks.

## Mining speeds (tool tiers)
Wood < Stone < Copper < Iron < Diamond < Netherite (Gold is fastest but has wood-tier harvest level and tiny durability). Efficiency V + Haste II allows "insta-mining" stone-type blocks.

## Raw material storage blocks
9 items → 1 block (and back): coal, iron, gold, copper, raw iron/gold/copper, diamond, emerald, lapis, redstone, netherite, also slime, honey(4 bottles), bone (bone meal), dried kelp, wheat (hay bale), resin.

## Wood types
| Wood | Source biome | Notes |
|---|---|---|
| Oak | Most biomes | Drops apples |
| Spruce | Taiga, snowy | 2×2 mega trees |
| Birch | Birch forest | White bark |
| Jungle | Jungle | 2×2 giant trees; cocoa beans grow on it |
| Acacia | Savanna | Orange planks, grey bark |
| Dark oak | Dark forest | Only grows 2×2; drops apples |
| Mangrove | Mangrove swamp | Propagules, roots, mud |
| Cherry | Cherry grove | Pink; pink petals |
| Pale oak | Pale garden | Pale grey-white; creaking hearts |
| **Poplar** | **Dappled forest (26.3)** | Grey wood, red/orange/yellow leaves |
| Bamboo | Jungle | Bamboo blocks/planks, mosaic, bamboo raft |
| Crimson | Crimson forest (Nether) | Stems/hyphae, non-flammable |
| Warped | Warped forest (Nether) | Teal, non-flammable |

Each wood set gives: log/stem, stripped log, wood, stripped wood, planks, stairs, slab, fence, fence gate, door, trapdoor, button, pressure plate, sign, hanging sign, boat (or raft/chest boat), and (since Copper Age) a **shelf**.

## Stone families
Stone, cobblestone, mossy cobblestone, smooth stone, stone bricks (mossy, cracked, chiseled), granite, diorite, andesite (+ polished), deepslate (cobbled, polished, bricks, tiles, chiseled), tuff (polished, bricks, chiseled — 1.21), calcite, dripstone, blackstone (polished, bricks, gilded), basalt (smooth/polished), end stone (bricks), purpur, prismarine (bricks, dark), sandstone/red sandstone (cut, chiseled, smooth), mud bricks, resin bricks (1.21.4), quartz (pillar, bricks, chiseled, smooth), **sulfur and cinnabar block sets (26.2)**.

Since 26.3 wool and concrete have stairs and slabs in all 16 colours.

## The 16 dye colours
White, light grey, grey, black, brown, red, orange, yellow, lime, green, cyan, light blue, blue, purple, magenta, pink. Colourable blocks: wool, carpet, terracotta, glazed terracotta, concrete, concrete powder, stained glass (+panes), beds, banners, candles, shulker boxes, bundles, (harness for happy ghast).

## Light-emitting blocks (light level)
| Level | Blocks |
|---|---|
| 15 | Glowstone, sea lantern, lantern, jack o'lantern, beacon, lava, fire, shroomlight, froglight, conduit (active), respawn anchor (full), end gateway/portal, campfire, redstone lamp (on), lit copper bulb |
| 14 | Torch, copper torch, end rod, cave vines with glow berries |
| 12 | Four candles in one block (each candle adds 3) |
| 10 | Soul torch, soul lantern, soul campfire, crying obsidian |
| 7 | Redstone torch, enchanting table, ender chest, glow lichen, lit redstone ore (9) |
| 5 | Amethyst cluster |
| 3 | Magma block |
| 1 | Brewing stand, brown mushroom, dragon egg, end portal frame, sculk sensor |
Light decreases by 1 per block travelled.

## Blast resistance (selected)
Obsidian, crying obsidian, ancient debris, netherite block, anvil, respawn anchor, ender chest, reinforced deepslate — immune to normal explosions. Bedrock, barrier, end portal frame — indestructible in Survival.

## Gravity blocks
Sand, red sand, gravel, concrete powder, anvils, dragon egg, scaffolding (sort of), pointed dripstone, suspicious sand/gravel.

## Special/utility blocks
Crafting table, furnace, blast furnace (2× speed, ores/armor), smoker (2× speed, food), campfire, chest/barrel, ender chest, shulker box, hopper, anvil, grindstone (remove enchantments, gain XP), smithing table, stonecutter, loom (banners), cartography table, fletching table, composter, lectern, cauldron, brewing stand, enchanting table, beacon, conduit, lodestone, respawn anchor, bell, scaffolding, crafter (auto-crafting), vault and trial spawner, copper chest, shelves, cushions (26.3), straw bed (26.3).


---

# 05 — Tools, Weapons & Armor

## Material tiers
| Tier | Durability (tools) | Harvest level | Enchantability | Notes |
|---|---|---|---|---|
| Wood | 59 | Wood | 15 | Can be used as furnace fuel |
| Stone | 131 | Stone | 5 | Also blackstone/cobbled deepslate |
| Copper (1.21.9) | 190 | Stone (mines iron) | ~13 | Between stone and iron |
| Iron | 250 | Iron | 14 | |
| Gold | 32 | Wood | 22 | Fastest mining speed; piglins like it |
| Diamond | 1,561 | Diamond | 10 | |
| Netherite | 2,031 | Netherite | 15 | Diamond + netherite ingot + upgrade template at smithing table; floats in lava, fire-proof |

Harvest level decides *what drops*: e.g. you need iron or better for diamond/gold/redstone/emerald ore, diamond or better for obsidian, crying obsidian, ancient debris, respawn anchor.

## Swords (Java combat)
| Sword | Damage | Attack speed |
|---|---|---|
| Wood / Gold | 4 | 1.6 |
| Stone / Copper | 5 | 1.6 |
| Iron | 6 | 1.6 |
| Diamond | 7 | 1.6 |
| Netherite | 8 | 1.6 |
Swords do sweep attacks (Sweeping Edge enchant in Java), break cobwebs fast, and block nothing (use a shield).

## Axes (Java)
| Axe | Damage | Attack speed |
|---|---|---|
| Wood / Gold | 7 | 0.8 / 1.0 |
| Stone / Copper | 9 | 0.8 |
| Iron | 9 | 0.9 |
| Diamond | 9 | 1.0 |
| Netherite | 10 | 1.0 |
Axes disable shields for 5 seconds, strip logs, scrape copper oxidation/wax.

## Other tools
- **Pickaxe** — stone, ores, metal blocks.
- **Shovel** — dirt, sand, gravel, snow, clay, soul sand; makes dirt paths and extinguishes campfires.
- **Hoe** — tills farmland; fastest for leaves, sculk, hay, moss, nether wart blocks, sponges.
- **Shears** — wool, leaves, cobwebs, vines, tripwire without triggering, pumpkin carving, honeycomb, mooshroom → cow; releases a sulfur cube's absorbed block (26.2).
- **Flint and steel / fire charge** — fire, Nether portals, TNT.
- **Fishing rod** — fish, treasure (enchanted books, saddles, nautilus shells, name tags), pull mobs. Carrot/warped fungus on a stick steer pigs/striders.
- **Brush** — archaeology on suspicious sand/gravel; brushes armadillo scutes.
- **Spyglass** — zoom. **Compass**, **recovery compass**, **clock**, **map**.
- **Lead** — tie mobs (now also happy ghasts, boats-ish behaviour in recent versions).
- **Bucket** — water, lava, milk (cures effects), powder snow, fish/axolotl/tadpole, sulfur cube (26.2).
- **Bundle** — stores up to a stack's worth of mixed items in one slot (1.21.2).

## Ranged & special weapons
| Weapon | Key facts |
|---|---|
| **Bow** | Up to 9–10 damage fully charged (crit chance). Enchants: Power, Punch, Flame, Infinity, Unbreaking, Mending. |
| **Crossbow** | Loads arrows or fireworks; Multishot, Piercing, Quick Charge. Fireworks rockets as ammo deal explosion damage. Pillagers use them. |
| **Trident** | Only from drowned. 9 melee, 8 thrown. Loyalty (returns), Riptide (launch yourself in rain/water), Channeling (lightning in storms), Impaling. |
| **Mace** (1.21) | Heavy core (vault loot) + breeze rod. Smash attack deals bonus damage per block fallen and resets your fall damage; Density, Breach, Wind Burst. Combine with wind charges for huge combos. |
| **Spear** (1.21.11) | All material tiers. Charge/jab attacks scaled by your movement speed — strong on horseback, nautilus, or elytra. **Lunge** enchantment gives a forward burst. |
| **Wind charge** | Thrown item from breezes; knocks back mobs and launches the player (no fall damage reset like the mace, but great for mobility). |
| **Snowballs/eggs** | Knockback only (snowballs damage blazes 3). |
| **Fire charge** | From dispensers: fireball. |
| **Ender pearl** | Teleport where it lands (5 fall damage). |
| **Splash/lingering potions** | Harming, poison, weakness, slowness, etc. |
| **TNT / TNT minecart / end crystal / bed (in Nether/End) / respawn anchor (Overworld)** | Explosive weapons. |

## Combat mechanics (Java 1.9+)
- **Attack cooldown**: wait for the meter to fill for full damage.
- **Critical hit**: attack while falling (not sprinting) = +50% damage.
- **Sprint-knockback**: sprinting hit adds knockback.
- **Shields**: block most frontal damage; disabled by axes. Can have banner patterns.
- Bedrock still uses near-spam-click combat.

## Armor points
| Material | Helmet | Chestplate | Leggings | Boots | Total | Toughness |
|---|---|---|---|---|---|---|
| Leather | 1 | 3 | 2 | 1 | 7 | 0 |
| Copper (1.21.9) | 2 | 4 | 3 | 1 | 10 | 0 |
| Golden | 2 | 5 | 3 | 1 | 11 | 0 |
| Chainmail | 2 | 5 | 4 | 1 | 12 | 0 |
| Iron | 2 | 6 | 5 | 2 | 15 | 0 |
| Diamond | 3 | 8 | 6 | 3 | 20 | 2 each |
| Netherite | 3 | 8 | 6 | 3 | 20 | 3 each + 10% knockback resistance each |
| Turtle shell (helmet) | 2 | — | — | — | — | Water Breathing 10 s when entering water |

Max armor is 20 points (10 chestplate icons) = up to 80% damage reduction (lowered by high damage unless you have toughness). Protection enchantments add up to another 80% total.

**Armor durability (helmet/chest/legs/boots):** leather 55/80/75/65, gold 77/112/105/91, chain & iron 165/240/225/195, diamond 363/528/495/429, netherite 407/592/555/481.

**Leather armor** can be dyed any colour (mix dyes at a crafting table or wash in a cauldron).

## Armor trims (1.20)
Smithing table: armor + **trim template** + **material** → decoration only.
- 18 templates: Coast, Dune, Eye, Host, Raiser, Rib, Sentry, Shaper, Silence, Snout, Spire, Tide, Vex, Ward, Wayfinder, Wild, Bolt, Flow (Bolt & Flow from trial chambers). Silence (ancient city) is the rarest.
- Materials: amethyst, copper, diamond, emerald, gold, iron, lapis, netherite, quartz, redstone, resin.
- Duplicate a template: template + 7 diamonds + base block (e.g. cobblestone).

## Special wearables
- **Elytra** — from End city ships; glide, propel with firework rockets. Repair with phantom membranes or Mending.
- **Carved pumpkin** — wear to avoid angering endermen (blocks view).
- **Mob heads** — reduce detection range of that mob type.
- **Wolf armor** (armadillo scutes), **horse armor** (leather, iron, gold, diamond, netherite since 1.21.11), **llama carpets**, **nautilus armor** (1.21.11), **harness** for happy ghast (1.21.6).
- **Totem of undying** (off-hand/main hand) — prevents death once; from evokers.


---

# 06 — Crafting, Smelting, Smithing & Stonecutting

## How to read the grids
3×3 grid, rows top→bottom. `.` = empty. Shapeless recipes are noted. The 2×2 inventory grid handles recipes that fit in 2×2.

## Basics
```
Planks: 1 log → 4 planks (shapeless)
Sticks: 2 planks vertical → 4 sticks
Crafting table:   P P     Torch (×4):  C        Chest:  P P P
                  P P                  S                P . P
                                                        P P P
Furnace:  K K K    (K = cobblestone/blackstone/cobbled deepslate)
          K . K
          K K K
```

## Tools (M = material, S = stick)
```
Pickaxe   Axe      Shovel   Hoe      Sword
M M M     M M      M        M M      M
. S .     M S      S        . S      M
. S .     . S      S        . S      S
```
Materials: planks, cobblestone, copper ingot, iron ingot, gold ingot, diamond. Netherite is made by **smithing**, not crafting. The **spear** (1.21.11) is also crafted per material.

## Armor (M = material)
```
Helmet   Chestplate   Leggings   Boots
M M M    M . M        M M M      M . M
M . M    M M M        M . M      M . M
         M M M        M . M
```
Costs: helmet 5, chestplate 8, leggings 7, boots 4 = 24 per set.

## Useful recipes (written)
| Item | Recipe |
|---|---|
| Bed | 3 wool (top row) + 3 planks (middle row) |
| **Straw bed** (26.3) | 3 hay bales |
| **Name tag** (26.1) | Paper + metal nugget (gold/iron/copper) |
| **Golden dandelion** (26.1) | Dandelion surrounded by 8 gold nuggets |
| Shield | Planks in a Y shape with iron ingot at top centre: `P I P / P P P / . P .` |
| Bow | 3 sticks + 3 string |
| Arrow (×4) | Flint / stick / feather stacked vertically |
| Crossbow | `S I S / T H T / . S .` (stick, iron, string, tripwire hook) |
| Bucket | 3 iron in a V |
| Shears | 2 iron diagonal |
| Flint and steel | Iron + flint |
| Compass | 4 iron around redstone dust |
| Clock | 4 gold around redstone dust |
| Recovery compass | 8 echo shards around compass |
| Map | 8 paper around compass |
| Book | 3 paper + 1 leather (shapeless) |
| Bookshelf | 6 planks + 3 books |
| Enchanting table | `. B . / D O D / O O O` (book, diamonds, obsidian) |
| Anvil | 3 iron blocks top, 1 iron ingot middle, 3 ingots bottom (31 iron total) |
| Brewing stand | 1 blaze rod over 3 cobblestone |
| Beacon | 5 glass, Nether star, 3 obsidian |
| Ender chest | 8 obsidian around eye of ender |
| Eye of ender | Ender pearl + blaze powder |
| Hopper | 5 iron + chest (V shape) |
| Piston | 3 planks / cobble-iron-cobble / cobble-redstone-cobble |
| Sticky piston | Piston + slimeball |
| Observer | `C C C / R R Q / C C C` (cobble, redstone, quartz) |
| Redstone torch | Redstone dust on stick |
| Repeater | Torch-redstone-torch on 3 stone |
| Comparator | 3 redstone torches + quartz + 3 stone |
| TNT | 5 gunpowder + 4 sand/red sand in checkerboard |
| Rails (×16) | 6 iron + 1 stick |
| Powered rails (×6) | 6 gold + stick + redstone |
| Golden apple | 8 gold ingots around an apple |
| Golden carrot | 8 gold nuggets around carrot |
| Glistering melon | 8 gold nuggets around melon slice |
| Cake | 3 milk, 2 sugar, 1 egg, 3 wheat |
| Bread | 3 wheat in a row |
| Pumpkin pie | Pumpkin + sugar + egg |
| Scaffolding (×6) | 6 bamboo + 1 string |
| Lantern | 8 iron nuggets around torch |
| Campfire | 3 sticks, coal/charcoal, 3 logs |
| Crafter | 5 iron, crafting table, 2 redstone, dropper |
| Mace | Heavy core over breeze rod |
| Wolf armor | 6 armadillo scutes |
| Harness | 3 leather, 2 glass, 1 wool (colour = wool) |
| Bundle | String + leather |
| Lodestone | 8 chiseled stone bricks + netherite ingot |
| Respawn anchor | 6 crying obsidian + 3 glowstone |
| Conduit | 8 nautilus shells around heart of the sea |
| Netherite ingot | 4 netherite scrap + 4 gold ingots (shapeless) |

## Smelting
Furnace: 10 s per item. Blast furnace: ores, raw metals, metal tools/armour (→ nuggets) at 2× speed. Smoker: food at 2× speed. Campfire: food, 30 s, no fuel, 4 at a time.

| Input | Output |
|---|---|
| Raw iron/gold/copper (or ore) | Ingot |
| Ancient debris | Netherite scrap |
| Sand | Glass |
| Cobblestone | Stone → (again) smooth stone |
| Stone bricks | Cracked stone bricks |
| Clay ball | Brick; clay block → terracotta |
| Netherrack | Nether brick |
| Log | Charcoal |
| Cactus | Green dye |
| Sea pickle | Lime dye |
| Kelp | Dried kelp |
| Wet sponge | Sponge |
| Raw meat/fish, potato | Cooked food |
| Chorus fruit | Popped chorus fruit |
| Iron/gold tools & armour | Iron/gold nuggets |
| Sandstone, quartz, basalt | Smooth variants |

## Fuel values (items smelted per unit)
| Fuel | Items |
|---|---|
| Lava bucket | 100 |
| Block of coal | 80 |
| Dried kelp block | 20 |
| Blaze rod | 12 |
| Coal / charcoal | 8 |
| Log, planks, wooden tools etc. | 1.5 |
| Bamboo, sticks | 0.25–0.5 |
| Carpet | 0.335 |

## Smithing table
- Diamond tool/armor + **netherite upgrade template** + netherite ingot → netherite version (keeps enchantments).
- Netherite template found in bastion remnants; duplicate with 7 diamonds + netherrack.
- Armor trims (see file 05).

## Stonecutter
One stone-type block → stairs (1:1), slabs (1:2), walls, polished/brick/chiseled variants without waste. Also copper cutting. 26.1 added more direct conversions for stone and deepslate variants.

## Loom
Banner + dye (+ optional banner pattern item) → patterns. Pattern items: Flower Charge, Creeper Charge, Skull Charge, Thing (Mojang logo), Globe, Snout, Flow, Guster, Field Masoned, Bordure Indented.

## Crafter (1.21)
Redstone-powered auto-crafting block. Toggle slots off to shape recipes; a redstone pulse crafts once and ejects the result.


---

# 07 — Mobs (Creatures)

HP in health points (2 HP = 1 heart). Values are Java Edition.

## Passive mobs (never attack)
| Mob | HP | Where | Drops / uses | Breeding / notes |
|---|---|---|---|---|
| Allay | 20 | Pillager outposts, woodland mansions (caged) | Collects items matching the one you give it; dances to jukeboxes | Duplicates with amethyst shard while dancing |
| Armadillo | 12 | Savanna, badlands | Scutes (brush it) → wolf armor | Spider eye; rolls up when threatened |
| Axolotl | 14 | Lush caves | Fights drowned/guardians with you; 5 colours (blue is very rare, 1/1200) | Bucket of tropical fish |
| Bat | 6 | Caves | — | Ambient |
| Camel | 32 | Desert villages | Two riders, dash ability, tall (hostile mobs can't reach you) | Cactus |
| Cat | 10 | Villages, swamp huts | Scares creepers & phantoms; brings gifts | Raw cod/salmon; 11 coat variants |
| Chicken | 4 | Grassy biomes | Feathers, raw chicken, eggs | Seeds; warm/cold variants (1.21.5) lay brown/blue eggs |
| Cod / Salmon / Tropical fish / Pufferfish | 3 | Oceans/rivers | Food; tropical fish ~3,000+ pattern combos | Bucketable |
| Cow | 10 | Grassy biomes | Leather, beef, milk | Wheat; temperate/warm/cold variants |
| Donkey / Mule | 15–30 | Plains, savanna | Can carry a chest | Mule = horse × donkey (sterile) |
| Frog | 10 | Swamps | Eats small slimes (slimeballs) and magma cubes → froglights (colour by frog type) | Slimeball; 3 variants by biome temperature |
| Glow squid | 10 | Deep dark water underground | Glow ink sacs (glowing sign text) | |
| Happy ghast | 20 | Grown from a dried ghast block placed in water → ghastling | Flying mount for up to 4 players with a harness | Snowballs heal/feed; 1.21.6 |
| Horse | 15–30 | Plains, savanna | Speed/jump/health vary | Golden apple/carrot; zombie horses now spawn naturally (1.21.11) with zombie horsemen |
| Mooshroom | 10 | Mushroom fields | Mushroom stew from bowl; red/brown (brown via lightning); suspicious stew from brown | Wheat |
| Nautilus | — | Oceans | Rideable underwater mount; can wear nautilus armor (1.21.11) | Tamed with pufferfish |
| Ocelot | 10 | Jungle | Scares creepers; trust with raw fish | |
| Parrot | 6 | Jungle | Sits on shoulder; imitates mob sounds; dances | Tamed with seeds; **cookies kill parrots** |
| Pig | 10 | Grassy | Porkchops; ride with saddle + carrot on a stick | Carrot/potato/beetroot; variants |
| Rabbit | 3 | Desert, snowy, flower forest | Rabbit hide, raw rabbit, **rabbit's foot** (leaping potion) | Dandelions/carrots; Killer Bunny variant (named "The Killer Bunny") |
| Sheep | 8 | Grassy | Wool (16 colours; shear for 1–3), mutton | Wheat; naturally pink sheep are rare (~0.16%); name "jeb_" for rainbow |
| Skeleton horse | 15 | Thunderstorm traps | Rideable underwater | |
| Sniffer | 14 | Hatched from sniffer eggs (ocean ruins via archaeology) | Sniffs up torchflower seeds & pitcher pods | Torchflower seeds |
| Snow golem | 4 | Built: 2 snow blocks + carved pumpkin | Throws snowballs; makes snow trails | Melts in warm biomes/rain |
| Squid | 10 | Oceans | Ink sacs (black dye) | |
| Strider | 20 | Nether lava lakes | Walk on lava with saddle + warped fungus on a stick | Warped fungus |
| Tadpole | 6 | Swamps | Grows into frog | Slimeball |
| Turtle | 30 | Beaches | Scutes (turtle shell helmet); eggs only hatch on their home beach | Seagrass |
| Villager | 20 | Villages | Trading (see file 11) | Needs beds + food |
| Wandering trader | 20 | Near player | Rare items; spawns with 2 trader llamas | Sells name tags for 1 emerald (26.1) |
| **Copper golem** | 12 | Built: copper block + carved pumpkin (1.21.9) | Moves items from copper chests into matching chests; oxidizes into a statue unless waxed/scraped | |
| **Sulfur cube** | — | Sulfur Caves (26.2) | Absorbs a block and gains its "archetype" behaviour (bouncy, slow-bouncy, hot, explosive...); shears release the block; bucketable | |

## Neutral mobs (attack only if provoked or under conditions)
| Mob | HP | Notes |
|---|---|---|
| Bee | 10 | Stings once (poison) then dies; whole hive angers. Pollinates crops. Use a campfire under the hive to harvest safely. |
| Cave spider | 12 | Hostile in mineshaft spawners; now also spawns naturally in Sulfur Caves (26.2). Poison bite. |
| Dolphin | 10 | Grants Dolphin's Grace when you swim near; leads you to treasure if fed raw fish. |
| Enderman | 40 | Angers if you look at its face or hit it. Teleports, hates water. Drops ender pearls. Picks up blocks. |
| Fox | 10 | Sleeps by day, steals items, eats sweet berries; trusts you if bred. |
| Goat | 10 | Rams mobs/players off cliffs; screaming goats; drops goat horns when ramming wood/stone/ore. |
| Iron golem | 100 | Village defender; spawns when villagers panic/gossip. Drops iron and poppies. Builds: 4 iron blocks T-shape + carved pumpkin. |
| Llama / trader llama | 15–30 | Spits; carries chests; caravans with leads. |
| Panda | 20 | Personalities: normal, lazy, worried, playful, aggressive, weak, brown (rare). Bamboo. |
| Piglin | 16 | Nether. Peaceful if you wear gold armor. **Bartering**: give a gold ingot → random item (ender pearls, fire resistance, obsidian, string, quartz, crying obsidian, soul speed books...). Angry if you open their chests or mine gold. |
| Polar bear | 30 | Attacks if cubs nearby. |
| Spider | 16 | Neutral in daylight (bright light), hostile at night. Climbs walls. String, spider eyes. |
| Trader llama | — | Defends wandering trader. |
| Wolf | 8 (40 tamed) | Tame with bones; 9 variants (1.20.5); wear wolf armor. Feed meat to heal. |
| Zombified piglin | 20 | Whole group angers if one is hit. Gold nuggets/ingots. |

## Hostile mobs
| Mob | HP | Where | Drops | Notes |
|---|---|---|---|---|
| Blaze | 20 | Nether fortresses | **Blaze rods** | Fireballs; weak to snowballs |
| Bogged | 16 | Swamps, trial chambers | Bones, arrows of Poison, mushrooms | Mossy skeleton variant (1.21) |
| Breeze | 30 | Trial chambers | **Breeze rods** (mace, wind charges) | Deflects projectiles, shoots wind charges |
| Creaking | — | Pale garden at night | — | Can't be killed directly; only moves when not looked at; destroy its **creaking heart** in a pale oak log |
| Creeper | 20 | Overworld | Gunpowder, music discs if killed by skeleton | Explodes; charged creeper (lightning) drops mob heads |
| Drowned | 20 | Oceans, rivers | Copper, rotten flesh, **trident** (rare), nautilus shell | Zombie that drowned |
| Elder guardian | 80 | Ocean monument (3 per monument) | Wet sponge, prismarine, tide trim | Gives Mining Fatigue III |
| Endermite | 8 | From ender pearls (rare) | — | Endermen attack them |
| Evoker | 24 | Woodland mansions, raids | **Totem of undying**, emeralds | Summons vexes and fangs |
| Ghast | 10 | Nether | Ghast tears, gunpowder | Reflect fireballs back to kill; source of dried ghast blocks (1.21.6) |
| Guardian | 30 | Ocean monuments | Prismarine shards/crystals, fish | Laser beam |
| Hoglin | 40 | Crimson forest | Pork, leather | Breed with crimson fungus; afraid of warped fungus; becomes zoglin in Overworld |
| Husk | 20 | Deserts | Rotten flesh | Hunger effect; doesn't burn in sun; rides camel husks (1.21.11) |
| Magma cube | varies | Nether | Magma cream | Splits |
| **Parched** | — | Deserts (1.21.11) | Bones, arrows | Skeleton variant riding camel husks; Weakness arrows |
| Phantom | 20 | Sky, when you haven't slept 3+ days | Phantom membrane (slow falling, elytra repair) | Afraid of cats |
| Piglin brute | 50 | Bastions | Golden axe (rare) | Always hostile, not distracted by gold |
| Pillager | 24 | Outposts, raids, patrols | Crossbow, arrows, ominous banner (captain) | Killing a captain gives Bad Omen → Raid |
| Ravager | 100 | Raids | Saddle | Destroys crops/leaves |
| Shulker | 30 | End cities | **Shulker shells** (shulker boxes) | Levitation bullets |
| Silverfish | 8 | Infested blocks, strongholds | — | Calls others when hit |
| Skeleton | 20 | Overworld | Bones, arrows, bow | Burns in sun |
| Skeleton horseman | — | Lightning traps | | |
| Slime | varies | Swamps (night), slime chunks below Y 40 | Slimeballs | Splits into smaller slimes |
| Stray | 20 | Snowy biomes | Slowness arrows | Skeleton variant |
| Vex | 14 | Summoned by evokers | — | Flies through walls; dies after time |
| Vindicator | 24 | Mansions, raids | Iron axe, emeralds | Named "Johnny" → attacks everything |
| Warden | 500 | Deep dark (summoned by shriekers) | **Sculk catalyst** | Blind, tracks vibrations & smell; sonic boom ignores armor; very high damage. Avoid it! |
| Witch | 26 | Swamp huts, anywhere at night, raids | Potion ingredients (redstone, glowstone, sugar, sticks, spider eyes, gunpowder, glass bottles) | Throws harmful potions, drinks healing |
| Wither skeleton | 20 | Nether fortresses | **Wither skeleton skull** (2.5%; Looting helps), coal, bones, stone sword | Wither effect |
| Zoglin | 40 | Zombified hoglin | Rotten flesh | Attacks everything |
| Zombie | 20 | Overworld | Rotten flesh, rare iron/carrots/potatoes | Burns in sun; can break doors on Hard; babies are fast; chicken jockeys |
| Zombie villager | 20 | Overworld | | **Cure** with splash potion of Weakness + golden apple → villager with big discounts |
| Zombie nautilus | — | Oceans (1.21.11) | | Ridden by drowned |
| Camel husk | — | Deserts (1.21.11) | | Undead camel with husk (spear) + parched riders |

## Bosses
| Boss | HP | How to summon / find | Reward |
|---|---|---|---|
| **Ender Dragon** | 200 | The End (always on first entry). Respawn with 4 end crystals on the exit portal. | 12,000 XP first time (500 later), dragon egg, End gateway (activated after each kill) |
| **Wither** | 300 (600 Bedrock) | Build: 4 soul sand/soul soil in a T + 3 wither skeleton skulls on top. Explodes on spawn; shield phase below half HP (arrows don't work, use melee) | **Nether star** → beacon |
| **Warden** | 500 | Deep dark, mini-boss | Sculk catalyst only — not worth fighting |
| **Elder guardian** | 80 | Ocean monuments | Sponges, tide trim template |

## Mob spawning rules (Java, simplified)
- Hostiles spawn in **block light 0** (sky light ≤ 7 counts), on solid blocks, ≥ 24 blocks from players, within 128 blocks (despawn instantly beyond 128).
- Mob cap: about 70 hostiles per player-loaded area.
- Spawners (dungeons, mineshafts, fortresses, trial chambers) follow their own rules (light ≤ 11 for regular spawners).
- Slime chunks: 1 in 10 chunks, below Y 40, determined by seed.
- Mushroom fields and Deep Dark have no natural hostile spawns (the deep dark spawns nothing; warden is summoned).

## Mob variants (cosmetic)
Cats (11), wolves (9), frogs (3), axolotls (5), horses (7 colours × 5 markings), llamas (4), parrots (5), rabbits (6+), foxes (2), pandas (7 personalities), tropical fish (2,700+), sheep (16 colours), cows/pigs/chickens (temperate/warm/cold), villagers (7 biome types × 15 professions), mooshrooms (2), salmon (3 sizes), striders (cold/warm), copper golem oxidation stages, sulfur cube archetypes.

## Easter-egg names (name tag)
- **"jeb_"** sheep: rainbow wool.
- **"Dinnerbone"** or **"Grumm"**: mob renders upside down.
- **"Toast"** rabbit: special texture (memorial for a real lost pet bunny).
- **"Johnny"** vindicator: attacks all mobs.
- **"The Killer Bunny"**: hostile rabbit (summon-only in Java).


---

# 08 — Dimensions, Biomes & Structures

## The three dimensions
| Dimension | Description | How to get there |
|---|---|---|
| **Overworld** | Main world; day/night, weather, Y −64 to 320 | Start here |
| **The Nether** | Hellish, lava oceans, no water (water evaporates), beds explode, compasses spin; 1 block = 8 Overworld blocks | Obsidian Nether portal (min 4×5 frame), lit with fire |
| **The End** | Floating end-stone island in the void; Ender Dragon; outer islands with End cities | End portal in a stronghold (12 eyes of ender) |

## Overworld biomes (grouped)
**Temperate / grassy**
- Plains, Sunflower Plains, Meadow, Forest, Flower Forest, Birch Forest, Old Growth Birch Forest, Dark Forest, **Pale Garden** (1.21.4; creaking, eyeblossoms), Cherry Grove, **Dappled Forest** (26.3; poplars, red shrubs, shelf mushrooms; near cold biomes), Swamp, Mangrove Swamp, Mushroom Fields (no hostile spawning).

**Warm / dry**
- Desert (temples, wells, camels, camel husks, husks), Savanna, Savanna Plateau, Windswept Savanna, Badlands (mesa), Wooded Badlands, Eroded Badlands (extra gold, mineshafts at surface), Jungle, Sparse Jungle, Bamboo Jungle (pandas).

**Cold / snowy**
- Taiga, Old Growth Pine Taiga, Old Growth Spruce Taiga, Snowy Taiga, Snowy Plains, Ice Spikes, Snowy Beach, Frozen River, Grove, Snowy Slopes.

**Mountains (peaks)**
- Windswept Hills, Windswept Gravelly Hills, Windswept Forest, Jagged Peaks, Frozen Peaks, Stony Peaks. (Emeralds and goats.)

**Water**
- River, Beach, Stony Shore, Ocean / Deep Ocean, Warm Ocean (coral reefs), Lukewarm / Deep Lukewarm, Cold / Deep Cold, Frozen / Deep Frozen Ocean.

**Cave biomes (underground)**
- **Dripstone Caves** — pointed dripstone, lots of copper.
- **Lush Caves** — moss, azalea, glow berries, axolotls, spore blossoms, clay pools. Above-ground azalea trees hint at them.
- **Deep Dark** — sculk, ancient cities, Warden. Below Y 0.
- **Sulfur Caves** (26.2) — sulfur & cinnabar, potent sulfur pools that cause Nausea, geysers/sulfur springs on the surface above, sulfur cubes, cave spiders.

Total: ~65+ Overworld biomes.

## Nether biomes
| Biome | Features |
|---|---|
| Nether Wastes | Classic netherrack; zombified piglins, ghasts, quartz |
| Crimson Forest | Red fungus trees; hoglins, piglins |
| Warped Forest | Teal fungus; endermen; the "safest" Nether biome |
| Soul Sand Valley | Soul sand/soil, fossils; skeletons, ghasts; blue soul fire |
| Basalt Deltas | Basalt, blackstone, magma cubes; hard terrain |

## End biomes
The End (central island), End Highlands (chorus plants, End cities), End Midlands, Small End Islands, End Barrens.

## Structures
### Overworld
| Structure | Biome | Notable contents |
|---|---|---|
| **Village** (plains, desert, savanna, taiga, snowy) | Grassy/arid/cold | Villagers, job sites, chests, iron golem; can become a zombie village (2%) |
| **Pillager outpost** | Plains, desert, savanna, taiga, mountains | Pillagers, caged allays, crossbows, sentry trim |
| **Woodland mansion** | Dark forest | Evokers, vindicators, totems, allays; rare (find with cartographer map) |
| **Desert pyramid** | Desert | TNT trap; 4 chests (diamonds, enchanted books), suspicious sand, dune trim |
| **Jungle pyramid** | Jungle | Tripwire & arrow traps, lever puzzle, wild trim |
| **Swamp hut** | Swamp | Witch + black cat; witch farm spot |
| **Igloo** | Snowy | Hidden basement with zombie villager, golden apple, splash weakness |
| **Ocean monument** | Deep ocean | Guardians, 3 elder guardians, 8 gold blocks, sponges |
| **Ocean ruins** | Oceans | Drowned, buried treasure maps, suspicious sand/gravel (sniffer eggs) |
| **Shipwreck** | Oceans/beaches | Maps to buried treasure, iron, emeralds, coast trim |
| **Buried treasure** | Beaches | Heart of the sea, iron, gold, TNT |
| **Mineshaft** | Underground (+ badlands surface) | Rails, chest minecarts, cave spider spawners, cobwebs |
| **Dungeon (monster room)** | Underground | Zombie/skeleton/spider spawner, 1–2 chests, saddles, music discs |
| **Stronghold** | Underground (128 per world, in rings) | **End portal**, libraries, silverfish, eye trim |
| **Ruined portal** | Anywhere (also Nether) | Obsidian, gold, golden apples; crying obsidian |
| **Ancient city** | Deep dark | Sculk shriekers, Warden risk, **Swift Sneak** books, enchanted golden apples, echo shards, ward & silence trims, disc fragments 5 |
| **Trail ruins** | Taiga, jungles, birch forests | Archaeology: sherds, trims (wayfinder, raiser, shaper, host), relic disc |
| **Trial chambers** | Underground (Y −40 to −20 area) | Trial spawners, breezes, **vaults** (trial keys), ominous vaults (heavy core, Wind Burst), bolt & flow trims |
| **Abandoned camp** (26.3) | Many wooded/wild biomes | Tents, chests, barrels; wheat, bread, leather, axes, arrows, explorer maps |
| **Desert well** | Desert | Suspicious sand (archaeology) |
| **Fossil** | Deserts, swamps, underground | Bone blocks, sometimes diamond ore |
| **Amethyst geode** | Underground | Amethyst clusters (budding amethyst can't be moved) |

### Nether
| Structure | Notes |
|---|---|
| **Nether fortress** | Blazes, wither skeletons, Nether wart, chests with diamonds/horse armor/saddles; rib trim |
| **Bastion remnant** | 4 types: bridge, hoglin stables, housing units, treasure room. Piglins, piglin brutes, magma cube spawners, gold blocks, **netherite upgrade template**, snout trim, Pigstep disc |
| Ruined portal | |
| Nether fossil | Soul sand valley bone structures |

### End
| Structure | Notes |
|---|---|
| Obsidian pillars + exit portal | Central island |
| End gateway | Appears after each dragon kill; throw an ender pearl in to reach outer islands |
| **End city** | Shulkers, purpur, end rods, great loot (diamond gear), spire trim |
| **End ship** | Attached to some End cities; **elytra**, dragon head, brewing stand with potions |

## Finding structures
- Explorer maps: cartographer villagers (ocean monument, woodland mansion, trial chambers, village maps), shipwrecks/ocean ruins (buried treasure), and the new 26.3 explorer maps from abandoned camps.
- Eye of ender → stronghold.
- `/locate structure <name>` and `/locate biome <name>` (cheats).
- Online seed maps (e.g. Chunkbase) use the world seed.

## Archaeology (1.20)
Use a **brush** on suspicious sand/gravel in desert pyramids, desert wells, ocean ruins, and trail ruins. Find **pottery sherds** (20+ designs) to make decorated pots, sniffer eggs, armor trims, emeralds, and more.


---

# 09 — Enchanting & Anvils

## Enchanting table
- Recipe: book + 2 diamonds + 4 obsidian.
- Place **15 bookshelves** one block away (air gap, same level or one above) to reach **level 30** options.
- Cost: shown level requirement, but you only spend 1–3 levels plus 1–3 **lapis lazuli**.
- Options reroll each time you enchant anything (the "enchantment seed").
- Books, tools, weapons, armor can be enchanted. Treasure enchantments never come from the table.
- Chiseled bookshelves don't count as power sources (Java).

## Other enchanting sources
Librarian villagers (books), fishing, chest loot, raid drops, piglin bartering (Soul Speed), trial chamber vaults, ancient cities (Swift Sneak).

## All enchantments (Java)
### Armor
| Enchantment | Max | Applies to | Effect |
|---|---|---|---|
| Protection | IV | All armor | General damage reduction |
| Fire Protection | IV | All armor | Fire damage & burn time |
| Blast Protection | IV | All armor | Explosions & knockback from them |
| Projectile Protection | IV | All armor | Arrows, tridents, fireballs |
| Thorns | III | All (table: chestplate) | Damages attackers; extra durability use |
| Respiration | III | Helmet | Longer underwater breathing |
| Aqua Affinity | I | Helmet | Normal mining speed underwater |
| Feather Falling | IV | Boots | Fall damage reduction |
| Depth Strider | III | Boots | Faster underwater movement |
| Frost Walker* | II | Boots | Freezes water beneath you |
| Soul Speed* | III | Boots | Fast on soul sand/soil (piglin bartering) |
| Swift Sneak* | III | Leggings | Faster sneaking (ancient cities only) |
| Curse of Binding* | I | Armor | Can't remove until death/breaks |

### Melee weapons
| Enchantment | Max | Effect |
|---|---|---|
| Sharpness | V | +damage to all |
| Smite | V | +damage to undead |
| Bane of Arthropods | V | +damage to spiders, bees, silverfish, endermites (+ Slowness) |
| Knockback | II | Extra knockback |
| Fire Aspect | II | Sets target on fire |
| Looting | III | More/rarer mob drops |
| Sweeping Edge | III | Stronger sweep (Java only) |

### Mace (1.21)
| Enchantment | Max | Effect |
|---|---|---|
| Density | V | More smash damage per block fallen |
| Breach | IV | Ignores part of target's armor |
| Wind Burst* | III | Launches you up after a smash hit (ominous vaults) |
Mace can also take Smite, Bane of Arthropods, Fire Aspect, Unbreaking, Mending.

### Spear (1.21.11)
| Enchantment | Max | Effect |
|---|---|---|
| Lunge | III | Forward speed burst on attack |
Spear also accepts common weapon enchantments.

### Tools
| Enchantment | Max | Effect |
|---|---|---|
| Efficiency | V | Faster mining |
| Silk Touch | I | Blocks drop themselves |
| Fortune | III | More drops from ores/crops |
| Unbreaking | III | Chance to not use durability |
| Mending* | I | XP repairs the item |
| Curse of Vanishing* | I | Item disappears on death |

### Bows & crossbows
| Enchantment | Max | Effect |
|---|---|---|
| Power | V | Bow damage |
| Punch | II | Bow knockback |
| Flame | I | Flaming arrows |
| Infinity | I | Never use normal arrows (need 1) |
| Multishot | I | Crossbow fires 3 |
| Piercing | IV | Arrows pass through mobs |
| Quick Charge | III | Faster crossbow reload |

### Trident
| Enchantment | Max | Effect |
|---|---|---|
| Loyalty | III | Returns after throw |
| Riptide | III | Launch yourself in water/rain |
| Channeling | I | Summons lightning on hit during thunderstorms |
| Impaling | V | Extra damage (Java: aquatic mobs; Bedrock: anything in water/rain) |

### Fishing rod
Luck of the Sea III (better treasure), Lure III (faster bites).

\* = treasure enchantment (not from the enchanting table).

## Mutually exclusive groups
- Protection / Fire / Blast / Projectile Protection
- Sharpness / Smite / Bane of Arthropods (and Density / Breach on maces)
- Fortune / Silk Touch
- Infinity / Mending
- Depth Strider / Frost Walker
- Riptide / Loyalty, Riptide / Channeling
- Multishot / Piercing

## Recommended "god" loadouts
- **Sword:** Sharpness V, Looting III, Fire Aspect II, Sweeping Edge III, Knockback (optional), Unbreaking III, Mending.
- **Pickaxe:** Efficiency V, Fortune III *or* Silk Touch, Unbreaking III, Mending.
- **Armor:** Protection IV on all (Blast Prot on one piece for creepers), Unbreaking III, Mending; Helmet: Respiration III + Aqua Affinity; Leggings: Swift Sneak III; Boots: Feather Falling IV, Depth Strider III, Soul Speed III.
- **Bow:** Power V, Punch II, Flame, Infinity (or Mending), Unbreaking III.
- **Trident:** Loyalty III / Riptide III, Impaling V, Channeling, Unbreaking III, Mending.
- **Mace:** Density V or Breach IV, Wind Burst III, Unbreaking III, Mending.
- **Elytra:** Unbreaking III, Mending.

## Anvils
- Combine two items of the same type or item + enchanted book; rename items (costs XP).
- **Prior work penalty**: each anvil use doubles a hidden cost (0 → 1 → 3 → 7 → 15 → 31 levels added). Cost ≥ 40 levels shows **"Too Expensive!"** in Survival.
- Plan merges in a balanced "binary tree" to minimise cost (combine books with each other first).
- Repair with raw material (e.g. diamonds) or two damaged items (+5% bonus durability at the crafting table/grindstone without enchantments).
- Anvils get damaged (chipped → damaged → break) and fall like gravel.

## Grindstone
Removes all non-curse enchantments and returns some XP. Also resets prior work penalty.

## XP farming for enchanting
Mob spawner farms (zombie/skeleton), enderman farms in the End (fastest), gold farms (zombified piglins), guardian farms, smelting large amounts of items (stored XP released when you take them out), trading with villagers.


---

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


---

# 11 — Food, Farming, Animals & Villagers

## Food table (hunger restored / saturation)
| Food | Hunger | Saturation | Notes |
|---|---|---|---|
| Enchanted golden apple | 4 | 9.6 | Regen II 20 s, Absorption IV 2 min, Resistance & Fire Res 5 min; not craftable |
| Golden apple | 4 | 9.6 | Regen II 5 s, Absorption 2 min; cures zombie villagers (with Weakness) |
| Golden carrot | 6 | 14.4 | **Best saturation in the game** |
| Steak / cooked porkchop | 8 | 12.8 | Best common food |
| Cooked mutton / cooked salmon | 6 | 9.6 | |
| Rabbit stew | 10 | 12 | |
| Pumpkin pie | 8 | 4.8 | |
| Cooked chicken | 6 | 7.2 | Raw chicken: 30% chance of Hunger |
| Mushroom stew / beetroot soup | 6 | 7.2 | Doesn't stack |
| Bread | 5 | 6 | |
| Baked potato | 5 | 6 | |
| Cooked cod / cooked rabbit | 5 | 6 | |
| Apple / chorus fruit | 4 | 2.4 | Chorus teleports you |
| Carrot | 3 | 3.6 | |
| Beef / porkchop (raw) | 3 | 1.8 | |
| Cake (per slice, 7 slices) | 2 | 0.4 | Must be placed |
| Cookie | 2 | 0.4 | Toxic to parrots |
| Melon slice | 2 | 1.2 | |
| Sweet / glow berries | 2 | 0.4 | |
| Honey bottle | 6 | 1.2 | Cures Poison |
| Dried kelp | 1 | 0.6 | Fast to eat |
| Rotten flesh | 4 | 0.8 | 80% chance of Hunger |
| Spider eye | 2 | 3.2 | Poison |
| Pufferfish | 1 | 0.2 | Poison, Hunger, Nausea |
| Suspicious stew | 6 | 7.2 | + effect by flower |

## Crops
| Crop | Plant on | Get seeds from | Notes |
|---|---|---|---|
| Wheat | Farmland | Breaking grass | Bread, hay bales, breeding |
| Carrots | Farmland | Zombies, villages, shipwrecks | Plant the carrot itself |
| Potatoes | Farmland | Zombies, villages | Poisonous potato (2%) |
| Beetroot | Farmland | Village farms, chests | Red dye, soup |
| Melon / Pumpkin | Farmland, fruit grows on adjacent dirt | Jungle/village chests, natural patches | Stem stays |
| Sugar cane | Sand/dirt next to water | Riverbanks | Grows 3 tall; paper & sugar |
| Cactus | Sand | Deserts | Can't touch blocks on sides; cactus flowers (1.21.5) |
| Bamboo | Grass/dirt/sand | Jungles | Fastest growing; scaffolding, fuel |
| Cocoa beans | Jungle logs | Jungle | Brown dye, cookies |
| Nether wart | Soul sand | Fortresses | Brewing |
| Sweet berries | Grass/dirt | Taiga | Thorny bush |
| Glow berries | Hang from cave vines | Lush caves | Light source |
| Kelp | Underwater | Oceans | Dried kelp fuel |
| Chorus fruit | End stone | End | Purpur |
| Mushrooms | Low light / mycelium / podzol | Dark areas | Huge mushrooms with bone meal |
| Torchflower / pitcher plant | Farmland | Sniffer | Decorative |

**Farming facts**
- Farmland needs water within 4 blocks horizontally to stay hydrated.
- Crops need light ≥ 9 to grow.
- **Bone meal** (from bones or composter) instantly advances growth.
- Villager **farmers** harvest and replant crops automatically (used in auto-farms).
- **Bees** pollinate crops, making them grow faster.
- Random tick speed (default 3) controls growth rate.

## Breeding & taming
| Animal | Food |
|---|---|
| Cows, sheep, mooshrooms, goats | Wheat |
| Pigs | Carrot, potato, beetroot |
| Chickens | Any seeds |
| Rabbits | Dandelion, carrot, golden carrot |
| Horses, donkeys | Golden apple / golden carrot (tame by riding until hearts) |
| Llamas | Hay bale |
| Wolves | Tame with bones; breed with meat |
| Cats/ocelots | Raw cod, raw salmon |
| Parrots | Tame with seeds (can't breed) |
| Turtles | Seagrass |
| Pandas | Bamboo (need 8+ bamboo nearby) |
| Foxes | Sweet/glow berries (babies trust you) |
| Bees | Any flower |
| Axolotls | Bucket of tropical fish |
| Frogs | Slimeball |
| Striders | Warped fungus |
| Hoglins | Crimson fungus |
| Camels | Cactus |
| Sniffers | Torchflower seeds |
| Armadillos | Spider eye |
| Nautilus | Pufferfish (taming) |

Babies grow up in 20 minutes; feeding them speeds this up. **Golden dandelion** (26.1) stops a baby from aging (use again to resume). Breeding cooldown: 5 minutes.

## Villagers
### Professions and job site blocks
| Profession | Job block | Best trades |
|---|---|---|
| Armorer | Blast furnace | Diamond armor (enchanted) |
| Butcher | Smoker | Buys meat, sells cooked food |
| Cartographer | Cartography table | Explorer maps, banner patterns |
| Cleric | Brewing stand | Ender pearls, redstone, glowstone, lapis |
| Farmer | Composter | Golden carrots, glistering melons; buys crops for emeralds |
| Fisherman | Barrel | Buys string/coal/fish; sells campfire, enchanted fishing rod |
| Fletcher | Fletching table | Buys sticks (easy emeralds!); sells arrows, tipped arrows |
| Leatherworker | Cauldron | Saddles, leather armor |
| Librarian | Lectern | **Enchanted books (incl. Mending)**, bookshelves, glass, clocks, compasses |
| Mason | Stonecutter | Terracotta, quartz blocks, dripstone |
| Shepherd | Loom | Wool, beds, banners, paintings |
| Toolsmith | Smithing table | Diamond tools (enchanted) |
| Weaponsmith | Grindstone | Diamond swords/axes (enchanted) |
| Nitwit | — | Can't work (green coat) |
| Unemployed | — | Will claim a free job block |

### Trading mechanics
- 5 levels: Novice → Apprentice → Journeyman → Expert → Master (badge colour stone → iron → gold → emerald → diamond).
- A villager's trades are **locked** after you trade once. Before that, break and replace the job block to reroll (great for getting Mending librarians).
- Villagers restock up to twice per day at their job site.
- **Prices drop** with: Hero of the Village, curing the villager from zombie villager (huge, permanent discount), good gossip. Prices rise with high demand or if you hurt villagers.
- In recent Java versions, trade rebalance experiments change librarian books by biome — check your version.

### Breeding villagers
Need **beds** (one free bed per baby) and food in inventory (3 bread, 12 carrots/potatoes/beetroots). Villagers share food. A village forms around claimed beds, a bell (meeting point), and job sites.

### Zombie villagers
Splash/lingering Potion of Weakness + golden apple → cures in 3–5 min (faster near iron bars and beds). Cured villagers give big discounts.

### Raids
Entering a village with **Bad Omen** (now obtained by drinking an ominous bottle) starts a raid: waves of pillagers, vindicators, evokers, witches, ravagers (and vexes). Win to get **Hero of the Village**. More waves on higher difficulty.

## Iron golems & village defence
Iron golems spawn when ≥ 5 villagers gossip/panic near a zombie and have slept/worked recently (rules vary by version). Iron farms exploit this.

## Fishing
Cast in water; bites happen faster in rain and with Lure. 
- Fish (85%), junk (10%), treasure (5%) at base. Treasure includes enchanted books, bows, fishing rods, name tags, nautilus shells, saddles.
- AFK fish farms (Luck of the Sea + Mending rod) are popular.


---

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


---

# 13 — Commands & Technical Reference

Commands need cheats enabled (world settings / "Open to LAN → Allow Cheats") or operator permissions on a server. Type `/` in chat. Press **Tab** for auto-complete — the best way to get exact syntax for your version.

## Target selectors
| Selector | Targets |
|---|---|
| `@p` | Nearest player |
| `@a` | All players |
| `@r` | Random player |
| `@s` | The executor (yourself) |
| `@e` | All entities |
| `@n` | Nearest entity (1.21+) |

Arguments: `@e[type=zombie,distance=..10,limit=3,sort=nearest]`, `@a[gamemode=survival]`, `@e[tag=boss]`, `@a[scores={kills=5..}]`, `@e[name="Bob"]`, `@a[level=30..]`, `x/y/z/dx/dy/dz` boxes.

Coordinates: absolute `100 64 -20`, relative `~ ~1 ~` (from the executor), local `^ ^ ^5` (5 blocks in front of where you look).

## Most-used commands
| Command | Example | What it does |
|---|---|---|
| `/gamemode` | `/gamemode creative` | survival / creative / adventure / spectator |
| `/difficulty` | `/difficulty hard` | peaceful / easy / normal / hard |
| `/time` | `/time set day` (1000), `night` (13000), `noon`, `midnight` | Change time |
| `/weather` | `/weather clear 6000` | clear / rain / thunder |
| `/tp` or `/teleport` | `/tp @s 0 100 0`, `/tp Jean Steve` | Teleport |
| `/give` | `/give @s diamond_sword[enchantments={sharpness:5}] 1` | Give items (components syntax since 1.20.5) |
| `/clear` | `/clear @s dirt` | Remove items |
| `/effect` | `/effect give @s night_vision infinite 0 true` | Apply effects; `effect clear @s` |
| `/enchant` | `/enchant @s sharpness 5` | Enchant held item (respects max level) |
| `/xp` / `/experience` | `/xp add @s 30 levels` | XP |
| `/kill` | `/kill @e[type=item]` | Kill entities (clear dropped items) |
| `/summon` | `/summon lightning_bolt ~ ~ ~` | Spawn entity |
| `/setblock` | `/setblock ~ ~ ~ diamond_block` | Place one block |
| `/fill` | `/fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 stone replace dirt` | Fill a region (max 32,768 blocks) |
| `/clone` | `/clone x1 y1 z1 x2 y2 z2 x y z` | Copy regions |
| `/locate` | `/locate structure village_plains`, `/locate biome cherry_grove` | Find nearest structure/biome |
| `/seed` | `/seed` | Show world seed |
| `/spawnpoint` | `/spawnpoint @s ~ ~ ~` | Set player spawn |
| `/setworldspawn` | | World spawn |
| `/gamerule` | `/gamerule keepInventory true` | Change rules (see below) |
| `/tellraw`, `/title`, `/say`, `/msg` | `/title @a title {"text":"Hello"}` | Messages |
| `/execute` | `/execute as @a at @s run summon tnt ~ ~ ~` | Run commands as/at entities with conditions (`if`, `unless`, `positioned`, `store`) |
| `/scoreboard` | `/scoreboard objectives add kills playerKillCount` | Track stats, sidebar displays |
| `/team` | `/team add red` | Teams, colours, friendly fire |
| `/data` | `/data get entity @s Pos` | Read/modify NBT data |
| `/item` | `/item replace entity @s armor.head with carved_pumpkin` | Edit slots |
| `/attribute` | `/attribute @s minecraft:scale base set 2` | Change attributes (scale since 1.20.5) |
| `/function` | `/function mypack:start` | Run data pack functions |
| `/particle`, `/playsound` | | Effects |
| `/place` | `/place structure ancient_city` | Generate features/structures |
| `/fillbiome` | | Change biomes in an area |
| `/ride` | `/ride @s mount @e[type=pig,limit=1]` | Mount entities |
| `/damage` | | Deal typed damage |
| `/random` | `/random value 1..6` | Random numbers |
| `/tick` | `/tick freeze`, `/tick rate 40` | Control game speed (Java) |
| `/worldborder` | `/worldborder set 1000` | Border |
| `/reload` | | Reload data packs |
| `/transfer` | | Send player to another server (1.20.5) |
| `/forceload` | | Keep chunks loaded |
| `/spreadplayers` | | Randomly scatter players (UHC games) |

## Game rules (common)
Since Java 1.21.11 game rules use registry-style snake_case IDs and a few were renamed — use Tab completion to see the exact names in your version. Classic names (still used in Bedrock and older Java):

| Rule | Default | Effect |
|---|---|---|
| `keepInventory` | false | Keep items/XP on death |
| `doDaylightCycle` | true | Time passes |
| `doWeatherCycle` | true | Weather changes |
| `doMobSpawning` | true | Natural spawns |
| `mobGriefing` | true | Creepers break blocks, endermen pick up blocks, villagers farm |
| `doFireTick` | true | Fire spreads |
| `naturalRegeneration` | true | Heal from hunger |
| `playersSleepingPercentage` | 100 | % needed to skip night (Java) |
| `doInsomnia` | true | Phantoms |
| `randomTickSpeed` | 3 | Crop/plant growth speed |
| `showDeathMessages` | true | |
| `doImmediateRespawn` | false | Skip death screen |
| `announceAdvancements` | true | |
| `spawnRadius` | 10 | Random spawn spread |
| `commandBlockOutput` | true | |
| `fallDamage`, `fireDamage`, `drowningDamage`, `freezeDamage` | true | |
| `doTileDrops`, `doMobLoot`, `doEntityDrops` | true | |

## F3 debug screen (Java)
- **XYZ** coordinates, block you're looking at, chunk, facing, biome, light levels, local difficulty, FPS, memory, TPS.
- Hotkeys: `F3+B` hitboxes, `F3+G` chunk borders, `F3+H` advanced tooltips (IDs, durability), `F3+T` reload resource packs, `F3+N` toggle creative/spectator, `F3+C` copy location, `F3+I` copy block/entity data, `F3+D` clear chat, `F3+A` reload chunks, `F3+P` pause on lost focus, `F3+F4` game mode switcher, `F3+Q` help list.
- Newer Java versions let you customise debug overlay entries.

## Bedrock specifics
- Coordinates shown via world setting.
- Commands similar but some syntax differs (e.g. `/give @s diamond_sword 1 0 {"enchantments"...}` uses different JSON; `/tp` and `/execute` follow the newer Java-like syntax since 1.19.50).
- Add-ons: behavior packs + resource packs. Marketplace for official content.

## Data packs & resource packs (Java)
- **Resource pack**: textures, models, sounds, languages, shaders (core shaders). Folder with `pack.mcmeta` + `assets/`.
- **Data pack**: functions (`.mcfunction` files of commands), advancements, loot tables, recipes, tags, predicates, item modifiers, world-gen (custom biomes/dimensions), enchantments, damage types, and (26.x) new registries like sulfur cube archetypes. Folder with `pack.mcmeta` + `data/<namespace>/...`.
- `load` and `tick` function tags run functions at load and every tick.

### Example function file `data/demo/function/hello.mcfunction`
```
say Hello from a data pack!
effect give @a minecraft:speed 10 1
```

## Modding (Java)
| Loader | Notes |
|---|---|
| **Fabric** | Lightweight, updates fast (Sodium, Iris shaders, Lithium) |
| **NeoForge** | Successor to Forge for big content mods (Create, Mekanism, Applied Energistics) |
| **Forge** | The original big loader; still used for older versions |
| **Quilt** | Fabric fork |
| OptiFine | Old performance/shader mod, largely replaced by Sodium + Iris |

Popular sites: Modrinth, CurseForge. Launchers: Prism Launcher, CurseForge app, Modrinth App, official launcher.

Unobfuscated Java builds since 26.1 make modding easier (readable code names).

## Servers
- Java server software: Vanilla `server.jar`, **Paper** (performance + plugins), Purpur, Spigot, Fabric server, NeoForge server. Proxies: Velocity, BungeeCord.
- Default port: **25565** (Java), **19132** UDP (Bedrock).
- `server.properties`: `difficulty`, `gamemode`, `max-players`, `online-mode`, `pvp`, `view-distance`, `simulation-distance`, `white-list`/allowlist, `motd`, `level-seed`.
- From 26.3, new servers default to an **allowlist** (you must add players or turn it off).
- Cross-play Java ↔ Bedrock: GeyserMC + Floodgate plugins.
- Famous servers: Hypixel, 2b2t (oldest anarchy server), Wynncraft, CubeCraft, The Hive (Bedrock), Mineplex (historic).

## Seeds
A seed is a number (or text converted to a number) that determines world generation. Same seed + same version = same world. Tools like Chunkbase show biomes and structures for a seed. In 2020 the community famously recovered the seed of the classic title-screen panorama and the original `pack.png` image using reverse-engineering.


---

# 14 — Tips, Tricks, Glossary & Fun Facts

## Survival tips
1. **Bed = checkpoint**. Always carry one when exploring far.
2. Use **boats** to trap/transport villagers and mobs; boats on ice are very fast.
3. Pillar up with blocks (jump + place) to escape mobs; "nerd pole".
4. Sprint-jump is the fastest way to move on foot.
5. **MLG water bucket**: place water just before landing to cancel fall damage.
6. Put a block in front of a lava source before digging toward it; fire resistance potions are life-savers in the Nether.
7. Gold armor piece in the Nether = piglins stay neutral.
8. Pumpkin head in the End = endermen won't aggro.
9. Use **beds to blow up** the Ender Dragon or mine ancient debris (they explode in Nether/End).
10. Fill a **shulker box** with essentials before big trips; shulker boxes keep their contents when broken.
11. **Ender chest** + shulker boxes = huge safe storage you can access anywhere.
12. Put a **campfire** under a beehive to harvest honey safely.
13. Cure zombie villagers for a big permanent discount (curing the same villager repeatedly no longer stacks in modern Java).
14. Trap a **Mending** librarian early.
15. Use **looms and cartography tables** to mark maps with banners.
16. **Nether highways**: travel 1 block in the Nether = 8 in the Overworld. Build on the Nether roof (Y 128+) for safety (Java).
17. Hold Shift on edges to avoid falling (sneaking prevents walking off).
18. Dropped items can be magnet-picked by **hoppers** and **allays**.
19. Light up a 128-block radius around AFK spots to boost farm efficiency.
20. Use a **sulfur cube** with a block in it as a physics toy, bounce pad, or minecart helper (26.2).
21. **Cushions** (26.3) let you sit; **straw beds** skip nights without overwriting your real spawn bed.
22. Craft **name tags** now (paper + nugget) to keep favourite mobs from despawning.

## Building tips
- Avoid flat walls: add depth with stairs, slabs, trapdoors, walls, and pillars.
- Use a **palette** of 3–5 blocks with contrast (e.g. spruce + stone bricks + dark oak).
- Roofs: use stairs at 45° and overhangs.
- Gradients: blend blocks (stone → andesite → cobblestone → mossy) for natural looks.
- Use light sources creatively (hidden glowstone under carpet, lanterns, candles, froglights).
- Terraform landscapes using a "scale" approach; use vines, leaves, moss for detail.
- New decorative toys: shelves (Copper Age), cushions and colourful wool/concrete stairs and slabs (26.3), pale oak and poplar woods.

## Glossary (community slang)
| Term | Meaning |
|---|---|
| **AFK** | Away from keyboard (AFK farms run while you idle) |
| **Biome** | Region type with distinct terrain/climate/mobs |
| **Chunk** | 16×16 column of blocks (full height); unit of loading |
| **Spawn chunks** | Area near world spawn that stays loaded (Java; configurable since 1.20.5) |
| **Mob cap** | Max number of naturally spawned mobs |
| **Tick / TPS** | Game update (20 per second) / ticks per second (lag if < 20) |
| **Slime chunk** | Chunk where slimes spawn underground |
| **Strip mining / branch mining** | Long 1×2 tunnels to find ores |
| **Bed mining** | Exploding beds to expose ancient debris |
| **Speedrun** | Beating the game as fast as possible |
| **MLG** | Clutch trick (e.g. water bucket landing) |
| **Pog / goated** | General slang for impressive |
| **Griefing** | Destroying others' builds |
| **Anarchy server** | No rules (e.g. 2b2t) |
| **SMP** | Survival Multiplayer (e.g. Hermitcraft, Dream SMP) |
| **UHC** | Ultra Hardcore — no natural regeneration PvP mode |
| **Parkour** | Jumping obstacle courses |
| **Bedwars / Skywars** | Popular PvP minigames (Hypixel) |
| **Redstoner / technical player** | Specialist in redstone & farms |
| **Seed** | World-generation number |
| **Snapshot / Preview** | Test versions (Java / Bedrock) |
| **Drop** | Smaller themed update (since 2024) |
| **Vanilla** | Unmodded game |
| **Modpack** | Bundle of mods (e.g. All the Mods, RLCraft, SkyFactory) |
| **Texture pack / resource pack** | Visual changes |
| **Shaders** | Advanced lighting effects (Iris/OptiFine, Vibrant Visuals on Bedrock) |
| **Creeper, aw man** | Famous 2011 parody song "Revenge" |
| **Herobrine** | Legendary fake ghost of Notch's "brother" |
| **Cobblestone generator** | Lava + water setup for infinite cobble |
| **Infinite water source** | 2×2 or 3-in-a-row water sources refill |
| **Hopper clock / zero-tick** | Redstone terms |
| **Stack** | 64 items (16 for eggs, snowballs, signs, ender pearls, buckets of honey; 1 for tools) |
| **Double chest** | 54 slots (= 6 stacks × 9) |
| **Shulker box** | Portable 27-slot box |
| **Ender chest** | Personal storage accessible everywhere |

## Useful numbers
- Stack size: 64 (most), 16, or 1.
- Chest: 27 slots; double chest: 54; shulker box: 27; barrel: 27; hopper: 5; dispenser/dropper: 9.
- Player inventory: 36 slots + 4 armor + 1 off-hand.
- World border: ±29,999,984 blocks (Java). Players can reach ±30 million.
- Total world area ≈ 3.6 quadrillion square blocks.
- The Far Lands (terrain glitch at ±12,550,821) existed before Beta 1.8 — famous YouTuber KurtJMac walked toward them for years ("Far Lands or Bust").
- Max enchanting level from the table: 30. Max level number: 2,147,483,647 (via commands).
- Day length: 24,000 ticks = 20 minutes.

## Fun facts
- Minecraft was originally named "Cave Game", then "Minecraft: Order of the Stone".
- The **creeper** came from a coding mistake: Notch swapped height/length values when modelling a pig.
- The **Enderman** sounds are reversed and distorted human speech ("Hi", "Hello", "What's up").
- Ghast sounds were made by C418's cat.
- The Ender Dragon fight was added in the final weeks before the 1.0 release in 2011, along with the End Poem.
- Splash text on the title screen has hundreds of random lines.
- The "jeb_" sheep and "Dinnerbone" upside-down mobs are developer tributes.
- The official **Minecraft Movie (2025)** popularised in-game memes like "chicken jockey" and the "Lava Chicken" song — which became a music disc in 1.21.7.
- The world isn't truly infinite: the world border stops at 30 million blocks.
- Diamond ore was once called the rarest ore, but **ancient debris** and **emerald ore** are rarer.
- Minecraft Education has been used to teach coding, chemistry, history, and even in UN projects ("Block by Block" urban planning).


---

