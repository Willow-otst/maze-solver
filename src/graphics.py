from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        print("window created...")

    def drawLine(self, line, fillColor="Black"):
        line.draw(self.canvas, fillColor)


    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        print("window running...")
        while self.running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fillColor="Black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fillColor, width=2
        )

class Rect:
    def __init__(self, window, p1=Point(-1,-1), p2=Point(-1,-1), walls="1111", fillColor="Black"):
        if len(walls) != 4:
            raise ValueError(f"Expected length of 4, got {len(walls)}: {walls!r}\n")
        if any(char not in '01' for char in walls):
            raise ValueError(f"Invalid characters in string: {binary_str!r}\n")

        self.window = window

        self.fillColor = fillColor

        self.p1 = p1
        self.p2 = p2

        # walls = "0000" indicates existing walls
        # each char can be 0 or 1 -> a 1 means a wall exitsts
        # they refer to walls in order: NORTH, EAST, SOUTH, WEST
        self.hasNorth = (self.hasWall(walls[0]))
        self.hasEast = (self.hasWall(walls[1]))
        self.hasSouth = (self.hasWall(walls[2]))
        self.hasWest =  (self.hasWall(walls[3]))

    # helper function
    def hasWall(self, val):
        return val == '1'

    def draw(self):
        if self.hasNorth:
            line = Line(Point(self.p1.x, self.p1.y), Point(self.p2.x, self.p1.y))
            self.window.drawLine(line, self.fillColor)
        if self.hasEast:
            line = Line(Point(self.p2.x, self.p1.y), Point(self.p2.x, self.p2.y))
            self.window.drawLine(line, self.fillColor)
        if self.hasSouth:
            line = Line(Point(self.p1.x, self.p2.y), Point(self.p2.x, self.p2.y))
            self.window.drawLine(line, self.fillColor)
        if self.hasWest:
            line = Line(Point(self.p1.x, self.p1.y), Point(self.p1.x, self.p2.y))
            self.window.drawLine(line, self.fillColor)

    def drawMove(self, toCell, undo=False):
        line = Line(self.getCenter(), toCell.getCenter())
        self.window.drawLine(line, "Red" if undo else "Gray")

    def getCenter(self):
        return Point((self.p1.x + self.p2.x)/2, (self.p1.y + self.p2.y)/2)







