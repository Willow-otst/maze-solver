from graphics import Window, Point, Line, Rect
import time
import random

class Maze:
    def __init__(self, window, length, height, margin=10, seed=None):
        self.window = window

        self.length = length
        self.height = height

        self.margin = margin

        if seed != None: random.seed(seed)

        self.cells = self.createCells()
        self.createExits()
        self.drawCells()
        self.createPaths()

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
        self.cells[0][0].setWalls("0---", False)

        #create exit
        self.cells[self.length-1][self.height-1].setWalls("--0-", False)

    def createPaths(self):
        self.walkCells(0, 0)
        self.resetVisitedCells()

    # recursive helper function
    def walkCells(self, x, y):
        self.cells[x][y].visited = True

        while True:
            newPaths = []
            if y-1 >= 0 and self.cells[x][y-1].visited == False:
                newPaths.append((x, y-1))
            if x+1 < self.length and self.cells[x+1][y].visited == False:
                newPaths.append((x+1, y))
            if y+1 < self.height and self.cells[x][y+1].visited == False:
                newPaths.append((x, y+1))
            if x-1 >= 0 and self.cells[x-1][y].visited == False:
                newPaths.append((x-1, y))

            if not newPaths:
                return

            newX, newY = random.choice(newPaths)
            currentCell = self.cells[x][y]
            newCell = self.cells[newX][newY]
            if y-1 == newY: # We went N
                currentCell.setWalls("0---", True)
                newCell.setWalls("--0-", True)
            if x+1 == newX: # We went E
                currentCell.setWalls("-0--", True)
                newCell.setWalls("---0", True)
            if y+1 == newY: # We went S
                currentCell.setWalls("--0-", True)
                newCell.setWalls("0---", True)
            if x-1 == newX: # We went W
                currentCell.setWalls("---0", True)
                newCell.setWalls("-0--", True)

            #currentCell.drawMove(newCell, True)
            self.animate(0.03)
            self.walkCells(newX, newY)

    # helper for createPaths
    def resetVisitedCells(self):
        for i in range(self.length):
            for j in range(self.height):
                self.cells[i][j].visited = False

    def drawCells(self):
        for i in range(self.length):
            for j in range(self.height):
                self.cells[i][j].draw()
                self.animate(0.02)

    def animate(self, speed):
        self.window.redraw()
        time.sleep(speed)
