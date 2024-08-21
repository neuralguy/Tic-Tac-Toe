import pygame
from pygame_gui import UIManager
from pygame_gui import elements
from config import WIDTH, HEIGHT


class Menu:
	def __init__(self):
		self.__widgets = {"texts": [], "buttons": [], "images": []}
		self.__game = False

		self.

	def update(self):
		self.draw()

	def draw(self, surface:pygame.surface.Surface) -> None:
		for image in self.__widgets["images"]:
			image.draw(surface)

		for text in self.__widgets["texts"]:
			text.draw(surface)

		for button in self.__widgets["buttons"]:
			button.draw(surface)

	def click(self, pos):
		for button in self.__widgets["buttons"]:
			if button.is_collide(pos):
				button.press()

	def create_menu(self) -> None:
		self.__widgets["images"].append(Image(0, 0, "../res/images/background.png").scale(WIDTH, HEIGHT))
		self.__widgets["images"].append()
		self.__widgets["texts"].append(Text(WIDTH // 2, HEIGHT // 8, "Tic Tac Toe", font_size=(WIDTH + HEIGHT) // 20, antialias=True))
		self.__widgets["buttons"].append(Button(WIDTH // 1.5, HEIGHT // 1.5, "Play", self.start_game, font_size=(WIDTH + HEIGHT) // 30))

	def start_game(self) -> None:
		self.__game = True

	def is_game_started(self) -> bool:
		return self.__game
