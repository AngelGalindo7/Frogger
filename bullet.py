import pygame, constants

# pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))

def create_bullet(self):
    return Bullet(pygame.mouse.get_)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

    def update(self):
        self.rect.x += 5
