#!/usr/bin/python3

import signal
import unittest

class TimeoutError(Exception):
  pass

def timeout_handler(sig, frame):
  raise TimeoutError('Timeout on line ' + str(frame.f_lineno) \
      + ' in ' + frame.f_code.co_filename)

def enter(duration=10):
  signal.signal(signal.SIGALRM, timeout_handler)
  signal.alarm(duration)

def exit():
  signal.alarm(0)

class LabB2Tests(unittest.TestCase):
  def test_importable(self):
    msg=("""
Your program failed the importability test.
This test can fail if the Python code in your file is invalid.
This test can also fail if your file contains code that runs when it
should not. If your file contains test code, it should only run if
your file is the main program. Such code would look like this:

def foo(bar):
    \"\"\"Do foo.\"\"\"
    return bar

if __name__ == "__main__":
    print('Test: foo("Hello World")')
    print('Expected answer: Hello World')
    ans = foo("Hello World")
    print('Actual answer: {}'.format(ans))
""")
    enter()
    import LabB2
    exit()
  def test_Stack_class(self):
    enter()
    from LabB2 import Stack
    self.assertEqual(type(Stack).__name__,'type', msg='This means that your file does not define a class named "Stack."')
    exit()
  def test_solve_function(self):
    msg=("""
This means that you do not have a solve function.
""")
    enter()
    from LabB2 import solve
    from types import FunctionType
    self.assertEqual(type(solve),FunctionType, msg=msg)
    exit()
  def test_solve_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    import LabB2, Maze
    msg=("""
Most commonly your program fails this test if you use a print statement
in your append function. You must not print anything in class methods.
Instead, you should return the data so that the test code can access it.

Wrong:

def add(a, b):
    ""\" Add a and b.""\"
    print(a+b)

Right:

def add(a, b):
    ""\" Return the sum of a and b.""\"
    return a+b
""")
    enter()
    oldout = sys.stdout
    maze=Maze.Maze(("#@##", "#  #", "##!@"), 0)
    buf=StringIO()
    try:
      sys.stdout=buf
      LabB2.solve(None, maze)
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0, msg=msg)
    exit()
  def test_maze1(self):
    enter()
    import Maze, LabB2
    name="maze1.txt"
    f=open(name, "r")
    maze=Maze.Maze([line for line in f], 0)
    f.close()
    self.assertListEqual(LabB2.solve(None, maze), \
        [(0, 0), (0, 1)], \
        msg="The solution is wrong.")
  def test_maze2(self):
    enter()
    import Maze, LabB2
    name="maze2.txt"
    f=open(name, "r")
    maze=Maze.Maze([line for line in f], 0)
    f.close()
    self.assertListEqual(LabB2.solve(None, maze), \
        [(0, 1), (0, 0)], \
        msg="The solution is wrong.")
  def test_maze3(self):
    enter()
    import Maze, LabB2
    name="maze3.txt"
    f=open(name, "r")
    maze=Maze.Maze([line for line in f], 0)
    f.close()
    self.assertListEqual(LabB2.solve(None, maze), \
        [(0, 1), (1, 1), (2, 1)], \
        msg="The solution is wrong.")
  def test_maze4(self):
    enter()
    import Maze, LabB2
    name="maze4.txt"
    f=open(name, "r")
    maze=Maze.Maze([line for line in f], 0)
    f.close()
    self.assertListEqual(LabB2.solve(None, maze), \
        [(2, 1), (1, 1), (0, 1)], \
        msg="The solution is wrong.")
  def test_maze5(self):
    enter()
    import Maze, LabB2
    name="maze5.txt"
    f=open(name, "r")
    maze=Maze.Maze([line for line in f], 0)
    f.close()
    self.assertListEqual(LabB2.solve(None, maze), \
        [(16, 22), (15, 22), (14, 22), (14, 23), (14, 24), (14, 25), \
         (14, 26), (14, 27), (14, 28), (14, 29), (13, 29), (12, 29), \
         (12, 28), (12, 27), (12, 26), (12, 25), (12, 24), (12, 23), \
         (12, 22), (12, 21), (12, 20), (12, 19), (12, 18), (12, 17), \
         (12, 16), (12, 15), (11, 15), (10, 15), (9, 15), (8, 15), (7, 15), \
         (6, 15), (5, 15), (4, 15), (3, 15), (2, 15), (1, 15), (1, 16), \
         (1, 17), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), \
         (1, 24), (2, 24), (3, 24), (4, 24), (4, 23), (4, 22), (5, 22), \
         (6, 22), (6, 23), (6, 24), (6, 25), (7, 25), (8, 25), (9, 25), \
         (9, 26), (9, 27), (9, 28), (9, 29), (8, 29), (7, 29), (6, 29), \
         (6, 30), (5, 30), (5, 31), (4, 31), (4, 32), (4, 33), (4, 34), \
         (4, 35), (3, 35), (2, 35), (1, 35), (1, 34), (1, 33), (1, 32), \
         (2, 32), (2, 31), (2, 30), (2, 29), (2, 28), (1, 28), (0, 28)], \
        msg="The solution is wrong.")
  def test_maze6(self):
    enter()
    import Maze, LabB2
    name="maze6.txt"
    f=open(name, "r")
    maze=Maze.Maze([line for line in f], 0)
    f.close()
    self.assertListEqual(LabB2.solve(None, maze), \
        [(11, 15), (12, 15), (12, 16), (12, 17), (12, 18), (12, 19), \
         (12, 20), (12, 21), (12, 22), (12, 23), (12, 24), (12, 25), \
         (12, 26), (12, 27), (12, 28), (12, 29), (13, 29), (14, 29), \
         (14, 28), (14, 27), (14, 26), (14, 25), (14, 24), (14, 23), \
         (14, 22), (14, 21), (14, 20), (14, 19), (15, 19), (15, 18), \
         (15, 17), (15, 16), (15, 15), (14, 15), (14, 14), (14, 13), \
         (13, 13), (12, 13), (11, 13), (11, 12), (10, 12), (9, 12), (8, 12), \
         (7, 12), (6, 12), (6, 11), (5, 11), (5, 10), (5, 9), (5, 8), (6, 8), \
         (7, 8), (8, 8), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (12, 8), \
         (12, 7), (12, 6), (12, 5), (11, 5), (10, 5), (10, 4), (10, 3), \
         (11, 3), (12, 3), (13, 3), (14, 3)], \
        msg="The solution is wrong.")
  def test_nomaze(self):
    enter()
    import Maze, LabB2
    name="nomaze.txt"
    f=open(name, "r")
    maze=Maze.Maze([line for line in f], 0)
    f.close()
    self.assertIsNone(LabB2.solve(None, maze), \
      msg="None was not returned for a maze with no solution.")
  def test_module_docstring(self):
    msg=("""
Your file must start with a docstring that explains the purpose and usage
of the file.
""")
    enter()
    import LabB2
    self.assertGreater(len(LabB2.__doc__),20, msg=msg)
    exit()
  def test_class_docstring(self):
    msg=("""
Your Stack class must start with a docstring that explains
what the class is used for.
""")
    enter()
    from LabB2 import Stack
    self.assertGreater(len(Stack.__doc__),20, msg=msg)
    exit()
  def test_func_docstring(self):
    enter()
    from LabB2 import Stack
    from types import FunctionType
    for name, f in Stack.__dict__.items():
      if type(f)==FunctionType:
        with self.subTest(function=name):
          self.assertGreater(len(f.__doc__),20, msg="This happens when this function does not have an adequate docstring.")
    exit()
  def test_solve_docstring(self):
    enter()
    from LabB2 import solve
    from types import FunctionType
    self.assertGreater(len(solve.__doc__),20, msg="This happens when this function does not have an adequate docstring.")
    exit()
  def test_timing(self):
    enter(120)
    import Maze, LabB2
    from time import monotonic
    name="nomaze.txt"
    f=open(name, "r")
    maze=Maze.Maze([line for line in f], 0.01)
    f.close()
    start=monotonic()
    LabB2.solve(None, maze)
    for threshold in range(5, 75, 5):
      with self.subTest(threshold=threshold):
        self.assertLess(monotonic()-start, threshold, msg="""
            The solution with loops is not fast enough, so you have not
            found the correct solution.""")
    exit()
  def test_illegal_names(self):
    import os, re
    dotend=re.compile(r'\.\s*(\\$|#)')
    dotsort=re.compile(r'\.\s*(index|sort(ed)?)\b')
    contsort=re.compile(r'^\s*(index|sort(ed)?)\b')
    for root, dirs, files in os.walk('.', followlinks=True):
      for name in files:
        ext=os.path.splitext(name)
        cont=False
        if ext[1]=='.py' and \
            (root!='.' or (ext[0]!='test' and ext[0]!='tests' and ext[0]!='Maze')):
          with open(os.path.join(root, name), 'r') as f:
            for n, line in enumerate(f,1):
              try:
                if cont:
                  self.assertIsNone(contsort.search(line))
                else:
                  self.assertIsNone(dotsort.search(line))
                cont=dotend.search(line)
              except:
                msg=("""
This tests that you do not cheat and use the sort built into Python.
The test can produce false positives. Avoid using "sort" or "sorted"
in your program to pass this test.

Illegal use of sort or sorted found on line {} of file {}
{}""".format(n, os.path.join(root, name), line))
                raise

if __name__=='__main__':
  unittest.main()
