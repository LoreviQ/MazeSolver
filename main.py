from graphics import Window, Line, Point

def main():
    window = Window(1000, 1000)
    l1 = Line(Point(500,500),Point(1000,0))
    window.draw_line(l1, "red")
    window.wait_for_close()

if __name__ == "__main__":
    main()