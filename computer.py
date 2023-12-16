import pygame
from config import *


class Computer(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x=0, position_y=0):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.position_x = position_x
        self.position_y = position_y
        self.rect.topright = (position_x, position_y)
        self.speed = speed

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.topright[1] <= 0:
            self.speed = abs(self.speed)
        if self.rect.bottomright[1] >= SCREEN_HEIGHT:
            self.speed = -abs(self.speed)