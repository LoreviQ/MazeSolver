from tkinter import Tk, BOTH, Canvas
import time

# Class for maze
class Maze:
    def __init__(self, p1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
        self._tl = p1 # Position of the top left point of the maze
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._cells = self._create_cells()
        #self._draw_cells(self._cells)
    
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
        time.sleep(0.05)



# Class for cells
class Cell:
    def __init__(self, p1, p2, window=None, left_wall=True, right_wall=True, top_wall=True, bottom_wall=True,):
        self._tl = Point(min(p1.x, p2.x), min(p1.y, p2.y)) # Top Left point
        self._tr = Point(max(p1.x, p2.x), min(p1.y, p2.y)) # Top Right point
        self._br = Point(max(p1.x, p2.x), max(p1.y, p2.y)) # Bottom Right point
        self._bl = Point(min(p1.x, p2.x), max(p1.y, p2.y)) # Bottom Left point
        self._window = window
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
    
    # Generates a line for each wall then draws it
    def draw(self):
        lines = []
        if self.left_wall:
            lines += [Line(self._tl, self._bl)]
        if self.right_wall:
            lines += [Line(self._tr, self._br)]
        if self.top_wall:
            lines += [Line(self._tl, self._tr)]
        if self.bottom_wall:
            lines += [Line(self._bl, self._br)]
        if lines:
            for line in lines:
                self._window.draw_line(line)
    
    # Draws a path between the centre of two cells
    def draw_move(self, to_cell, undo=False):
        c1 = Point((self._tl.x+self._br.x)/2, (self._tl.y+self._br.y)/2)
        c2 = Point((to_cell._tl.x+to_cell._br.x)/2, (to_cell._tl.y+to_cell._br.y)/2)
        if undo:
            color = "grey"
        else:
            color = "red"
        self._window.draw_line(Line(c1,c2), color)

# Class for point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Class for line
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)

# Class for GUI window
class Window:
    def __init__(self, width, height):
        # CONFIG
        TITLE = "title"

        # init
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title(TITLE)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas()
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
    
    # Draws line from input
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    # Updates window
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # Constantly calls redraw() until window is closed
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    # Called when window closed, stopping active code
    def close(self):
        self.__running = False