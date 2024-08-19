from points import Point
from line import Line
from graphics import Window
from typing import Optional

class Cell:
    def __init__(self, window: Optional[Window] = None) -> None:
        # wall status
        self.wall_left = True
        self.wall_right = True
        self.wall_top = True
        self.wall_bottom = True

        # cell coordinates
        self.__x1 = 0
        self.__y1 = 0
        self.__x2 = 0
        self.__y2 = 0

        # visited
        self.__visited = False

        # draw window
        self.__window = window

    @property
    def x1(self) -> int:
        return self.__x1

    @x1.setter
    def x1(self, x1: int) -> None:
        if not isinstance(x1, int):
            raise TypeError(f'Error->Cell: x1 type is not int. Type: {type(x1)}')
        self.__x1 = x1

    @property
    def x2(self) -> int:
        return self.__x2

    @x2.setter
    def x2(self, x2: int) -> None:
        if not isinstance(x2, int):
            raise TypeError(f'Error->Cell: x2 type is not int. Type: {type(x2)}')
        self.__x2 = x2

    @property
    def y1(self) -> int:
        return self.__y1

    @y1.setter
    def y1(self, y1: int) -> None:
        if not isinstance(y1, int):
            raise TypeError(f'Error->Cell: y1 type is not int. Type: {type(y1)}')
        self.__y1 = y1

    @property
    def y2(self) -> int:
        return self.__y2

    @y2.setter
    def y2(self, y2: int) -> None:
        if not isinstance(y2, int):
            raise TypeError(f'Error->Cell: y2 type is not int. Type: {type(y2)}')
        self.__y2 = y2

    @property
    def visited(self) -> bool:
        return self.__visited

    @visited.setter
    def visited(self, visited: bool) -> None:
        self.__visited = visited

    @property
    def window(self) -> Window:
        return self.__window

    @window.setter
    def window(self, window: Window) -> None:
        if not isinstance(window, Window):
            raise TypeError(f'Error->Cell: window type is not Window. Type: {type(window)}')
        self.__window = window

    def center(self) -> Point:
        x = abs(self.x2 - self.x1) // 2 + self.x1
        y = abs(self.y2 - self.y1) // 2 + self.y1
        return Point(x, y)

    def draw(self,
             x1: int,
             y1: int,
             x2: int,
             y2: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if not self.window:
            return

        draw_func = lambda x1, y1, x2, y2, wall: self.window.draw_line(Line(Point(x1, y1), Point(x2, y2)), '#babbf1' if wall else '#303446')
        draw_func(self.x1, self.y1, self.x1, self.y2, self.wall_left)   # wall_left
        draw_func(self.x2, self.y1, self.x2, self.y2, self.wall_right)  # wall right
        draw_func(self.x1, self.y2, self.x2, self.y2, self.wall_bottom)    # wall top
        draw_func(self.x1, self.y1, self.x2, self.y1, self.wall_top) # wall bottom:

    def draw_move(self,
                  to_cell,
                  undo: Optional[bool] = False) -> None:
        line_start = self.center()
        line_end = to_cell.center()
        fill_color = '#838ba7' if undo else '#a6d189'
        line = Line(line_start, line_end)
        line.draw(self.window.canvas, fill_color=fill_color)

    def __repr__(self):
        text = ''
        for key in self.__dict__.keys():
            text += f'{key}={self.__dict__[key]},'

        return f'{self.__class__.__name__}({text[:-1]})'
