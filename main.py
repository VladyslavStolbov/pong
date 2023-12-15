import pygame
from pygame.locals import *

from paddle import Paddle

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

player_sprite = Paddle("assets/player.png", 10, SCREEN_HEIGHT // 2)
computer_sprite = Paddle("assets/computer.png", SCREEN_WIDTH - 10, SCREEN_HEIGHT // 2)
all_sprites = pygame.sprite.Group()
all_sprites.add(player_sprite, computer_sprite)

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    screen.fill("white")

    keys = pygame.key.get_pressed()
    player_sprite.update(keys)
    all_sprites.update(keys)
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
