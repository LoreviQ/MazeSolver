from graphics import Window, Line, Point, Cell

def main():
    window = Window(1000, 1000)
    for i in range(100, 900, 200):
        for j in range(100, 900, 200):
            cell = Cell(Point(i,j),Point(i+200,j+200), window)
            cell.draw()
    window.wait_for_close()

if __name__ == "__main__":
    main()