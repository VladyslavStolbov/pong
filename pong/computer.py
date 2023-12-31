import pygame
import config

class Computer(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x, position_y, speed):
        """Initialize the Computer paddle."""
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(midright=(position_x, position_y))
        self.speed = speed

    def update(self):
        """Update the position of the computer paddle."""
        # Move the computer paddle vertically
        self.rect.y += self.speed

        # Limiting movements only within the screen borders
        if self.rect.top <= 0:
            self.speed = abs(self.speed)
        if self.rect.bottom >= config.SCREEN_HEIGHT:
            self.speed = -abs(self.speed)
