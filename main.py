from tkinter import Tk, BOTH, Canvas

# Class for point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Class for line
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)
        canvas.pack()

# Class for GUI window
class Window:
    def __init__(self, width, height):
        #CONFIG
        TITLE = "title"

        #init
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title(TITLE)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
    
    # Updates window
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    # Constantly calls redraw() until window is closed
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    # Called when window closed, stopping active code
    def close(self):
        self.running = False
        

def main():
    window = Window(400, 400)
    window.wait_for_close()

if __name__ == "__main__":
    main()