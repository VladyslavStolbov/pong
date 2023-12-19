import pygame
import config


class GameManager:
    def __init__(self, font):
        self.font = font
        self.winner = None

    def display_score(self):
        player_score_number = self.font.render(str(config.player_score), True, "white")
        computer_score_number = self.font.render(str(config.computer_score), True, "white")

        player_score_rect = player_score_number.get_rect(center=((config.SCREEN_WIDTH // 2) - 150, 100))
        computer_score_rect = computer_score_number.get_rect(center=((config.SCREEN_WIDTH // 2) + 150, 100))

        config.screen.blit(player_score_number, player_score_rect)
        config.screen.blit(computer_score_number, computer_score_rect)

    def end_screen(self, is_player):
        if is_player:
            self.winner = "Player"
        else:
            self.winner = "Computer"
        win_text = self.font.render(f"{self.winner} win!", True, "white")
        win_text_rect = win_text.get_rect(center=(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
        config.screen.blit(win_text, win_text_rect)

    def check_for_collision(self, ball):
        if ball.rect.right >= config.SCREEN_WIDTH:
            config.player_score += 10
            ball.reset_ball()
        if ball.rect.left <= 0:
            config.computer_score += 10
            ball.reset_ball()

    def check_for_win(self):
        if config.player_score == 10:
            self.end_screen(is_player=True)
        elif config.computer_score == 10:
            self.end_screen(is_player=False)
