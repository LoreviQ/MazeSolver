import time
from graphics import Cell, Point
import random

# Class for maze
class Maze:
    def __init__(self, p1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self._tl = p1 # Position of the top left point of the maze
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._cells = self._create_cells()
        self._break_entrance_and_exit()

        if seed:
            random.seed(seed)

        # Draw window into UI
        if self._window:
            self._break_walls_r(0,1)
            self._draw_cells(self._cells)
    
    def _create_cells(self):
        cells = []
        for r in range(self._num_rows):
            columns = []
            for c in range(self._num_cols):
                x1 = self._tl.x + self._cell_size_x * c
                y1 = self._tl.y + self._cell_size_y * r
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                columns += [Cell(Point(x1, y1), Point(x2, y2), self._window)]
            cells += [columns]
        return cells   
    
    def _draw_cells(self, cells):
        for columns in cells:
            for cell in columns:
                cell.draw()
                self._animate()
    
    def _animate(self):
        self._window.redraw()
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._cells[self._num_rows-1][self._num_cols-1].bottom_wall = False
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            # Check Directions
            to_visit = []
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit += ["left"]
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit += ["right"]
            if i > 0 and not self._cells[i-1][j].visited: 
                to_visit += ["top"]
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited: 
                to_visit += ["bottom"]
            if not to_visit:
                #self._cells[i][j].draw()
                return
            
            # Move in direction
            direction = random.choice(to_visit)
            match direction:
                case "left":
                    self._cells[i][j].left_wall = False
                    self._cells[i][j - 1].right_wall = False
                    self._break_walls_r(i, j - 1)
                case "right":
                    self._cells[i][j].right_wall = False
                    self._cells[i][j + 1].left_wall = False
                    self._break_walls_r(i, j + 1)
                case "top":
                    self._cells[i][j].top_wall = False
                    self._cells[i - 1][j].bottom_wall = False
                    self._break_walls_r(i - 1, j)
                case "bottom":
                    self._cells[i][j].bottom_wall = False
                    self._cells[i + 1][j].top_wall = False
                    self._break_walls_r(i + 1, j)