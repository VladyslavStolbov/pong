import pygame
from config import *
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x, position_y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.position_x = position_x
        self.position_y = position_y
        self.rect.center = (position_x, position_y)
        self.ball_direction = random.choice((True, False))
        self.random_coordinate = random.randint(-2,  2)

    def update(self):
        if self.ball_direction:
            self.rect.move_ip(paddle_speed, self.random_coordinate)
        if not self.ball_direction:
            self.rect.move_ip(-paddle_speed, self.random_coordinate)

    def change_direction(self):
        self.ball_direction = not self.ball_direction