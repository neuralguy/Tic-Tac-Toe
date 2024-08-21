# Don't forget pygame.init() before using it

import pygame

class Text:
    """
    Класс для отрисовки текста на экране.

    Атрибуты:
        __text (str): Текст для отрисовки.
        __text_color (tuple[int,int,int]|list[int,int,int]|str): Цвет текста.
        __text_alpha (int): Прозрачность текста (от 0 до 255).
        __font (pygame.font.Font): Шрифт для отрисовки текста.
        __render (pygame.surface.Surface): Отрисованный текст как поверхность.
        __width (int): Ширина текста.
        __height (int): Высота текста.
        __x (int): Координата x текста.
        __y (int): Координата y текста.
        __rect (pygame.Rect): Прямоугольник, описывающий текст.
        __antialias (bool): Включить сглаживание текста.
    """
    def __init__(self,
        x: int,
        y: int,
        text: str,
        name: str="",
        text_color: tuple[int,int,int]|list[int,int,int]|str=(156,157,158),
        text_alpha: int=1,
        font_size: int=16,
        font_path: str="freesansbold.ttf",
        antialias: bool=False) -> None:
        """
        Инициализация объекта Text.

        Args:
          x (int): Координата x текста.
          y (int): Координата y текста.
          text (str): Текст для отрисовки.
          text_color (tuple[int,int,int]|list[int,int,int]|str, optional): Цвет текста. По умолчанию "white".
          text_alpha (int, optional): Прозрачность текста (от 0 до 255). По умолчанию 1.
          font_size (int, optional): Размер шрифта. По умолчанию 16.
          font_path (str, optional): Путь к файлу шрифта. По умолчанию "freesansbold.ttf".
          antialias (bool, optional): Включить сглаживание текста. По умолчанию False.
        """
        self.__text = text
        self.__text_color = text_color
        self.__text_alpha = text_alpha

        self.__font = pygame.font.Font(font_path, font_size)
        self.__render = self.__font.render(text, antialias, text_color).convert_alpha()
        
        self.__width = self.__render.get_width()
        self.__height = self.__render.get_height()
        self.__x = x - self.__width // 2
        self.__y = y - self.__height // 2
        self.__rect = pygame.Rect((self.__x, self.__y), (self.__width, self.__height))

        self.__antialias = antialias

    def draw(self, surface:pygame.surface.Surface) -> None:
        """
        Отрисовывает текст на поверхности.

        Args:
          surface (pygame.surface.Surface): Поверхность, на которой будет отрисован текст.
        """
        surface.blit(self.__render, (self.__x, self.__y))
    
    def set_text(self, text:str) -> None:
        """
        Устанавливает новый текст.

        Args:
          text (str): Новый текст.
        """
        self.__text = text
        self.__render = self.__font.render(text, self.__antialias, self.__text_color)

    def set_text_color(self, text_color:tuple[int,int,int]|list[int,int,int]|str) -> None:
        """
        Устанавливает новый цвет текста.

        Args:
          text_color (tuple[int,int,int]|list[int,int,int]|str): Новый цвет текста.
        """
        self.__text_color= text_color
        self.__render = self.__font.render(self.__text, self.__antialias, text_color)

    def get_pos(self) -> tuple[int,int]:
        """
        Возвращает позицию текста.

        Returns:
          tuple[int,int]: Координаты x и y текста.
        """
        return (self.__x, self.__y)

    def get_text(self) -> str:
        """
        Возвращает текст.

        Returns:
          str: Текст.
        """
        return self.__text

    def get_text_color(self) -> tuple[int,int,int]|list[int,int,int]|str:
        """
        Возвращает цвет текста.

        Returns:
          tuple[int,int,int]|list[int,int,int]|str: Цвет текста.
        """
        return self.__text_color

    def get_render(self) -> pygame.surface.Surface:
        """
        Возвращает отрисованную поверхность текста.

        Returns:
          pygame.surface.Surface: Отрисованная поверхность текста.
        """
        return self.__render

    def get_width(self) -> int:
        """
        Возвращает ширину текста.

        Returns:
          int: Ширина текста.
        """
        return self.__width

    def get_height(self) -> int:
        """
        Возвращает высоту текста.

        Returns:
          int: Высота текста.
        """
        return self.__height

    def get_rect(self) -> pygame.rect.Rect:
        return self.__rect
