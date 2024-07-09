import pygame
import os
from animator import Animator
from generic_explosion import Explosion
from enum import Enum

class EnemyState(Enum):
    ALIVE = 0
    DYING = 1
    DEAD = 2

class Enemy:
    def __init__(self, surface, startX, startY):
        # Enemy will be of a single type. Further enemies must have
        # Appropriate args
        self.surface = surface
        self.live_anim = Animator(
            self.surface,
            startX,
            startY,
            2,
            [pygame.image.load(os.path.join("sprite_assets", f"enemy_1_{i}.png")) for i in range(0, 2)]
        )
        self.explosion_list = []
        self.rect = pygame.Rect(startX, startY, 64, 64)
        self.speed = 3
        self.current_state = EnemyState.ALIVE
        self.hp = 5

    def update(self):
        if self.current_state == EnemyState.ALIVE:
            self.live_anim.animate()
            self.rect.y += self.speed
            if self.hp <= 0:
                self.current_state == EnemyState.DYING
            self.live_anim.play_x, self.live_anim.play_y = self.rect.x, self.rect.y

        if self.current_state == EnemyState.DYING:
            self.explosion_list.append(Explosion(self.surface, self.rect.x, self.rect.y)) if len(self.explosion_list) < 1 else None
            for e in self.explosion_list:
                e.update()
                if e.kaboom.current_frame >= 7:
                    self.explosion_list.remove(e)
                    self.current_state == EnemyState.DEAD

        if self.current_state == EnemyState.DEAD:
            pass

    def draw(self):
        if self.current_state == EnemyState.ALIVE:
            self.live_anim.draw()
        