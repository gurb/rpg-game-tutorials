import pygame
import random

from player import Player

# we initialize pygame module
pygame.init()

# create a surface represent our window
screen = pygame.display.set_mode((640, 480))

sprites_group = pygame.sprite.Group()

player = Player(sprites_group, screen.get_rect().center, (25,25), (0,0,255))

def main():
    running = True
    # the game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # draw
        screen.fill((255,255,255))
        sprites_group.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()

pygame.quit()
