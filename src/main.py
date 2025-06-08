from graphics import Window, Point, Line, Rect
from maze import Maze
from solver import Solver

def main():
    win = Window(800, 600)

    print("\nCreating Maze...")
    maze = Maze(win, 10, 10, 10, None)
    print("Maze Created.\n")

    print("Solving Maze...")
    solver = Solver(maze)
    print("Maze Solved.\n")

    print("Awaiting Window Close.")
    win.wait_for_close()

if __name__ == "__main__":
    main()
