import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, sprites_group, pos, dim, col):
        self.groups = sprites_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface(dim)
        self.image.fill(col)

        self.rect = self.image.get_rect()
        self.rect.center = pos
