import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 15
        num_rows = 20
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
                m1.cells[0][0].wall_left,
                False
        )
        self.assertEqual(
                m1.cells[-1][-1].wall_right,
                False
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 25
        num_rows = 19
        m1 = Maze(0, 0, num_rows, num_cols,  10, 10)
        m2 = m1
        for i in range(num_cols):
            for j in range(num_rows):
                m1.cells[i][j].visited = True

        m1._reset_cells_visited()
        self.assertEqual(m1.cells, m2.cells)

if __name__ == "__main__":
    unittest.main()
