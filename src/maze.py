from graphics import Window
from cell import Cell
from time import sleep
from typing import Optional
from enum import Enum
import random

class Animation(Enum):
    CELL = 'cell'
    LINE = 'line'

class Maze:
    def __init__(self,
                 x1: int,
                 y1: int,
                 num_rows: int,
                 num_cols: int,
                 cell_size_x: int,
                 cell_size_y: int,
                 seed: Optional[int] = None,
                 line_speed: Optional[int] = None,
                 cell_speed: Optional[int] = None,
                 no_cell_animation: Optional[bool] = False,
                 no_line_animation: Optional[bool] = False,
                 window: Optional[Window] = None) -> None:
        # start position
        self.__x1 = x1
        self.__y1 = y1

        # cell details
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y

        # cells
        self.__cells = []

        # window
        self.__window = window

        # animation speed
        self.__animation_speed = {
            'line': line_speed * .01 if line_speed else 0.05,
            'cell': cell_speed * .01 if cell_speed else 0.05
        }
        self.no_cell_animation = no_cell_animation
        self.no_line_animation = no_line_animation

        # draw maze
        if seed:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self._reset_cells_visited()

    @property
    def x1(self) -> int:
        return self.__x1

    @x1.setter
    def x1(self, x: int) -> None:
        if not isinstance(x, int):
            raise TypeError(f'Error->Maze: x1 is not type int. Type: {type(x)}')

    @property
    def y1(self) -> int:
        return self.__y1

    @y1.setter
    def y1(self, y: int) -> None:
        if not isinstance(y, int):
            raise TypeError(f'Error->Maze: y1 is not type int. Type: {type(y)}')

    @property
    def num_cols(self) -> int:
        return self.__num_cols

    @num_cols.setter
    def num_cols(self, n: int) -> None:
        if not isinstance(n, int):
            raise TypeError(f'Error->Maze: num_cols is not type int. Type: {type(n)}')

    @property
    def num_rows(self) -> int:
        return self.__num_rows

    @num_rows.setter
    def num_rows(self, n: int) -> None:
        if not isinstance(n, int):
            raise TypeError(f'Error->Maze: num_rows is not type int. Type: {type(n)}')

    @property
    def cell_size_x(self) -> int:
        return self.__cell_size_x

    @cell_size_x.setter
    def cell_size_x(self, n: int) -> None:
        if not isinstance(n, int):
            raise TypeError(f'Error->Maze: cell_size_x is not type int. Type: {type(n)}')

    @property
    def cell_size_y(self) -> int:
        return self.__cell_size_y

    @cell_size_y.setter
    def cell_size_y(self, n: int) -> None:
        if not isinstance(n, int):
            raise TypeError(f'Error->Maze: cell_size_y is not type int. Type: {type(n)}')

    @property
    def cells(self) -> list:
        return self.__cells

    @property
    def window(self) -> Window | None:
        return self.__window

    @window.setter
    def window(self, window: Window) -> None:
        if not isinstance(window, Window):
            raise TypeError(f'Error->Maze: window is not type Window. Type: {type(window)}')

    def __create_cells(self) -> None:
        self.__cells = [[Cell(self.window) for x in range(self.num_rows)] for x in range(self.num_cols)]

        if not self.window:
            return
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self,
                    i: int,
                    j: int) -> None:
        if not self.window:
            return
        x_offset = i * self.cell_size_x + self.x1
        y_offset = j * self.cell_size_y + self.y1
        x_end = x_offset + self.__cell_size_x
        y_end = y_offset + self.__cell_size_y
        self.__cells[i][j].draw(x_offset, y_offset, x_end, y_end)
        self.__animate(Animation.CELL)

    def __animate(self, type: str) -> None:
        if not self.window:
            return
        self.window.redraw()
        if type == Animation.CELL and self.no_cell_animation:
            return
        if type == Animation.LINE and self.no_line_animation:
            return
        sleep(self.__animation_speed[type.value])

    def _reset_cells_visited(self) -> None:
        for i in self.cells:
            for j in i:
                j.visited = False

    def __break_entrance_and_exit(self) -> None:
        self.cells[0][0].wall_left = False
        self.__draw_cell(0, 0)
        self.cells[-1][-1].wall_right = False
        self.__draw_cell(self.num_cols -1, self.num_rows -1)

    def __break_walls_r(self,
                        i: int,
                        j: int) -> None:
        self.cells[i][j].visited = True
        while True:
            to_visit = []
            # determine which cell(s) to visit next
            # left
            if i > 0 and not self.cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # up
            if j > 0 and not self.cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if not to_visit:
                self.__draw_cell(i, j)
                return

            dir = to_visit[random.randrange(len(to_visit))]
            dir_x = dir[0]
            dir_y = dir[1]
            # right
            if dir_x == i + 1:
                self.cells[i][j].wall_right = False
                self.cells[i+1][j].wall_left = False
            # left
            if dir_x == i - 1 and dir_x > 0:
                self.cells[i][j].wall_left = False
                self.cells[i - 1][j].wall_right = False
            # down
            if dir_y == j + 1:
                self.cells[i][j].wall_bottom = False
                self.cells[i][j + 1].wall_top = False
            # up
            if dir_y  == j - 1 and dir_y > 0:
                self.cells[i][j].wall_top = False
                self.cells[i][j - 1].wall_top = False

            self.__break_walls_r(dir_x, dir_y)

    def solve(self) -> bool:
        return self.__solve_r(0, 0)

    def __solve_r(self,
                  i: int,
                  j: int) -> bool:
        self.__animate(Animation.LINE)
        self.cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # left
        if (i > 0 and
            self.cells[i-1][j] and
            not self.cells[i][j].wall_left and
            not self.cells[i-1][j].visited):
            self.cells[i][j].draw_move(self.cells[i-1][j])
            if self.__solve_r(i-1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i-1][j], undo=True)

        # right
        if (i < self.num_cols - 1 and
            self.cells[i+1][j] and
            not self.cells[i][j].wall_right and
            not self.cells[i+1][j].visited):
            self.cells[i][j].draw_move(self.cells[i+1][j])
            if self.__solve_r(i+1, j):
                return True
            self.cells[i][j].draw_move(self.cells[i+1][j], undo=True)

        # up
        if (j > 0 and
            self.cells[i][j-1] and
            not self.cells[i][j].wall_top and
            not self.cells[i][j-1].visited):
            self.cells[i][j].draw_move(self.cells[i][j-1])
            if self.__solve_r(i, j-1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j-1], undo=True)

        # down
        if (j < self.num_rows - 1 and
            self.cells[i][j+1] and
            not self.cells[i][j].wall_bottom and
            not self.cells[i][j+1].visited):
            self.cells[i][j].draw_move(self.cells[i][j+1])
            if self.__solve_r(i, j+1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j+1], undo=True)
        return False

