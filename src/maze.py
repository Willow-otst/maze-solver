from graphics import Window, Point, Line, Rect
import time

class Maze:
    def __init__(self, window, length, height, margin=10):
        self.window = window
        self.length = length
        self.height = height
        self.margin = margin

        self.cells = self.createCells()
        self.createExits()

    def createCells(self):
        startPoint = Point(0+self.margin, 0+self.margin)

        cellLength = (self.window.width - (self.margin*2)) / self.length
        cellHeight = (self.window.height - (self.margin*2)) / self.height

        cellArray = []
        for i in range(self.length):
            col = []
            for j in range(self.height):
                x = startPoint.x + (cellLength * i)
                y = startPoint.y + (cellHeight * j)
                cell = Rect(self.window, Point(x, y), Point(x+cellLength, y+cellHeight))
                col.append(cell)
            cellArray.append(col)
        return cellArray

    def createExits(self):
        #create enterance
        enterance = self.cells[0][0]
        enterance.hasNorth = False
        enterance.draw()

        #create exit
        exit = self.cells[self.length-1][self.height-1]
        exit.hasSouth = False
        exit.draw()

    def drawCells(self):
        for i in range(self.length):
            for j in range(self.height):
                self.cells[i][j].draw()
                self.animate()

    def animate(self):
        self.window.redraw()
        time.sleep(0.005)
