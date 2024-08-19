from maze import Maze
from graphics import *
from time import sleep
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A script to demonstrate keyword arguments")
    parser.add_argument("--line_speed", type=int, help="Line animation speed (in miliseconds). Default: 5.")
    parser.add_argument("--cell_speed", type=int, help="Cell animation speed (in miliseconds). Default: 5.")
    parser.add_argument("--num_cols", type=int, help="Animation speed (in miliseconds).")
    parser.add_argument("--num_rows", type=int, help="Animation speed (in miliseconds).")
    parser.add_argument("--cell_size_x", type=int, help="Animation speed (in miliseconds).")
    parser.add_argument("--cell_size_y", type=int, help="Animation speed (in miliseconds).")
    parser.add_argument("--no_cell_animation", action='store_true')
    parser.add_argument("--no_line_animation", action='store_true')
    parser.add_argument("--repeat_until_solved", action='store_true')
    args = parser.parse_args()

    maze_config = {
        'x1': 50,
        'y1': 50,
        'num_cols': 30,
        'num_rows': 30,
        'cell_size_x': 20,
        'cell_size_y': 20,
        'line_speed': 5,
        'cell_speed': 5,
        'no_cell_animation': False,
        'no_line_animation': False
    }

    program_config = {
        'repeat_until_solved': False
    }

    for key in vars(args):
        if key in maze_config:
            if vars(args)[key] is not None:
                maze_config[key] = vars(args)[key]
        elif key in program_config:
            if vars(args)[key] is not None:
                program_config[key] = vars(args)[key]

    print(maze_config)
    win_size_x = maze_config['num_cols'] * maze_config['cell_size_x'] + maze_config['x1'] * 2
    win_size_y = maze_config['num_rows'] * maze_config['cell_size_y'] + maze_config['y1'] * 2
    win = Window(win_size_x, win_size_y)

    while True:
        maze = Maze(
            **maze_config,
            window=win)
        if maze.solve():
            break
        if not program_config['repeat_until_solved']:
            break
        sleep(5)
        win.clear()

    win.wait_for_close()
