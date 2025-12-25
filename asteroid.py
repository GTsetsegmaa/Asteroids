import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super.__init__()
    
    def draw(self, screen):
        pygame.draw.circle(surface, "white", self, self.radius, LINE_WIDTH)

