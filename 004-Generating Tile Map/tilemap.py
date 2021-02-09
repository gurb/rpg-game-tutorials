import pygame
import random

# dimension of each tiles
TILE_SIZE = 32

# texture of colors
YELLOW  = (255, 255, 0)
RED     = (255, 0, 0)
BLUE    = (0 , 0, 255)
GREEN   = (0, 255, 0)
BROWN   = (160, 82, 45)

def create_texture(color):
    image = pygame.Surface((TILE_SIZE, TILE_SIZE))
    image.fill(color)
    return image

# 0x0 -> grass
# 0xb -> dirt
textures = {
    0x0 : create_texture(GREEN),
    0xb : create_texture(BROWN)
}

tiles = [0x0, 0xb]

# generate with tiles randomly
def generate_map(width, height, tilesize = TILE_SIZE):
    map_data = []
    for i in range(height // tilesize):
        map_data.append([])
        for j in range(width // tilesize):
            rand_index = random.randint(0,1)
            # convert to hex from string value
            tile = int(hex(tiles[rand_index]), 16)
            map_data[i].append(tile)
    return map_data


def draw_map(screen, map_data):
    MAP_HEIGHT = len(map_data) 
    MAP_WIDTH = len(map_data[0])
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            screen.blit(textures[map_data[row][col]],
                        (col*TILE_SIZE, row*TILE_SIZE))        
