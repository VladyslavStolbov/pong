import pygame
from config import *


class Computer(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x=0, position_y=0):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.position_x = position_x
        self.position_y = position_y
        self.rect.topright = (position_x, position_y)

    def update(self):
        global paddle_speed
        self.rect.move_ip(0, paddle_speed)
        if self.rect.top <= 0:
            paddle_speed = abs(paddle_speed)
        if self.rect.bottom >= SCREEN_HEIGHT:
            paddle_speed = -abs(paddle_speed)
