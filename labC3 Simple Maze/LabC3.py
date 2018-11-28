#!/usr/bin/python3

""" Demonstrate using a stack to find a solution to a maze. """

import Maze

class Stack:
  """ An implemtation of a stack. """

def solve(screen, maze):
  """ Return a list containing the path through the maze that solves the
      maze. If screen is not None, show the progress to solution on the
      screen. Return None if no solution path is found. 
  """
  maze.startCurses(screen)
  path=[maze.location()]
  # Create a stack.
  # Push the initial path onto the stack.
  # Until the stack is empty or a solution is found,
    # Pop a path off the stack.
    # Get the last move from the path.
    # Use maze.tryMove(move, ".") to test if the path is a solution.
    # Use maze.moves(path) to get a list of legal moves.
    # For each legal move:
      # Make a copy of path and append the legal move to the copy.
      # Push the new copy of the path onto the stack.

if __name__ == "__main__":
  import curses
  maze=( "+----+@+---+", \
         "|    | |   |", \
         "| +--+ | | |", \
         "| |    | | |", \
         "| | ---+ +-+", \
         "| |      | |", \
         "| | +--+-+ |", \
         "| | |  |   |", \
         "| |      +-+", \
         "| +-+ -+ | |", \
         "|   |  |   |", \
         "+---+--+!--+" )
  mazeController=Maze.Maze(maze,.5)
  print("PATH:")
  print(curses.wrapper(solve, mazeController))

  # Example of reading a maze from a file:
  #f=open("nomaze.txt", "r")
  #mazeController=Maze.Maze([line for line in f],0)
  #f.close()
  #print(curses.wrapper(solve, mazeController))
