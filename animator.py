"""
Custom animator module

TODO: Add more documentation here
"""

import pygame


class Animator:
    def __init__(self, surface, play_x, play_y, frame_count, strip):
        self.surface = surface
        self.play_x = play_x
        self.play_y = play_y
        self.strip = strip
        self.frame_count = frame_count
        self.FRAME_RATE = 60 * .05
        self.current_frame = 0
        self.anim_timer = 0
        self.current_image = self.strip[0]

    def animate(self):
        self.anim_timer += 1
        if self.anim_timer % self.FRAME_RATE == 0:
            self.current_frame += 1
            if self.current_frame >= len(self.strip):
                self.current_frame = 0

        self.current_image = self.strip[self.current_frame]

    def draw(self):
        self.surface.blit(self.current_image, (self.play_x, self.play_y))