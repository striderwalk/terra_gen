from enum import Enum


class TILES(Enum):
    empty = 0
    water = 1
    shallow_water = 2
    sand = 3
    grass = 4
    forest = 5
    mountains = 6
    tall_mountains = 7
    snowy_mountains = 8


neighbour_map = {
    TILES.water: {
        TILES.water: 3,
        TILES.shallow_water: 3,
    },
    TILES.shallow_water: {
        TILES.water: 3,
        TILES.sand: 1,
        TILES.shallow_water: 1,
    },
    TILES.sand: {
        TILES.shallow_water: 1,
        TILES.sand: 1,
        TILES.grass: 1,
    },
    TILES.grass: {
        TILES.sand: 1,
        TILES.grass: 1,
        TILES.forest: 1,
    },
    TILES.forest: {
        TILES.grass: 1,
        TILES.forest: 2,
        TILES.mountains: 1,
    },
    TILES.mountains: {TILES.forest: 1, TILES.mountains: 1, TILES.tall_mountains: 1},
    TILES.tall_mountains: {
        TILES.mountains: 1,
        TILES.tall_mountains: 1,
        TILES.snowy_mountains: 1,
    },
    TILES.snowy_mountains: {TILES.snowy_mountains: 1, TILES.tall_mountains: 2},
}


COLOURS = {
    TILES.water: (0, 0, 100),
    TILES.shallow_water: (0, 0, 200),
    TILES.sand: (200, 200, 0),
    TILES.grass: (0, 200, 0),
    TILES.forest: (0, 100, 0),
    TILES.mountains: (175, 175, 175),
    TILES.tall_mountains: (100, 100, 100),
    TILES.snowy_mountains: (255, 255, 255),
}
