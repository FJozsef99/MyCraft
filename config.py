import random
import pygame

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

WORLD_SIZE_X = 58
WORLD_SIZE_Y = 32

MAP_PATH = "maps/start.map"
PLAYER_PATH = "images/player.png"
PLAYER_X = 0
PLAYER_Y = 0

RANDOM_SEED = random.randint(1, 900000)
WEIGHTS1 = [30, 50, 100]

TILE_SIZE = 32

TILE_PATHS = ["images/dirt.png", "images/grass.png", "images/wood.png"]

# Terrain types
OCEAN3 = 0
OCEAN2 = 1
OCEAN1 = 2
# BEACH = 3
# GRASS = 4
# MOUNTAIN = 5
# SNOW = 6

# List of all terrain type, ordered from lower height to higher height
ALL_TERRAIN_TYPES = [OCEAN3, OCEAN2, OCEAN1]#, BEACH, GRASS, MOUNTAIN, SNOW]



