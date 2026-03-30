import random
import pygame

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

WORLD_SIZE_X = 58
WORLD_SIZE_Y = 32

MAP_PATH = "maps/start.map"
PLAYER_PATH = "images/player.png"
PLAYER_START_X = 0
PLAYER_START_Y = 0

#RANDOM_SEED = random.randint(1, 900000)
TILING_WEIGHTS = [30, 40, 100, 40]

TILE_SIZE = 32

TILE_PATHS = ["images/water.png", "images/sand.png", "images/grass.png", "images/stone.png"]

# Terrain types
OCEAN = 0
SAND = 1
GRASS = 2
STONE = 3
# GRASS = 4
# MOUNTAIN = 5
# SNOW = 6

# List of all terrain type, ordered from lower height to higher height
ALL_TERRAIN_TYPES = [OCEAN, SAND, GRASS, STONE]#, BEACH, GRASS, MOUNTAIN, SNOW]



