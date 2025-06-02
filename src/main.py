from graphics import Window, Point, Line, Rect

def main():
    win = Window(800, 600)

    lines = [
        Line(Point(100, 300), Point(200, 100)),
        Line(Point(200, 100), Point(200, 100)),
        Line(Point(100, 100), Point(200, 100)),
        Line(Point(100, 100), Point(300, 200)),
        Line(Point(100, 100), Point(200, 300))
    ]
    for line in lines:
        win.drawLine(line)

    rects = [
        Rect(win, Point(100,100), Point(150,150), "1000", "Blue"),
        Rect(win, Point(200,200), Point(150,150), "1111", "Blue"),
        Rect(win, Point(300,100), Point(150,350), "1001", "Blue"),
        Rect(win, Point(50,50), Point(100,100), "1111", "Red"),
        Rect(win, Point(125,125), Point(200,200), "1111", "Red"),
        Rect(win, Point(225,225), Point(250,250), "1111", "Red"),
        Rect(win, Point(300,300), Point(500,500), "1111", "Red")

    ]
    for rect in rects:
        rect.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()
