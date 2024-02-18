from tkinter import Tk, BOTH, Canvas
import time

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
    def draw_line(self, line, fill_color):
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
        

def main():
    window = Window(1000, 1000)
    l1 = Line(Point(500,500),Point(1000,0))
    window.draw_line(l1, "red")
    window.wait_for_close()

if __name__ == "__main__":
    main()