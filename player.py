import pygame
from sprite import Sprite
from input import is_key_pressed


class Player(Sprite):
    def __init__(self, image, x, y, obstacles):
        super().__init__(image, x, y)
        self.movement_speed = 5
        self.obstacles = obstacles

    def update(self):
        dx = 0
        dy = 0

        if is_key_pressed(pygame.K_w):
            dy -= self.movement_speed
        if is_key_pressed(pygame.K_s):
            dy += self.movement_speed
        if is_key_pressed(pygame.K_a):
            dx -= self.movement_speed
        if is_key_pressed(pygame.K_d):
            dx += self.movement_speed

        # Move horizontally
        self.rect.x += dx
        if pygame.sprite.spritecollide(self, self.obstacles, False):
            self.rect.x -= dx

        # Move vertically
        self.rect.y += dy
        if pygame.sprite.spritecollide(self, self.obstacles, False):
            self.rect.y -= dy
