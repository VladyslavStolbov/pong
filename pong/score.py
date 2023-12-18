import pygame
from config import *


class Score:

    def __init__(self):
        self.font = pygame.font.Font(os.path.join(fonts_path, "m5x7.ttf"), 256)

    def change_score(self, is_player):
        global player_score, computer_score
        if is_player:
            player_score += 1
        else:
            computer_score += 1

    def display_score(self, screen):
        player_score_number = self.font.render(str(player_score,), True, "white")
        computer_score_number = self.font.render(str(computer_score), True, "white")

        player_score_rect = player_score_number.get_rect(center=((SCREEN_WIDTH // 2) - 150, 100))
        computer_score_rect = computer_score_number.get_rect(center=((SCREEN_WIDTH // 2) + 150, 100))

        screen.blit(player_score_number, player_score_rect)
        screen.blit(computer_score_number, computer_score_rect)


