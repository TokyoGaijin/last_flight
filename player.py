import pygame
import os
from animator import Animator
from enum import Enum
from bullet import Bullet

class PlayerState(Enum):
    ALIVE = 0
    DYING = 1
    DEAD = 2


class Player:
    def __init__(self, surface, startX, startY):
        self.surface = surface
        self.speed = 5
        self.current_state = PlayerState.ALIVE
        
        self.live_anim = Animator(
            self.surface,
            startX,
            startY,
            2,
            [pygame.image.load(os.path.join("sprite_assets", f"player_plane_{i}.png")) for i in range(0, 2)]
        )
        self.current_anim = self.live_anim
        self.rect = pygame.Rect(startX, startY, 50, 50)
        self.explosion_list = []
        self.bullet_list = []
        self.cool_timer = 0
        self.FIRE_BUFFER = 60 / 2

    def fire(self):
        self.bullet_list.append(Bullet(self.surface, self.rect.x + 10, self.rect.y + 10, "up", color = (255, 255, 0)))
        self.bullet_list.append(Bullet(self.surface, self.rect.right - 15, self.rect.y + 10, "up", color = (255, 255, 0)))

    def update(self):
        keys = pygame.key.get_pressed()
        if self.current_state == PlayerState.ALIVE:
            if keys[pygame.K_LEFT] and self.rect.left >= 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right <= 640:
                self.rect.x += self.speed
            if keys[pygame.K_UP] and self.rect.top >= 0:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN] and self.rect.bottom <= 480:
                self.rect.y += self.speed

            if keys[pygame.K_SPACE]:
                if len(self.bullet_list) < 6 and self.cool_timer % self.FIRE_BUFFER == 0:
                    self.fire()
                self.cool_timer += 1
            else:
                self.cool_timer = 0

            for b in self.bullet_list:
                b.update()
                if b.rect.bottom <= 0:
                    self.bullet_list.remove(b)

                

            self.live_anim.animate()
            self.live_anim.play_x, self.live_anim.play_y = self.rect.x, self.rect.y

            if keys[pygame.K_k]:
                self.current_state = PlayerState.DYING


            
        elif self.current_state == PlayerState.DYING:
            if len(self.explosion_list) < 1: 
                self.explosion_list.append(Animator(
                        self.surface,
                        self.rect.x,
                        self.rect.y,
                        11,
                        [pygame.image.load(os.path.join("sprite_assets", f"player_death_{i}.png")) for i in range(0, 11)]
                         ))

            for explosion in self.explosion_list:
                explosion.animate()
                if explosion.current_frame >= explosion.frame_count -1:
                    self.explosion_list.remove(explosion)
                    self.current_state = PlayerState.DEAD


    def draw(self):
        if self.current_state == PlayerState.ALIVE:
            # pygame.draw.rect(self.surface, (255, 0, 0), self.rect) # Testing
            for b in self.bullet_list:
                b.draw()
            self.live_anim.draw()

        if self.current_state == PlayerState.DYING:
            for explosion in self.explosion_list:
                explosion.draw()
            