import pygame
from pygame.locals import *
import os

from config import *
from player import Player
from computer import Computer
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

background_image = pygame.image.load(os.path.join(assets_path, "board.png"))

player_sprite = Player(os.path.join(assets_path, "paddle.png"), 0, SCREEN_HEIGHT // 2)
computer_sprite = Computer(os.path.join(assets_path, "paddle.png"), SCREEN_WIDTH, SCREEN_HEIGHT // 2)
ball_sprite = Ball(os.path.join(assets_path, "ball.png"), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

all_sprites = pygame.sprite.Group()
all_sprites.add(player_sprite, computer_sprite, ball_sprite)

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    screen.blit(background_image, (0, 0))

    keys = pygame.key.get_pressed()
    player_sprite.update(keys)
    computer_sprite.update()
    ball_sprite.update()
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
