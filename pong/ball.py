import pygame
import random
import os
import config


class Ball(pygame.sprite.Sprite):
    def __init__(self, image_path, position_x, position_y, speed_x, speed_y, paddles):
        super().__init__()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect(center=(position_x, position_y))
        self.speed_x = speed_x * random.choice((-5, 5))
        self.speed_y = speed_y * random.choice((-5, 5))
        self.paddles = paddles
        self.collision_tolerance = 10
        self.collision_sound = pygame.mixer.Sound(os.path.join(config.sounds_path, "collision.wav"))
        self.collision_sound.set_volume(0.3)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.collisions()

    def collisions(self):
        # Collision with top and bottom of the screen
        if self.rect.top <= 0 or self.rect.bottom >= config.SCREEN_HEIGHT:  # noqa: F405
            pygame.mixer.Sound.play(self.collision_sound)
            self.speed_y *= -1

        # Collision with paddles on both sides
        if pygame.sprite.spritecollide(self, self.paddles, False):
            self.collision_sound.play()
            # Assign list of collision paddles
            collision_paddles = pygame.sprite.spritecollide(self, self.paddles, False)
            # Looping through list and check coordinates
            for paddle in collision_paddles:
                # A collision_tolerance for less restrictive statements.
                # A self.speed checking for moving sprites. Should be movement in different directions.
                if abs(self.rect.left - paddle.rect.right) < self.collision_tolerance and self.speed_x < 0:
                    self.rect.left = paddle.rect.right  # Assign coordinates back to intersect
                    self.speed_x *= -1  # Invert moving
                if abs(self.rect.right - paddle.rect.left) < self.collision_tolerance and self.speed_x > 0:
                    self.rect.right = paddle.rect.left
                    self.speed_x *= -1
                if abs(self.rect.top - paddle.rect.bottom) < self.collision_tolerance and self.speed_y > 0:
                    self.rect.top = paddle.rect.bottom
                    self.speed_y *= -1
                if abs(self.rect.bottom - paddle.rect.top) < self.collision_tolerance and self.speed_y < 0:
                    self.rect.bottom = paddle.rect.top
                    self.speed_y *= -1

    def reset_ball(self):
        self.speed_y *= random.choice((-1, 1))
        self.speed_x *= random.choice((-1, 1))
        self.rect.center = (config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2)


