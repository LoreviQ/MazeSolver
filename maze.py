import time
from graphics import Cell, Point
import random
import sys 


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
        self._break_walls_r(0,1)
        self._reset_cells_visited()

        # Draw window into UI
        if self._window:
            self._draw_cells()
            self.solve()
    
    def _create_cells(self):
        cells = []
        for r in range(self._num_rows):
            row = []
            for c in range(self._num_cols):
                x1 = self._tl.x + self._cell_size_x * c
                y1 = self._tl.y + self._cell_size_y * r
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                row += [Cell(Point(x1, y1), Point(x2, y2), self._window)]
            cells += [row]
        return cells   
    
    def _draw_cells(self):
        for row in self._cells:
            for cell in row:
                cell.draw()
    
    def _animate(self):
        self._window.redraw()
        time.sleep(0.02)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._cells[self._num_rows-1][self._num_cols-1].bottom_wall = False
    
    def _break_walls_r(self, row, column):
        cells = self._get_adjacent_cells(row, column)

        cells["this"].visited = True 
        while True:
            # Check Directions
            try:
                to_visit = []
                if cells["left"] and not cells["left"].visited:
                    to_visit += ["left"]
                if cells["right"] and not cells["right"].visited:
                    to_visit += ["right"]
                if cells["top"] and not cells["top"].visited: 
                    to_visit += ["top"]
                if cells["bottom"] and not cells["bottom"].visited: 
                    to_visit += ["bottom"]
                if not to_visit:
                    return
            except:
                print(self._cells)
                print(cells)
                sys.exit()
            
            # Move in direction
            direction = random.choice(to_visit)
            match direction:
                case "left":
                    cells["this"].left_wall = False
                    cells[direction].right_wall = False
                    self._break_walls_r(row, column - 1)
                case "right":
                    cells["this"].right_wall = False
                    cells[direction].left_wall = False
                    self._break_walls_r(row, column + 1)
                case "top":
                    cells["this"].top_wall = False
                    cells[direction].bottom_wall = False
                    self._break_walls_r(row - 1, column)
                case "bottom":
                    cells["this"].bottom_wall = False
                    cells[direction].top_wall = False
                    self._break_walls_r(row + 1, column)

    def _get_adjacent_cells(self, row, column):
        cells = {"this": self._cells[row][column],}
        if column > 0:
            cells["left"] = self._cells[row][column-1]
        if column < self._num_cols - 1:
            cells["right"] = self._cells[row][column+1],
        if row > 0: 
            cells["top"] = self._cells[row-1][column]
        if row < self._num_rows - 1: 
            cells["bottom"] = self._cells[row+1][column]

        for direction in ["left", "right", "top", "bottom"]:
            if direction not in cells:
                cells[direction] = None

        for key in cells:
            if type(cells[key]) is tuple:
                cells[key] = cells[key][0]

        return cells

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
    
    def solve(self):
        self._solve_r(0,0)
    
    def _solve_r(self, row, column):
        self._animate()
        cells = self._get_adjacent_cells(row, column)

        cells["this"].visited = True
        if row == self._num_rows - 1 and column == self._num_cols - 1:
            return True
        
        if cells["left"] and not cells["left"].visited and not cells["this"].left_wall and not cells["left"].right_wall:
            cells["this"].draw_move(cells["left"])
            if self._solve_r(row, column-1):
                return True
            cells["this"].draw_move(cells["left"], undo=True)
        if cells["right"] and not cells["right"].visited and not cells["this"].right_wall and not cells["right"].left_wall:
            cells["this"].draw_move(cells["right"])
            if self._solve_r(row, column+1):
                return True
            cells["this"].draw_move(cells["right"], undo=True)
        if cells["top"] and not cells["top"].visited and not cells["this"].top_wall and not cells["top"].bottom_wall:
            cells["this"].draw_move(cells["top"])
            if self._solve_r(row-1, column):
                return True
            cells["this"].draw_move(cells["top"], undo=True)
        if cells["bottom"] and not cells["bottom"].visited and not cells["this"].bottom_wall and not cells["bottom"].top_wall:
            cells["this"].draw_move(cells["bottom"])
            if self._solve_r(row+1, column):
                return True
            cells["this"].draw_move(cells["bottom"], undo=True)
        
        return False