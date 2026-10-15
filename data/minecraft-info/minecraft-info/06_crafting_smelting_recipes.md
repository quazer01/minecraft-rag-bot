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
