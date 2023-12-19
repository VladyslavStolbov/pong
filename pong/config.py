import os
import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

paddle_speed = 6
ball_speed_x, ball_speed_y = 1, 1
player_score = 0
computer_score = 0

assets_path = os.path.join(os.path.dirname(__file__), "../assets")
sounds_path = os.path.join(os.path.dirname(__file__), "../sounds")
fonts_path = os.path.join(os.path.dirname(__file__), "../fonts")

