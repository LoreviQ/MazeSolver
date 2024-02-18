from graphics import Window, Line, Point, Cell
from maze import Maze

def main():
    window = Window(1000, 1000)
    maze = Maze(Point(100,100), 20, 20, 40, 40, window)
    window.wait_for_close()

if __name__ == "__main__":
    main()