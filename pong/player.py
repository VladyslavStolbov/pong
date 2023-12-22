import pygame
from pygame.locals import *
import config


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x, position_y, speed):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(midleft=(position_x, position_y))
        self.speed = speed

    def handle_input(self):
        """Handle keyboard input for player movement"""
        keys = pygame.key.get_pressed()

        # Move up if any of the specified keys is pressed
        if any(keys[key] for key in (K_UP, K_w, K_k)):
            self.rect.move_ip(0, -self.speed)

        # Move down if any of the specified keys is pressed
        if any(keys[key] for key in (K_DOWN, K_s, K_j)):
            self.rect.move_ip(0, self.speed)

    def constrain_to_screen(self):
        """Constrain player movement within the screen borders"""
        # Ensure the player does not go above the screen
        if self.rect.top < 0:
            self.rect.top = 0

        # Ensure the player does not go below the screen
        if self.rect.bottom > config.SCREEN_HEIGHT:
            self.rect.bottom = config.SCREEN_HEIGHT

    def update(self):
        """Update player state"""
        self.handle_input()
        self.constrain_to_screen()
