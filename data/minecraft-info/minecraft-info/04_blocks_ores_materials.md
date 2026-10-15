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
