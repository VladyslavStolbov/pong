import pygame
from pygame.locals import *
import os

from config import *
from player import Player
from computer import Computer
from ball import Ball

def check_collision():
    if ball.rect.right >= SCREEN_WIDTH or ball.rect.left <0:
        ball.change_direction()
    if ball.rect.bottom >= SCREEN_HEIGHT or ball.rect.top <= 0:
        ball.change_direction()
    if ball.rect.collideobjects([player, computer]):
        ball.change_direction()

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

background_image = pygame.image.load(os.path.join(assets_path, "board.png"))

player = Player(os.path.join(assets_path, "paddle.png"), 0, SCREEN_HEIGHT // 2)
computer = Computer(os.path.join(assets_path, "paddle.png"), SCREEN_WIDTH, SCREEN_HEIGHT // 2)
ball = Ball(os.path.join(assets_path, "ball.png"), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

all_sprites = pygame.sprite.Group()
all_sprites.add(player, computer, ball)

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    screen.blit(background_image, (0, 0))

    check_collision()

    keys = pygame.key.get_pressed()

    player.update(keys)
    computer.update()
    ball.update()
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
