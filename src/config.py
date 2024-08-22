import pygame


DEBUG = True

WIDTH = 700
HEIGHT = 700

TILE_SIZE = 70
NUM_CELLS_FOR_WIN = 3

GAME_TITLE = 'Tic Tac Toe'

CLOCK = pygame.time.Clock()
FPS = 120

class Colors:
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    black = (0,0,0)
    white = (255,255,255)


BUTTON_WIDTH = WIDTH // 3
BUTTON_HEIGHT = HEIGHT // 7