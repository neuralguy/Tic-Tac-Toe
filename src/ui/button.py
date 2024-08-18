import pygame
from .text import Text


class Button(Text):
    """
    Класс для создания интерактивной кнопки.

    Наследует от класса Text и добавляет функциональность для обработки кликов.

    Атрибуты:
        __callback (callable): Функция, вызываемая при нажатии на кнопку.
        __width (int): Ширина кнопки.
        __height (int): Высота кнопки.
        __h_padding (int): Горизонтальный отступ текста от краев кнопки.
        __v_padding (int): Вертикальный отступ текста от краев кнопки.
        __background_color (tuple[int,int,int]|list[int,int,int]|str): Цвет фона кнопки.
        __background_alpha (int): Прозрачность фона кнопки (от 0 до 255).
        __background_surface (pygame.surface.Surface): Поверхность фона кнопки.
    """
    def __init__(self, 
        x: int, 
        y: int, 
        text: str, 
        callback: callable, 
        width: int=-1, 
        height: int=-1,
        h_padding=30,
        v_padding=5,
        text_color: tuple[int,int,int]|list[int,int,int]|str="white", 
        text_alpha: int=255,
        font_size: int=16, 
        font_path: str="freesansbold.ttf", 
        antialias: bool=True,
        background_color: tuple[int,int,int]|list[int,int,int]|str="black", 
        background_alpha: int=0
        ) -> None:
        """
        Инициализация объекта Button.

        Args:
            x (int): Координата x кнопки.
            y (int): Координата y кнопки.
            text (str): Текст на кнопке.
            callback (callable): Функция, вызываемая при нажатии на кнопку.
            width (int, optional): Ширина кнопки. По умолчанию -1 (автоматически подбирается по ширине текста).
            height (int, optional): Высота кнопки. По умолчанию -1 (автоматически подбирается по высоте текста).
            h_padding (int, optional): Горизонтальный отступ текста от краев кнопки. По умолчанию 30.
            v_padding (int, optional): Вертикальный отступ текста от краев кнопки. По умолчанию 5.
            text_color (tuple[int,int,int]|list[int,int,int]|str, optional): Цвет текста. По умолчанию "white".
            text_alpha (int, optional): Прозрачность текста (от 0 до 255). По умолчанию 255.
            font_size (int, optional): Размер шрифта. По умолчанию 16.
            font_path (str, optional): Путь к файлу шрифта. По умолчанию "freesansbold.ttf".
            antialias (bool, optional): Включить сглаживание текста. По умолчанию True.
            background_color (tuple[int,int,int]|list[int,int,int]|str, optional): Цвет фона кнопки. По умолчанию "black".
            background_alpha (int, optional): Прозрачность фона кнопки (от 0 до 255). По умолчанию 0.
        """
        super().init(x, y, text, text_color,  text_alpha, font_size,  font_path,  antialias)

        self.__callback = callback
        self.__width = width if width != -1 else self.get_width() + h_padding * 2
        self.__height = height if height != -1 else self.get_height() + v_padding * 2

        self.__h_padding = h_padding
        self.__v_padding = v_padding

        self.__background_color = background_color
        self.__background_alpha = background_alpha
        self.__background_surface = pygame.Surface((self.__width, self.__height), pygame.SRCALPHA).convert_alpha()
        self.update_background()

    def press(self) -> None:
        """
        Вызывает исполняемую функцию.
        """
        self.__callback()

    def draw(self, surface:pygame.surface.Surface) -> None:
        """
        Отрисовывает кнопку на поверхности.

        Args:
          surface (pygame.surface.Surface): Поверхность, на которой будет отрисована кнопка.
        """
        x, y = self.get_pos()
        surface.blit(self.__background_surface, (x - self.__h_padding, y - self.__v_padding))
        surface.blit(self.get_render(), self.get_pos())

    def update_background(self):
        """
        Обновляет фон кнопки.
        """
        self.__background_surface.set_alpha(self.__background_alpha)
        self.__background_surface.fill(self.__background_color)

    def set_callback(self, callback:callable) -> None:
        """
        Устанавливает новую исполняемую функцию.

        Args:
          callback (callable): Новая функция обратного вызова.
        """
        self.__callback = callback

    def get_callback(self) -> callable:
        """
        Возвращает исполняемую функцию.

        Returns:
          callable: Исполняемая функция.
        """
        return self.__callback
