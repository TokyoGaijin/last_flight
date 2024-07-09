import pygame

class Bullet:
    def __init__(self, surface, startX, startY, dir, color = (255, 0, 0)):
        self.surface = surface
        self.dir = "up"
        self.color = color
        self.rect = pygame.Rect(startX, startY, 8, 8)

    def update(self):
        if self.dir == "up":
            self.rect.y -= 10
        if self.dir == "down":
            self.rect.y += 10

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)