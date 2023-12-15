import pygame
from pygame.locals import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x=0, position_y=0):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.position_x = position_x
        self.position_y = position_y
        self.rect.center = (position_x, position_y)
        self.image.set_colorkey("black")

    def update(self, keys):
        if any(keys[key] for key in (K_UP, K_w, K_k)):
            self.rect.move_ip(0, -5)
        if any(keys[key] for key in (K_DOWN, K_s, K_j)):
            self.rect.move_ip(0, 5)