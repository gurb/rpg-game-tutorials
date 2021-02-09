import pygame
import random

# we initialize pygame module
pygame.init()

# create a surface represent our window
screen = pygame.display.set_mode((640, 480))

def main():
    running = True
    # the game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # draw
        screen.fill((255,255,255))
        pygame.draw.circle(screen, (255,0,0), (random.randint(0, 640), 240), 20)
        
        # update
        pygame.display.flip()

if __name__ == "__main__":
    main()

pygame.quit()
