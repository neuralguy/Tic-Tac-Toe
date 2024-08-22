import pygame
from cell import Cell
from config import WIDTH, HEIGHT, TILE_SIZE, NUM_CELLS_FOR_WIN


class Board:
    def __init__(self):
        self.__cells = [[Cell(x * TILE_SIZE, y * TILE_SIZE) for x in range(HEIGHT // TILE_SIZE)] for y in range(WIDTH // TILE_SIZE)]

    def draw(self, surface:pygame.surface.Surface) -> None:
        for x in range(0, WIDTH, TILE_SIZE):
            for y in range(0, HEIGHT, TILE_SIZE):
                pygame.draw.rect(surface, "white", (x, y, TILE_SIZE, TILE_SIZE), 1)

        for row in self.__cells:
            for cell in row:
                cell.draw(surface)

    def get_cell(self, row:int, col:int) -> Cell:
        for cell_row in self.__cells:
            for cell in cell_row:
                if [i // TILE_SIZE for i in cell.get_pos()] == [col, row]:
                    return cell

    def reset_cells(self) -> None:
        """Данная функция обнуляет значения во всех клетках"""
        for cell in sum(self.__cells, []):
            cell.set_state(None)

    def get_diagonal(self, matrix, row, col, row_dir, col_dir) -> list[Cell]:
        """Функция получает матрицу, строку, столбец, направление для движения по строке, направление для движения по столбцу и возвращает диагональ
        матрицы, начиная с элемента под индексами row и col"""
        diagonal = []

        while 0 < row < len(matrix) and 0 < col < len(matrix[0]):
            diagonal.append(matrix[row][col])
            row += row_dir
            col += col_dir

        return diagonal

    def check_win(self, row:int, col:int, player:int) -> bool|None:
        """Самая сложная функция из всего проекта. В ней рассчитывается количество идущих в ряд одинаковых фигур, и если оно равно необходимому для
        победы, то возвращается True, иначе ничего не возвращается(None). Если и разбираться в этом, то только попутно визуализируя происходящее. 
        Сам я это всё написал путём проб и ошибок часа за 2"""

        # Проверка строки
        for i in range(len(self.__cells[row]) - NUM_CELLS_FOR_WIN + 1):
            if all(self.__cells[row][i+j].get_state() == player for j in range(NUM_CELLS_FOR_WIN)):
                return True

        # Проверка столбца
        for i in range(len(self.__cells) - NUM_CELLS_FOR_WIN + 1):
            if all(self.__cells[i+j][col].get_state() == player for j in range(NUM_CELLS_FOR_WIN)):
                return True

        # Диагональ вправо
        for i in range(len(self.__cells) - NUM_CELLS_FOR_WIN + 1):
            min_el = min(row, col)
            if all(self.__cells[row - min_el + j][col - min_el + j] == player for j in range(NUM_CELLS_FOR_WIN)):
                return True
        diagonal = self.get_diagonal(self.__cells, row, col, 1, -1) # влево-вниз
        diagonal.extend(self.get_diagonal(self.__cells, row, col, -1, 1)) # вправо-вверх

        for i in range(len(diagonal) - NUM_CELLS_FOR_WIN + 1):
            states = [cell.get_state() for cell in diagonal[i:i+NUM_CELLS_FOR_WIN] if cell.get_state() is not None]
            if len(states) == NUM_CELLS_FOR_WIN and (sum(states) == NUM_CELLS_FOR_WIN or sum(states) == 0):
                return True

        # # Диагональ влево
        # diagonal = self.get_diagonal(self.__cells, row, col, -1, -1) # влево-вверх
        # diagonal.extend(self.get_diagonal(self.__cells, row, col, 1, 1)) # вправо-вниз

        # for i in range(len(diagonal) - NUM_CELLS_FOR_WIN + 1):
        #     states = [cell.get_state() for cell in diagonal[i:i+NUM_CELLS_FOR_WIN] if cell.get_state() is not None]
        #     if len(states) == NUM_CELLS_FOR_WIN and (sum(states) == NUM_CELLS_FOR_WIN or sum(states) == 0):
        #         return True


