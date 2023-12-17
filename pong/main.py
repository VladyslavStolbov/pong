import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, QUIT

from config import *
from player import Player
from computer import Computer
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()


paddle_speed = 6
ball_speed_x, ball_speed_y = 1, 1
background_image = pygame.image.load(os.path.join(assets_path, "board.png"))

# Game objects and groups
player = Player(os.path.join(assets_path, "paddle.png"), 0, SCREEN_HEIGHT // 2, paddle_speed)
computer = Computer(os.path.join(assets_path, "paddle.png"), SCREEN_WIDTH, SCREEN_HEIGHT // 2, paddle_speed)
paddles_group = pygame.sprite.Group(player, computer)
ball = Ball(os.path.join(assets_path, "ball.png"), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
            ball_speed_x, ball_speed_y, paddles_group)
ball_group = pygame.sprite.Group(ball)

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    screen.blit(background_image, (0, 0))

    keys = pygame.key.get_pressed()

    paddles_group.draw(screen)
    ball_group.draw(screen)

    player.update(keys)
    computer.update()
    ball_group.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
