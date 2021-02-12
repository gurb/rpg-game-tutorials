import pygame
import random

from player import Player
from tilemap import *
from camera import Camera

# we initialize pygame module
pygame.init()

class Entity(pygame.sprite.Sprite):
    def __init__(self, sprites_group, pos, dim, col):
        self.groups = sprites_group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface(dim)
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

clock = pygame.time.Clock()

# create a surface represent our window
screen = pygame.display.set_mode((640, 480))

sprites_group = pygame.sprite.Group()

player = Player(sprites_group, (0,0), (25,25), (0,0,255))

map_data = generate_map(1024, 1024)

camera = Camera(player, 640, 480)

e = Entity(sprites_group, (32,32), (32,32), (255,0,255))

def main():
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        camera.scroll()

        # draw
        screen.fill((255,255,255))
        draw_map(screen, map_data, camera)
        for sprite in sprites_group:
             screen.blit(sprite.image, (sprite.rect.topleft + camera.offset))
        # print(MAP_POS)

        # update
        
        sprites_group.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()

pygame.quit()
