import pygame
from config import TILE_SIZE


class Cell:
	def __init__(self, x, y, state=None):
		self.__x = x 
		self.__y = y 
		self.__state = state

	def draw(self, surface:pygame.surface.Surface):
		if self.__state == 1:
			pygame.draw.circle(surface, "red", (self.__x + TILE_SIZE // 2, self.__y + TILE_SIZE // 2), TILE_SIZE // 2.5, 10)
		if self.__state == 0:
			pygame.draw.line(surface, "blue", 
				(self.__x + TILE_SIZE // 10, self.__y + TILE_SIZE // 10), 
				(self.__x + TILE_SIZE - TILE_SIZE // 10, self.__y + TILE_SIZE - TILE_SIZE // 10), 10)

			pygame.draw.line(surface, "blue", 
				(self.__x + TILE_SIZE // 10, self.__y + TILE_SIZE - TILE_SIZE // 10), 
				(self.__x + TILE_SIZE - TILE_SIZE // 10, self.__y + TILE_SIZE // 10), 10)

	def set_state(self, state:int|None) -> None:
		self.__state = state

	def get_pos(self) -> list[int,int]:
		return [self.__x, self.__y]

	def get_state(self) -> int|None:
		return self.__state