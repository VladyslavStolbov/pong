import pygame
from pygame.locals import *

from config import *
from player import Player
from computer import Computer

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

background_image = pygame.image.load("../assets/board.png")

player_sprite = Player("../assets/paddle.png", 0, SCREEN_HEIGHT // 2)
computer_sprite = Computer("../assets/paddle.png", SCREEN_WIDTH, SCREEN_HEIGHT // 2)
all_sprites = pygame.sprite.Group()
all_sprites.add(player_sprite, computer_sprite)

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
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
