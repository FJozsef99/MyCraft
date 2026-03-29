import pygame

sprites = []
loaded = {}

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.transform.scale(pygame.image.load(image), (32,32))
            loaded[image] = self.image

        # hitbox setting
        self.rect = self.image.get_rect(topleft=(x, y))

        sprites.append(self)

    def delete(self):
        sprites.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
