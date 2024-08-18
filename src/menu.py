import pygame
from config import WIDTH, HEIGHT
from ui import *


class Menu:
	def __init__(self):
		self.__widgets = {"texts": [], "buttons": [], "images": []}

	def draw(self, surface:pygame.surface.Surface) -> None:
		for image in self.__widgets["images"]:
			image.draw(surface)

		for text in self.__widgets["texts"]:
			text.draw(surface)

		for button in self.__widgets["buttons"]:
			button.draw(surface)

	def create_menu(self) -> None:
		self.__widgets["images"].append(Image(0, 0, "../res/images/background.png").scale(WIDTH, HEIGHT))
		self.__widgets["texts"].append(Text(WIDTH // 2, HEIGHT // 8, "Tic Tac Toe", font_size=(WIDTH + HEIGHT) // 20, antialias=True))
