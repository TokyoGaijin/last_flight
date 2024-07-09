import pygame
import os
from animator import Animator
from enum import Enum

# Add a STATE class if necessary
# Delete the import to free memory if unused

class Enemy:
    def __init__(self, surface, startX, startY):
        self.surface = surface
        self.live_anim = Animator(
            self.surface,
            startX,
            startY,
            2,
            [pygame.image.load(os.path.join("sprite_assets", f"enemy_1_{i}.png")) for i in range(0, 2)]
        )
        self.is_dying = False
        self.is_alive = True

        self.explosion = Animator(
            self.surface,
            startX,
            startY,
            8,
            [pygame.image.load(os.path.join("sprite_assets", f"generic_explosion_{i}.png")) for i in range(0, 8)]
        )
        self.rect = pygame.Rect(startX, startY, 64, 64)
        self.hp = 100
        self.speed = 3

    def update(self):
        self.is_dying = True if self.hp <= 0 else False
        self.rect.y += self.speed if not self.is_dying else self.speed == 0

        if self.is_dying:
            self.explosion.animate()
        else:
            self.live_anim.animate()

        self.live_anim.play_x, self.live_anim.play_y = self.rect.x, self.rect.y
        self.explosion.play_x, self.explosion.play_y = self.rect.x, self.rect.y

        if self.is_dying:
            if self.explosion.current_frame >= self.explosion.frame_count - 1:
                self.is_alive = False

        

    def draw(self):
        if self.is_alive:
            if self.is_dying:
                self.explosion.draw()
            else:
                self.live_anim.draw()
