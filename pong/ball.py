import random
from config import *

import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x, position_y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.position_x = position_x
        self.position_y = position_y
        self.rect.center = (position_x, position_y)
        self.ball_direction = self.choose_direction()
        self.random_coordinate = random.randint(-2,  2)

    def update(self):
        if self.ball_direction:
            self.rect.move_ip(speed, self.random_coordinate)
        if not self.ball_direction:
            self.rect.move_ip(-speed, self.random_coordinate)

    def choose_direction(self):
        return random.choice((True, False))