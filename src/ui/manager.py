import pygame
from .text import Text
from .button import Button
from .image import Image


class Manager:
	def __init__(self):
		self.__widgets = []

	def draw(self, surface:pygame.surface.Surface):
		for widget in self.__widgets:
			widget.draw(surface)

	def handle_event(self, event:pygame.event):
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			for widget in self.__widgets:
				if isinstance(widget, Button) and widget.is_collide(event.pos):
					widget.activate()
					break
		if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			for widget in self.__widgets:
				if isinstance(widget, Button) and widget.is_active():
					widget.deactivate()

					if widget.is_collide(event.pos):
						widget.press()

	def add(self, widget:Text|Button|Image) -> None:
		self.__widgets.append(widget)

	def get_widget(self, name:str) -> Text|Button|Image:
		for widget in self.__widgets:
			if widget.get_name() == name:
				return widget