import sys
import os

import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_SPACE, QUIT
import config
from player import Player
from computer import Computer
from ball import Ball


class Game:
    def __init__(self):
        pygame.init()

        self.score_sound = pygame.mixer.Sound(os.path.join(config.sounds_path, "score.wav"))
        self.main_font = pygame.font.Font(os.path.join(config.fonts_path, "m5x7.ttf"), 256)
        self.secondary_font = pygame.font.Font(os.path.join(config.fonts_path, "m5x7.ttf"), 64)
        self.winner = None
        self.background_image = pygame.image.load(os.path.join(config.assets_path, "board.png"))

        # Game objects and groups
        self.player = Player(os.path.join(config.assets_path, "paddle.png"), 0, config.SCREEN_HEIGHT // 2,
                             config.paddle_speed)
        self.computer = Computer(os.path.join(config.assets_path, "paddle.png"), config.SCREEN_WIDTH,
                                 config.SCREEN_HEIGHT // 2, config.paddle_speed)
        self.paddles_group = pygame.sprite.Group(self.player, self.computer)
        self.ball = Ball(os.path.join(config.assets_path, "ball.png"), config.SCREEN_WIDTH // 2,
                         config.SCREEN_HEIGHT // 2, config.ball_speed_x, config.ball_speed_y, self.paddles_group)
        self.ball_group = pygame.sprite.Group(self.ball)

    def display_score(self):
        player_score_number = self.main_font.render(str(config.player_score), True, "white")
        computer_score_number = self.main_font.render(str(config.computer_score), True, "white")

        player_score_rect = player_score_number.get_rect(center=((config.SCREEN_WIDTH // 2) - 150, 100))
        computer_score_rect = computer_score_number.get_rect(center=((config.SCREEN_WIDTH // 2) + 150, 100))

        config.screen.blit(player_score_number, player_score_rect)
        config.screen.blit(computer_score_number, computer_score_rect)

    def start_menu(self):
        pong_text = self.main_font.render("PONG", True, "white", "black")
        pong_rect = pong_text.get_rect(center=(config.SCREEN_WIDTH // 2, (config.SCREEN_HEIGHT // 2) - 50))
        press_key_text = self.secondary_font.render("Press space to start game!", True, "white",
                                                    "black")
        press_key_rect = press_key_text.get_rect(center=(config.SCREEN_WIDTH // 2, (config.SCREEN_HEIGHT // 2) + 50))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_SPACE:
                    running = False
                    self.main()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            config.screen.blit(pong_text, pong_rect)
            config.screen.blit(press_key_text, press_key_rect)

            pygame.display.flip()
            config.clock.tick(config.FPS)

    def end_menu(self):

        win_text = self.main_font.render(f"{self.winner} win!", True, "white", "black")
        win_text_rect = win_text.get_rect(center=(config.SCREEN_WIDTH // 2, (config.SCREEN_HEIGHT // 2) - 20))
        press_key_text = self.secondary_font.render("Press space to restart game!", True, "white",
                                                    "black")
        press_key_rect = press_key_text.get_rect(center=(config.SCREEN_WIDTH // 2, (config.SCREEN_HEIGHT // 2) + 100))

        while True:

            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_SPACE:
                    self.reset_game()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            config.screen.blit(win_text, win_text_rect)
            config.screen.blit(press_key_text, press_key_rect)

            self.display_score()

            pygame.display.flip()
            config.clock.tick(config.FPS)

    def check_for_collision(self, ball):
        if ball.rect.right >= config.SCREEN_WIDTH:
            self.score_sound.play()
            config.player_score += 1
            ball.reset_ball()
        if ball.rect.left <= 0:
            self.score_sound.play()
            config.computer_score += 1
            ball.reset_ball()

    def check_for_win(self):
        if config.player_score == 10:
            self.winner = "Player"
            self.end_menu()
        elif config.computer_score == 10:
            self.winner = "Computer"
            self.end_menu()

    def reset_game(self):
        config.player_score = 0
        config.computer_score = 0
        self.main()

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
        self.check_for_collision(self.ball)
        self.check_for_win()

    def draw(self):
        self.display_score()
        self.paddles_group.draw(config.screen)
        self.ball_group.draw(config.screen)

    def main(self):
        running = True
        while running:
            self.event_handler()
            self.update()
            self.draw()
            pygame.display.flip()
            config.clock.tick(config.FPS)

    def run(self):
        self.start_menu()