import sys
import os
import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, QUIT
from config import SCREEN_WIDTH, SCREEN_HEIGHT, assets_path, paddle_speed, ball_speed_x, ball_speed_y
from player import Player
from computer import Computer
from ball import Ball
from score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load(os.path.join(assets_path, "board.png"))

        # Game objects and groups
        self.player = Player(os.path.join(assets_path, "paddle.png"), 0, SCREEN_HEIGHT // 2, paddle_speed)
        self.computer = Computer(os.path.join(assets_path, "paddle.png"), SCREEN_WIDTH, SCREEN_HEIGHT // 2, paddle_speed)
        self.paddles_group = pygame.sprite.Group(self.player, self.computer)
        self.ball = Ball(os.path.join(assets_path, "ball.png"), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                         ball_speed_x, ball_speed_y, self.paddles_group)
        self.ball_group = pygame.sprite.Group(self.ball)
        self.score = Score()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    def update(self):
        self.screen.blit(self.background_image, (0, 0))
        self.paddles_group.update()
        self.ball_group.update()

    def draw(self):
        self.score.display_score(self.screen)
        self.paddles_group.draw(self.screen)
        self.ball_group.draw(self.screen)

    def run(self):
        running = True
        while running:
            self.event_handler()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
