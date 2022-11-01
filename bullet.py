import pygame

class Bullet():
    def __init__(self, x ,y , radius, color, direction, step):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.step = step * direction

    def draw (self,screen):
        pygame.draw.circle (screen, self.color, (self.x, self.y) ,self.radius)


