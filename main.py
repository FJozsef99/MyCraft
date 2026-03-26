import pygame
import input
from player import Player
from sprite import sprites, Sprite
from map import TileKind, Map
from world_gen import World

pygame.init()

pygame.display.set_caption("MyCraft")


w1 = World(80, 50, 33)
World.print_noise_map(w1)
for row in World.get_tiled_map(w1):
    for tile in row:
        print(tile, end="")
    print()


screen = pygame.display.set_mode((1920, 1080))
clear_c = (20, 151, 20)
running = True
player = Player("images/player.png", 0 , 0)
tile_kinds = [
    TileKind("dirt", "images/dirt.png", False),
    TileKind("grass", "images/grass.png", False),
    TileKind("wood", "images/wood.png", False)
]

map = Map("maps/start.map", tile_kinds, 32)
#Sprite("images/tree.png",0,0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            input.keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            input.keys_down.remove(event.key)
    #update
    player.update()


    #draw
    screen.fill(clear_c)

    map.draw(screen)

    for s in sprites:
        s.draw(screen)
    pygame.display.flip()

    #pygame.time.delay(1)



pygame.quit()