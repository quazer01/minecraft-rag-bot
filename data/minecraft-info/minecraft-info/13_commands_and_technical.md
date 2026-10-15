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
