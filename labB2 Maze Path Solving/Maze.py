#!/usr/bin/python3

""" Maze module that supports drawing a maze and navigating within it. """

# Author: Dr. Steven P. Crain, Steven.Crain@plattsburgh.edu
# (C) Copyright 2017
# License: Creative commons non-commercial attribution license

import curses
import time

class MazeDone(Exception):
  """ Exception that is raised when navigation reaches an exit to the maze. """
  pass

class Maze:
  """ Maze is a class that provides display and navigation of a maze.

      The maze is provided as an array of strings, one string per row in the
      maze. The entry to the maze is marked by an "@" character. If there
      are multiple "@" character, the first "@" on the last line that contains
      an "@" is the entry. All exits are marked with "!". It is possible to
      navigate to the location of any space character. All other characters
      are walls.
  """
  def __init__(self, maze, delay=0):
    self.nowy=0
    self.nowx=1
    self.screen=None
    self.maze=maze
    self.rows=len(maze)
    self.cols=len(maze[0])
    self.delay=delay
    for y in range(self.rows):
      try:
        self.nowx=maze[y].index('@')
        self.nowy=y
      except ValueError:
        pass
  def location(self):
    return (self.nowy, self.nowx)
  def startCurses(self, screen):
    """ Start displaying the maze on the screen. """
    if screen is not None:
      self.screen=screen
      self.drawMazeCurses()
      self.refresh()
  def startInteractive(screen, self):
    """Start displaying the maze on screen."""
    self.startCurses(screen)
    try:
      while True:
        k=screen.getkey()
        if k=='KEY_UP':
          self.tryMove(self.nowy-1, self.nowx)
        elif k=='KEY_DOWN':
          self.tryMove(self.nowy+1, self.nowx)
        elif k=='KEY_LEFT':
          self.tryMove(self.nowy, self.nowx-1)
        elif k=='KEY_RIGHT':
          self.tryMove(self.nowy, self.nowx+1)
        else:
          return
    except MazeDone:
      self.screen.addstr(self.rows+1, self.nowx, "MAZE COMPLETED!")
      self.screen.addstr(self.rows+2, self.nowx, "Press any key.")
      self.screen.getkey()
  def validMove(self, y, x=None):
    """ Determine if (x,y) is a valid place to move to. """
    #print("A",y,x)
    if x is None:
      self.screen.addstr("y is ".format(y));
      self.screen.getkey()
      x=y[1]
      y=y[0]
    #print("Test {}, {} ".format(y,x))
    try:
      return 0 <= y < self.rows and 0 <= x < self.cols \
          and self.maze[y][x] in " @!"
    except:
      self.screen.addstr("({}, {})".format(y,x));
      self.screen.getkey()
      raise
  def tryMove(self, y, x=" ", backch=" "):
    """ Move to (y, x) if that is a legal place to be."""
    #print("B",y,x,backch)
    try:
      b=x
      x=y[1]
      y=y[0]
      backch=b
    except:
      pass
    if self.validMove(y, x):
      if len(backch)>1:
        backch=" "
      try:
        self.screen.addstr(self.nowy, self.nowx, backch)
      except:
        pass
      self.nowy=y
      self.nowx=x
      self.refresh()
      if self.maze[y][x]=="!":
        raise MazeDone("Maze Completed")
  def refresh(self):
    """Refresh the curses display."""
    time.sleep(self.delay)
    if self.screen is None:
      return
    self.screen.addstr(self.nowy, self.nowx, "@")
    self.screen.move(self.nowy, self.nowx)
    self.screen.refresh()
    #self.screen.getkey()
  def drawMazeCurses(self):
    """Draw the maze on the curses screen."""
    self.screen.clear()
    for y in range(self.rows):
      self.screen.addstr(y,0,self.maze[y])
      try:
        s=self.maze[y].index('@')
        self.screen.addstr(y,s,' ')
      except ValueError:
        pass
      try:
        s=self.maze[y].index('!')
        self.screen.addstr(y,s,' ')
      except ValueError:
        pass
  def moves(self, path):
    """ Get a list of legal moves to continue in the maze without
        revisiting anyplace visited in the path. The path should be
        a list of (y, x) tuples. The output is a possibly empty list of
        (y,x) tuples.
    """
    #print("C",path)
    last=path[-1]
    y=last[0] 
    x=last[1]
    #self.screen.addstr(20,0, str(path))
    ret=[]
    y-=1
    if self.validMove(y, x) and (y,x) not in path:
      ret.append((y,x))
    y+=2
    if self.validMove(y, x) and (y,x) not in path:
      ret.append((y,x))
    y-=1
    x-=1
    if self.validMove(y, x) and (y,x) not in path:
      ret.append((y,x))
    x+=2
    if self.validMove(y, x) and (y,x) not in path:
      ret.append((y,x))
    #self.screen.addstr(21,0, str(ret))
    #self.screen.getkey()
    return ret

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
  mazeController=Maze(maze)
  print(mazeController.location())
  print(mazeController.moves((mazeController.location(),)))
  curses.wrapper(Maze.startInteractive, mazeController)
