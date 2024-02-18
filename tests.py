import unittest
from graphics import Point
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells_params1(self):
        #PARAMS
        p1 = Point(0,0)
        num_cols = 12
        num_rows = 10
        width = 100
        height = 100
        m1 = Maze(p1, num_rows, num_cols, width, height)

        #Test
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        self.assertEqual(
            m1._cells[0][0]._tr.x - m1._cells[0][0]._tl.x,
            width
        )
        self.assertEqual(
            m1._cells[3][3]._bl.y - m1._cells[3][3]._tl.y,
            height
        )
        self.assertEqual(
            m1._cells[5][6]._tl.x - m1._cells[5][5]._tl.x,
            width
        )
        self.assertEqual(
            m1._cells[3][2]._tl.y - m1._cells[2][2]._tl.y,
            height
        )
        self.assertEqual(
            m1._cells[3][2]._tl.x,
            2*width
        )

    def test_maze_create_cells_params2(self):
        #PARAMS
        p1 = Point(100,100)
        num_cols = 25
        num_rows = 20
        width = 50
        height = 25
        m1 = Maze(p1, num_rows, num_cols, width, height)

        #Test
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        self.assertEqual(
            m1._cells[0][0]._tr.x - m1._cells[0][0]._tl.x,
            width
        )
        self.assertEqual(
            m1._cells[3][3]._bl.y - m1._cells[3][3]._tl.y,
            height
        )
        self.assertEqual(
            m1._cells[5][6]._tl.x - m1._cells[5][5]._tl.x,
            width
        )
        self.assertEqual(
            m1._cells[3][2]._tl.y - m1._cells[2][2]._tl.y,
            height
        )
        self.assertEqual(
            m1._cells[3][2]._tl.x,
            p1.x + 2*width
        )

    def test_entrance_exit(self):
        #PARAMS
        p1 = Point(100,100)
        num_cols = 25
        num_rows = 20
        width = 50
        height = 25
        m1 = Maze(p1, num_rows, num_cols, width, height)
    
        #Test
        self.assertEqual(
            m1._cells[0][0].top_wall,
            False
        )
        self.assertEqual(
            m1._cells[19][24].bottom_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()