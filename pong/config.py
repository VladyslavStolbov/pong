import os
import pygame

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Pygame display initialization
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Game settings
paddle_speed = 6
ball_speed_x, ball_speed_y = 1, 1
player_score = 0
computer_score = 0
score_increment = 1
winner = None

# File paths
assets_path = os.path.join(os.path.dirname(__file__), "../assets")
sounds_path = os.path.join(os.path.dirname(__file__), "../sounds")
fonts_path = os.path.join(os.path.dirname(__file__), "../fonts")

# Load game assets
background_image = pygame.image.load(os.path.join(assets_path, "board.png"))
main_font = pygame.font.Font(os.path.join(fonts_path, "m5x7.ttf"), 256)
secondary_font = pygame.font.Font(os.path.join(fonts_path, "m5x7.ttf"), 64)

# Load game sounds
score_sound = pygame.mixer.Sound(os.path.join(sounds_path, "score.wav"))
