import unittest
from maze import Maze
from graphics import *

# window used for testing
class DummyWindow(Window):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.draw_calls = []

    def drawLine(self, line, fillColor="Black"):
        self.draw_calls.append((line.p1.x, line.p1.y, line.p2.x, line.p2.y, fillColor))

    def redraw(self):
        pass

class TestMaze(unittest.TestCase):

    # Setup runs before each test; creates a dummy window
    def setUp(self):
        self.window = DummyWindow(200, 200)

    # Test that the correct number of cells (columns and rows) is created
    def test_create_cells_grid_size(self):
        maze = Maze(self.window, 4, 5)
        self.assertEqual(len(maze.cells), 4)  # 4 columns
        for col in maze.cells:
            self.assertEqual(len(col), 5)  # 5 rows per column

    # Test that the positions of the first cell are correctly calculated
    def test_cell_positions(self):
        maze = Maze(self.window, 2, 2)
        margin = 10
        expected_width = (self.window.width - 2 * margin) / 2
        expected_height = (self.window.height - 2 * margin) / 2

        cell = maze.cells[0][0]
        self.assertAlmostEqual(cell.p1.x, margin)
        self.assertAlmostEqual(cell.p1.y, margin)
        self.assertAlmostEqual(cell.p2.x, margin + expected_width)
        self.assertAlmostEqual(cell.p2.y, margin + expected_height)

    # Test that drawCells() causes lines to be drawn (via drawLine)
    def test_draw_cells_adds_lines(self):
        maze = Maze(self.window, 2, 2)
        maze.drawCells()
        self.assertGreater(len(self.window.draw_calls), 0)


if __name__ == "__main__":
    unittest.main()
