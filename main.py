from graphics import Window, Line, Point, Cell, Maze

def main():
    window = Window(1000, 1000)
    maze = Maze(Point(100,100), 8, 8, 100, 100, window)
    window.wait_for_close()

if __name__ == "__main__":
    main()