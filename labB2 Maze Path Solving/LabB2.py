#!/usr/bin/python3
#Alejo Pijuan and Kevin Saint-Fort
""" Demonstrate using a stack to find a solution to a maze. """

import Maze
import curses



def solve(screen, maze):
  """ Return a list containing the path through the maze that solves the
      maze. If screen is not None, show the progress to solution on the
      screen. Return None if no solution path is found. 
  """

  maze.startCurses(screen)
  theStack=Stack()
  theStack.push([maze.location()])
  alreadyPassed = set()
  while len(theStack) >=1:
    try:
      tryToMove(maze, theStack, alreadyPassed)
    except MazeDone as fin1:
      return fin1.path

    
def tryToMove(maze, theStack, alreadyPassed):
  """Will try to find the possible paths and move"""
  path = theStack.pop()
  try:
    maze.tryMove(path[-1], ".")
  except Maze.MazeDone:
    raise MazeDone(path)
  for i in maze.moves(path):
    if i not in alreadyPassed:
      alreadyPassed.add(i)
      path2 = path.copy()
      path2.append(i)
      theStack.push(path2)
    
class Stack:
  """ An implemtation of a stack. """
  def __init__(self):
    """intitializer constructor for the whole class"""
    self.info = []

  def __len__(self):
    """will return the lenght of self.info"""
    return len(self.info)

  def __iter__(self):
    """iter shall pass by each element and holla at them"""
    return self.info.__iter__()

  def peek(self):
    """looks at info[-1] from the list, without affecting it"""
    return self.info[-1]
  
  def push(self, avalue):
    """push it good, push it real good - Salt n Pepa"""
    self.info.append(avalue)

  def pop(self):
    """Pops the lastmost element from the list"""
    return self.info.pop()



class MazeDone(Exception):
  """Creates exception and acts on it with try and exception"""
  def __init__(self, path):
    Exception.__init__(self)
    self.path = path

def lookFor(screen, maze):
  maze.startCurses(screen)
  try:
    forNext(maze, (maze.nowy, maze.nowx))
  except MazeDone as fin2:
    return fin2.path


def forNext(maze, nextOne, path = []):
  try:
    maze.tryMove(nextOne[0], nextOne[1], ".")
  except Maze.MazeDone:
    path.append(nextOne)
    raise MazeDone(path)
  path.append(nextOne)
  total.append(path.copy())
  for nextOne in maze.moves(path):
    forNext(maze, nextOne, path)
  path.pop()






  
  
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
