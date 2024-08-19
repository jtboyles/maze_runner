from line import Line
from tkinter import Tk, BOTH, Canvas
from typing import Optional

class Window():
    def __init__(self,
                 width: int,
                 height: int) -> None:
        # root widget
        self.__root = Tk()
        self.__root.title('Maze Runner')
        self.__root.protocol('WM_DELETE_WINDOW', self.close)

        # canvas widget
        self.__canvas = Canvas(self.__root, bg='#303446', height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        # window state
        self.__running_state = False

    @property
    def canvas(self) -> Canvas:
        return self.__canvas

    @canvas.setter
    def canvas(self, canvas: Canvas) -> None:
        if not isinstance(canvas, Canvas):
            raise TypeError(f'Error->Window: canvas is not of type Canvas. Type: {type(canvas)}')
        self.__canvas = canvas

    def clear(self) -> None:
        self.canvas.delete('all')

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running_state = True
        while self.__running_state:
            self.redraw()

    def close(self) -> None:
        self.__running_state = False

    def draw_line(self,
             line: Line,
             fill_color: Optional[str] = 'black') -> None:
        line.draw(self.__canvas, fill_color)

    def __repr__(self):
        text = ''
        for key in self.__dict__.keys():
            text += f'{key}={self.__dict__[key]},'

        return f'{self.__class__.__name__}({text[:-1]})'
