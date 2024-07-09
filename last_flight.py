import pygame
from enum import Enum
from player import Player

# Testing Imports
import random
from new_test_enemy import Enemy

# Declare game states here

SCREEN_X = 640
SCREEN_Y = 480
SCREEN = (SCREEN_X, SCREEN_Y)
SURFACE = pygame.display.set_mode(SCREEN, pygame.SCALED)
FPS = 60
CLOCK = pygame.time.Clock()
CF_BLUE = (100, 149, 237)
BLACK = (0, 0, 0)
BG = CF_BLUE

# Instantiate objects here
player = Player(SURFACE, 320, 240)
enemy_list = []

def add_enemy():
    enemy_list.append(Enemy(SURFACE, random.randrange(0, SCREEN_X - 62), -62))

def draw():
    for e in enemy_list:
        e.draw()
    player.draw()



def update_elements():
    player.update()

    if len(enemy_list) < 1:
        add_enemy()

    for e in enemy_list:
        e.update()
        for b in player.bullet_list:
            if b.rect.colliderect(e.rect):
                e.hp = 0
                player.bullet_list.remove(b)
        if not e.is_alive or e.rect.top >= SCREEN_Y:
            enemy_list.remove(e)



        


def update():
    CLOCK.tick(FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    draw()
    update_elements()
    pygame.display.update()
    SURFACE.fill(BG)


def run():
    while True:
        update()

if __name__ == '__main__':
    run()