import pygame
from menu import Menu
from cell import Cell
from board import Board
from config import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)

        self.board = Board()
        self.menu = Menu()
        self.player = 0

    def game_loop(self):
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.click(event.pos)

            CLOCK.tick(FPS)

    def menu_loop(self):
        self.menu.create_menu()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pass

            self.menu.draw(SCREEN)
            pygame.display.update()
            CLOCK.tick(FPS)

    def draw(self):
        SCREEN.fill(Colors.black)
        self.board.draw(SCREEN)
        pygame.display.update()

    def click(self, pos):
        row = pos[1] // TILE_SIZE
        col = pos[0] // TILE_SIZE

        cell = self.board.get_cell(row, col)

        if cell.get_state() is None:
            cell.set_state(self.player)
            self.player = not self.player

            self.draw()

            if self.board.check_win(row, col):
                self.game_over()

    def game_over(self):
        self.player = 0
        self.board.reset_cells()
        self.draw()


if __name__ == '__main__':
    game = Game()
    game.menu_loop()
