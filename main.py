import pygame, sys
from level import Level
from settings import *
from tiles import Tile


# PyGame Setup - Inicializa todos os módulos pygame importados
pygame.init()

# configuração do tamanho do display 
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame:
            pygame.quit()
            sys.exit

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)