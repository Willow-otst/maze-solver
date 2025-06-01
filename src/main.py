from graphics import Window, Point, Line

def main():
    lines = [
        Line(Point(100, 100), Point(200, 100)),
        Line(Point(200, 100), Point(200, 100)),
        Line(Point(100, 300), Point(200, 100)),
        Line(Point(100, 100), Point(300, 200)),
        Line(Point(100, 100), Point(200, 300))
    ]

    win = Window(800, 600)
    for line in lines:
        win.drawLine(line, "Black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
