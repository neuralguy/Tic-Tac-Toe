import pygame
from cell import Cell
from config import WIDTH, HEIGHT, TILE_SIZE


class Board:
	def __init__(self):
		self.__cells = self.create_cells()

	def draw(self, surface:pygame.surface.Surface) -> None:
		for x in range(0, WIDTH, TILE_SIZE):
			for y in range(0, HEIGHT, TILE_SIZE):
				pygame.draw.rect(surface, "white", (x, y, TILE_SIZE, TILE_SIZE), 1)

		for cell in self.__cells:
			cell.draw(surface)

	def create_cells(self) -> list[Cell]:
		cells = []
		for x in range(0, WIDTH, TILE_SIZE):
			for y in range(0, HEIGHT, TILE_SIZE):
				cells.append(Cell(x, y))
		return cells

	def get_cell(self, row:int, col:int) -> Cell:
		for cell in self.__cells:
			if [i // TILE_SIZE for i in cell.get_pos()] == [col, row]:
				return cell



