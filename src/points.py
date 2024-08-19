class Point:
    def __init__(self,
                 x: int,
                 y: int) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x_cord: int) -> None:
        if not isinstance(x_cord, int):
            raise TypeError(f'Error->Point: {x_cord} coordinate must be an int. type: {type(x_cord)}')
        self.__x = x_cord

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y_cord: int) -> None:
        if not isinstance(y_cord, int):
            raise TypeError(f'Error->Point: {y_cord} coordinate must be an int. type: {type(y_cord)}')
        self.__y = y_cord

    def __repr__(self):
        text = ''
        for key in self.__dict__.keys():
            text += f'{key}={self.__dict__[key]},'

        return f'{self.__class__.__name__}({text[:-1]})'
