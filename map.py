import pygame

from config import *
import file_handler
from obstacle import Obstacle


class Map:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.tile_images = []
        self.obstacles = pygame.sprite.Group()

        for s in TILE_PATHS:
            img = pygame.transform.scale(pygame.image.load(s), (TILE_SIZE, TILE_SIZE))
            self.tile_images.append(img)

        # Load map file r:read
        map_data = file_handler.file_loader(MAP_PATH)

        # Load tile numbers from map_data into [self.tiles]
        self.tiles = []
        for y, line in enumerate(map_data.split("\n")):
            row = []
            for x, tile_number in enumerate(line):
                if tile_number == '2':
                    self.obstacles.add(Obstacle("images/wood.png", x * tile_size, y * tile_size))
                else:
                    row.append(int(tile_number))
            self.tiles.append(row)

    # Draws the tiles on screen
    def draw(self, screen):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                location = (x * self.tile_size, y * self.tile_size)
                image = self.tile_images[tile]
                screen.blit(image, location)
