import pygame
from pygame import mixer

mixer.init()

class SoundBox:
    def __init__(self, channels):
        self.channels = [mixer.Channel(i) for i in range(channels)]
        self.sounds = {}

    def load_sound(self, path, channel):
        self.sounds[channel] = mixer.Sound(path)

    def play(self, channel):
        self.channels[channel].stop()
        self.channels[channel].play(self.sounds[channel])