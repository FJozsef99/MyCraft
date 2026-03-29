import pygame
import input
from player import Player
from sprite import sprites, Sprite
from map import Map
from world_gen import World
from config import *

# Window init
pygame.init()
pygame.display.set_caption("MyCraft")

# World gen with configs
w1 = World(WORLD_SIZE_X, WORLD_SIZE_Y, RANDOM_SEED)
# World.print_noise_map(w1) #debug

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# clear_c = (20, 151, 20)
running = True

game_map = Map(TILE_SIZE)
player = Player(PLAYER_PATH, PLAYER_X, PLAYER_Y, game_map.obstacles)
# Sprite("images/tree.png",0,0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)
    # update
    player.update()

    # draw
    # screen.fill(clear_c)

    game_map.draw(screen)

    for s in sprites:
        s.draw(screen)
    pygame.display.flip()

    pygame.time.delay(1)

pygame.quit()
