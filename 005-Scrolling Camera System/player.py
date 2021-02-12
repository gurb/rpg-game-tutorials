import pygame
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, sprites_group, pos, dim, col):
        self.groups = sprites_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface(dim)
        self.image.fill(col)

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.vel = Vector2(0,0)

        self.pos = Vector2(pos)

    def update(self):
        self.get_event()
        self.rect.center = self.pos

    def get_event(self):
        keys = pygame.key.get_pressed()
        is_press = any(keys)
        if keys[pygame.K_w]:
            self.v = (0, -5)
            self.move(self.v)
        if keys[pygame.K_s]:
            self.v = (0, +5)
            self.move(self.v)
        if keys[pygame.K_a]:
            self.v = (-5, 0)
            self.move(self.v)
        if keys[pygame.K_d]:
            self.v = (+5, 0)
            self.move(self.v)
        if is_press is False:
            self.v = (0,0)

    def move(self, v):
        self.pos.x += v[0]
        self.pos.y += v[1] 
