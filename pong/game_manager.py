import sys
import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_SPACE, QUIT
import config
import game


class GameManger():

    def start_menu(self):
        pong_text = config.main_font.render("PONG", True, "white", "black")
        pong_rect = pong_text.get_rect(center=(config.SCREEN_WIDTH // 2, (config.SCREEN_HEIGHT // 2) - 50))
        press_key_text = config.secondary_font.render("Press space to start game!", True, "white", "black")
        press_key_rect = press_key_text.get_rect(center=(config.SCREEN_WIDTH // 2, (config.SCREEN_HEIGHT // 2) + 50))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_SPACE:
                    config.game_start_sound.play()
                    game.Game().main()
                    running = False
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
        win_text = config.main_font.render(f"{config.winner} win!", True, "white", "black")
        win_text_rect = win_text.get_rect(center=(config.SCREEN_WIDTH // 2, (config.SCREEN_HEIGHT // 2) - 20))
        press_key_text = config.secondary_font.render("Press space to restart game!", True, "white", "black")
        press_key_rect = press_key_text.get_rect(center=(config.SCREEN_WIDTH // 2, (config.SCREEN_HEIGHT // 2) + 100))

        while True:

            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_SPACE:
                    config.game_start_sound.play()
                    self.reset_game()
                    game.Game().main()
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

    def reset_game(self):
        config.player_score = 0
        config.computer_score = 0

    def display_score(self):
        player_score_number = config.main_font.render(str(config.player_score), True, "white")
        computer_score_number = config.main_font.render(str(config.computer_score), True, "white")

        player_score_rect = player_score_number.get_rect(center=((config.SCREEN_WIDTH // 2) - 150, 100))
        computer_score_rect = computer_score_number.get_rect(center=((config.SCREEN_WIDTH // 2) + 150, 100))

        config.screen.blit(player_score_number, player_score_rect)
        config.screen.blit(computer_score_number, computer_score_rect)

    def check_for_win(self):
        if config.player_score == 10:
            config.winner = "Player"
            self.end_menu()
        elif config.computer_score == 10:
            config.winner = "Computer"
            self.end_menu()

    def check_for_collision(self, ball):
        if ball.rect.right >= config.SCREEN_WIDTH:
            config.score_sound.play()
            config.player_score += config.score_increment
            ball.reset_ball()
        if ball.rect.left <= 0:
            config.score_sound.play()
            config.computer_score += config.score_increment
            ball.reset_ball()
