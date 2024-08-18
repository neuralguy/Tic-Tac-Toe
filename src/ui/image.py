import pygame


class Image:
    def __init__(self, 
            x: int, 
            y: int, 
            path: str, 
            alpha: int=255):
        self.__x = x
        self.__y = y
        self.__path = path
        self.__alpha = alpha
        self.__image = None
        self.load(path)
    """
    Инициализация объекта Image.

    Args:
        x: Координата X изображения.
        y: Координата Y изображения.
        path: Путь к изображению.
        alpha: Значение альфа-канала (0-255).
    """

    def draw(self, surface:pygame.surface.Surface) -> None:
        """
        Отрисовывает изображение на поверхности.

        Args:
            surface: Поверхность, на которую нужно отрисовать.
        """
        surface.blit(self.__image, (self.__x, self.__y))

    def load(self, path:str) -> None:
        """
        Загружает изображение из файла.

        Args:
            path: Путь к файлу изображения.
        """
        self.__image = pygame.image.load(path).convert_alpha()

    def scale(self, width:int, height:int):
        """
        Масштабирует изображение.

        Args:
            width: Новая ширина.
            height: Новая высота.
        """
        self.__image = pygame.transform.scale(self.__image, (width, height))
        return self

    def crop(self, x:int, y:int, width:int, height:int):
        """
        Обрезает изображение.

        Args:
            x: Координата X области обрезки.
            y: Координата Y области обрезки.
            width: Ширина области обрезки.
            height: Высота области обрезки.
        """
        self.__image = self.__image.subsurface((x, y, width, height))
        return self

    def get_pos(self) -> list[int,int]:
        return [self.__x, self.__y]
