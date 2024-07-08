import pygame
from enum import Enum

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


def draw():
    pass


def update_elements():
    pass


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