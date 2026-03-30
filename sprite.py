import pygame

sprites = []
loaded = {}


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        if image_path in loaded:
            self.image = loaded[image_path]
        else:
            self.image = pygame.transform.scale(pygame.image.load(image_path), (32, 32))
            loaded[image_path] = self.image

        # self.x = x
        # self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))

        sprites.append(self)

    def delete(self):
        sprites.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
