from tkinter import Canvas
from points import Point
from typing import Optional

class Line:
    def __init__(self,
                 point_one: Point,
                 point_two: Point) -> None:
        self.__point_one = point_one
        self.__point_two = point_two

    @property
    def point_one(self) -> Point:
        return self.__point_one

    @point_one.setter
    def point_one(self, point: Point) -> None:
        if not isinstance(point, Point):
            raise TypeError(f'Error->Line: {point} point must be type Point. Type: {type(point)}')
        self.__point_one = point

    @property
    def point_two(self) -> Point:
        return self.__point_two

    @point_two.setter
    def point_two(self, point: Point) -> None:
        if not isinstance(point, Point):
            raise TypeError(f'Error->Line: {point} point must be type Point. Type: {type(point)}')
        self.__point_two = point

    def draw(self,
             canvas: Canvas,
             fill_color: Optional[str] = 'black') -> None:
        canvas.create_line(
            self.point_one.x,
            self.point_one.y,
            self.point_two.x,
            self.point_two.y,
            fill=fill_color,
            width=2
        )

    def __repr__(self):
        text = ''
        for key in self.__dict__.keys():
            text += f'{key}={self.__dict__[key]},'

        return f'{self.__class__.__name__}({text[:-1]})'
