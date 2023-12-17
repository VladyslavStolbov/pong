import pygame
from config import *
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x, position_y, speed_x, speed_y, paddles):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect(center=(position_x, position_y))
        self.speed_x = speed_x * random.choice((-5, 5))
        self.speed_y = speed_y * random.choice((-5, 5))
        self.paddles = paddles
        self.collision_tolerance = 10

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.collisions()

    def collisions(self):

        # Collision with top and bottom of the screen
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

        if pygame.sprite.spritecollide(self, self.paddles, False):
            collision_paddle = pygame.sprite.spritecollide(self, self.paddles, False)[0].rect
            if abs(self.rect.left - collision_paddle.right) < self.collision_tolerance and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect.right - collision_paddle.left) < self.collision_tolerance and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.top - collision_paddle.bottom) < self.collision_tolerance and self.speed_y > 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_paddle.top) < self.collision_tolerance and self.speed_y < 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1



