import pygame
from animator import Animator
import os

class Explosion:
    def __init__(self, surface, source_x, source_y):
        self.surface = surface
        self.kaboom = Animator(
            self.surface,
            source_x,
            source_y,
            8,
            [pygame.image.load(os.path.join("sprite_assets", f"generic_explosion_{i}.png")) for i in range(0, 8)]
        )

    def update(self):
        self.kaboom.animate()
        self.kaboom.draw()