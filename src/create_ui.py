import pygame
from ui import *
from config import WIDTH, HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT


def create_menu(manager) -> list:
    manager.add(Image(
        x=0, 
        y=0, 
        path="../res/images/background.png",
        name="background"
        ).scale(WIDTH, HEIGHT))

    manager.add(Text(
        x=WIDTH // 2, 
        y=HEIGHT // 10, 
        text="Tic Tac Toe",
        name="main_text",
        font_size=55,
        antialias=True))

    manager.add(Button(
        x=WIDTH // 8, 
        y=HEIGHT // 1.5, 
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        font_size=30,
        text="Settings",
        name="settings"))
        
    manager.add(Button(
        x=WIDTH // 1.8, 
        y=HEIGHT // 1.5, 
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        font_size=30,
        text="Play",
        name="play"))