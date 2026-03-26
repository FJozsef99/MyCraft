import pygame
from sprite import Sprite
from input import is_key_pressed
from config import *


class Player(Sprite):
    def __init__(self):
        super().__init__(PLAYER_PATH, PLAYER_X, PLAYER_Y)
        self.movement_speed = 5

    def update(self):
        if is_key_pressed(pygame.K_w):
            self.y -= self.movement_speed
        if is_key_pressed(pygame.K_a):
            self.x -= self.movement_speed
        if is_key_pressed(pygame.K_s):
            self.y += self.movement_speed
        if is_key_pressed(pygame.K_d):
            self.x += self.movement_speed
