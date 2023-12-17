import pygame
from config import *
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x, position_y, speed):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(midleft=(position_x, position_y))
        self.speed = speed

    def update(self, keys):
        # Movements Up and Down by Arrow Up, W, K and Arrow Down, S, J
        if any(keys[key] for key in (K_UP, K_w, K_k)):
            self.rect.move_ip(0, -self.speed)
        if any(keys[key] for key in (K_DOWN, K_s, K_j)):
            self.rect.move_ip(0, self.speed)
        # Limiting movements only in screen borders
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
