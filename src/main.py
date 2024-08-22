import pygame
from cell import Cell
from board import Board
from config import *
from ui.manager import Manager
from create_ui import create_menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.board = Board()
        self.player = 0

        self.manager = Manager()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.click(event.pos)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.board.reset_cells()

            self.draw_game()
            CLOCK.tick(FPS)

    def menu_loop(self):
        create_menu(self.manager)
        self.manager.get_widget("play").set_callback(self.game_loop)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                self.manager.handle_event(event)


            self.manager.draw(self.screen)
            pygame.display.update()
            CLOCK.tick(FPS)

    def draw_game(self):
        self.screen.fill(Colors.black)
        self.board.draw(self.screen)
        pygame.display.update()

    def click(self, pos):
        row = pos[1] // TILE_SIZE
        col = pos[0] // TILE_SIZE

        cell = self.board.get_cell(row, col)

        if cell.get_state() is None:
            cell.set_state(self.player)

            if self.board.check_win(row, col, self.player):
                self.game_over()

            self.player = not self.player

    def game_over(self):
        self.player = 0
        # self.board.reset_cells()
        print("game_over")


if __name__ == '__main__':
    game = Game()
    game.menu_loop()
