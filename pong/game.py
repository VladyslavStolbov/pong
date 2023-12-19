import sys
import os
import time

import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, QUIT
import config
from player import Player
from computer import Computer
from ball import Ball
from game_manager import GameManager


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load(os.path.join(config.assets_path, "board.png"))
        self.font = pygame.font.Font(os.path.join(config.fonts_path, "m5x7.ttf"), 256)

        # Game objects and groups
        self.player = Player(os.path.join(config.assets_path, "paddle.png"), 0, config.SCREEN_HEIGHT // 2,
                             config.paddle_speed)
        self.computer = Computer(os.path.join(config.assets_path, "paddle.png"), config.SCREEN_WIDTH,
                                 config.SCREEN_HEIGHT // 2, config.paddle_speed)
        self.paddles_group = pygame.sprite.Group(self.player, self.computer)
        self.ball = Ball(os.path.join(config.assets_path, "ball.png"), config.SCREEN_WIDTH // 2,
                         config.SCREEN_HEIGHT // 2, config.ball_speed_x, config.ball_speed_y, self.paddles_group)
        self.ball_group = pygame.sprite.Group(self.ball)
        self.game_manager = GameManager(self.font)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    def update(self):
        config.screen.blit(self.background_image, (0, 0))
        self.paddles_group.update()
        self.ball_group.update()
        self.game_manager.check_for_collision(self.ball)
        self.game_manager.check_for_win()

    def draw(self):
        self.game_manager.display_score()
        self.paddles_group.draw(config.screen)
        self.ball_group.draw(config.screen)

    def run(self):
        running = True
        while running:
            self.event_handler()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
