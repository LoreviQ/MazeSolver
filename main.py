from graphics import Window, Line, Point, Cell

def main():
    window = Window(1000, 1000)
    cells = []
    for i in range(100, 900, 200):
        for j in range(100, 900, 200):
            cell = Cell(Point(i,j),Point(i+200,j+200), window)
            cell.draw()
            cells += [cell]
    cells[0].draw_move(cells[1])
    cells[1].draw_move(cells[5])
    cells[5].draw_move(cells[9])
    cells[9].draw_move(cells[10])
    window.wait_for_close()

if __name__ == "__main__":
    main()