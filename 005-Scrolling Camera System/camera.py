import pygame
from pygame.math import Vector2

class Camera:
    def __init__(self, target, width, height):
        self.width = width
        self.height = height
        self.camera = Vector2(target.pos.x, target.pos.y)
        self.target = target
        self.offset = Vector2(0,0)

    def scroll(self):
        self.pointTarget = self.target.pos - self.camera
        self.camera += self.pointTarget
        self.offset = -self.camera + Vector2(self.width/2, self.height/2)
