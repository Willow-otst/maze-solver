from maze import Maze

class Solver:
    def __init__(self, maze):
        self.maze = maze
        self.goal = (maze.length-1, maze.height-1)

        self.solve()

    def solve(self, x=0, y=0):
        self.maze.animate(0.2)

        currentCell = self.maze.cells[x][y]
        currentCell.visited = True

        if (x, y) == self.goal:
            return True

        # Check North
        if (x, y) != (0, 0) and not currentCell.hasNorth and not self.maze.cells[x][y-1].visited:
            nextCell = self.maze.cells[x][y-1]
            currentCell.drawMove(nextCell, True)
            if self.solve(x, y-1):
                return True
            currentCell.drawMove(nextCell, False)

        #Check East
        if not currentCell.hasEast and not self.maze.cells[x+1][y].visited:
            nextCell = self.maze.cells[x+1][y]
            currentCell.drawMove(nextCell, True)
            if self.solve(x+1, y):
                return True
            currentCell.drawMove(nextCell, False)

        #Check South
        if (x, y) != self.goal and not currentCell.hasSouth and not self.maze.cells[x][y+1].visited:
            nextCell = self.maze.cells[x][y+1]
            currentCell.drawMove(nextCell, True)
            if self.solve(x, y+1):
                return True
            currentCell.drawMove(nextCell, False)

        #Check West
        if not currentCell.hasWest and not self.maze.cells[x-1][y].visited:
            nextCell = self.maze.cells[x-1][y]
            currentCell.drawMove(nextCell, True)
            if self.solve(x-1, y):
                return True
            currentCell.drawMove(nextCell, False)

        return False
