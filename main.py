import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill("white")

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
