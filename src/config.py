import pygame


WIDTH = 700
HEIGHT = 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

TILE_SIZE = 140

GAME_TITLE = 'Tic Tac Toe'

CLOCK = pygame.time.Clock()
FPS = 60


class Colors:
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    black = (0,0,0)
    white = (255,255,255)
