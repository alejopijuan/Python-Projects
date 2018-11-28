#!/usr/bin/python3

import unittest

class LabC2Tests(unittest.TestCase):
  def test_importable(self):
    print("""
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
    import LabC2
  def test_sort_hand_function(self):
    print("""
Your program failed test 2.  
This means that your file does not define a function named "sort_hand."
If you defined a function, make sure it is named sort_hand.
Otherwise, you should review p. 20 in the textbook about how to define
functions.
""")
    from LabC2 import sort_hand
    from types import FunctionType
    self.assertEqual(type(sort_hand),FunctionType)
  def test_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabC2 import sort_hand
    from GameUno import GameUno, RED, BLUE, WILD4
    print("""
Most commonly your program fails this test if you use a print statement
in your sort_hand function. You must not print anything in this function.
Instead, you should return the location so that the test code can access it.

Wrong:

def add(a, b):
    ""\" Add a and b.""\"
    print(a+b)

Right:

def add(a, b):
    ""\" Return the sum of a and b.""\"
    return a+b
""")
    oldout = sys.stdout
    buf=StringIO()
    game=GameUno()
    moves=[game.card(3,RED), game.card(7,BLUE), game.card(WILD4)]
    try:
      sys.stdout=buf
      sort_hand( moves)
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0)
  def test_run(self):
    print("""
Your program must contain the test code stated in the instructions. The output
must have output that exactly matches the assignment when it runs.
""")
    import subprocess
    result=subprocess.check_output(["python3","LabC2.py"], timeout=120, universal_newlines=True)
    self.assertMultiLineEqual(result,"""sort_hand([('Red', 7, 7), ('Red', 3, 3), ('Blue', 'Draw 2', 20)])
Expected answer: [('Blue', 'Draw 2', 20), ('Red', 3, 3), ('Red', 7, 7)]
Actual answer: [('Blue', 'Draw 2', 20), ('Red', 3, 3), ('Red', 7, 7)]
""")
  def test_sort_hand_monocolor(self):
    print("""
This happens when you do not correctly return the first location of a value
that is in the list multiple times.
""")
    from LabC2 import sort_hand
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(2,BLUE), game.card(4,BLUE), game.card(DRAW2,BLUE),\
           game.card(10,BLUE), game.card(REVERSE,BLUE), game.card(0,BLUE)]
    self.assertEqual(sort_hand(moves), None)
    self.assertEqual(moves, [game.card(0,BLUE), game.card(2,BLUE), \
        game.card(4,BLUE), game.card(10,BLUE), game.card(DRAW2,BLUE), \
        game.card(REVERSE,BLUE)])
  def test_sort_hand_mono2(self):
    print("""
This happens when you do not correctly sort_hand an entry in the middle of the list.
""")
    from LabC2 import sort_hand
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(2,RED), game.card(2,BLUE), game.card(2,YELLOW),\
           game.card(2,GREEN)]
    self.assertEqual(sort_hand(moves), None)
    self.assertEqual(moves, [game.card(2,BLUE), game.card(2,GREEN), \
        game.card(2,RED), game.card(2,YELLOW)])
  def test_sort_mono20(self):
    print("""
This happens when you do not correctly sort_hand the last item in the list.
""")
    from LabC2 import sort_hand
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(DRAW2,YELLOW), \
           game.card(SKIP,RED), \
           game.card(SKIP,YELLOW), \
           game.card(REVERSE,GREEN), \
           game.card(SKIP,BLUE), \
           game.card(DRAW2,BLUE), \
           game.card(REVERSE,YELLOW), \
           game.card(SKIP,GREEN), \
           game.card(REVERSE,RED), \
           game.card(REVERSE,BLUE), \
           game.card(DRAW2,GREEN), \
           game.card(DRAW2,RED)]
    self.assertEqual(sort_hand(moves), None)
    self.assertEqual(moves, [game.card(DRAW2,BLUE), \
           game.card(REVERSE,BLUE), \
           game.card(SKIP,BLUE), \
           game.card(DRAW2,GREEN), \
           game.card(REVERSE,GREEN), \
           game.card(SKIP,GREEN), \
           game.card(DRAW2,RED), \
           game.card(REVERSE,RED), \
           game.card(SKIP,RED), \
           game.card(DRAW2,YELLOW), \
           game.card(REVERSE,YELLOW), \
           game.card(SKIP,YELLOW)])
  def test_sort_mixed(self):
    print("""
This happens when you do not correctly sort_hand the last item in the list.
""")
    from LabC2 import sort_hand
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[ \
           game.card(REVERSE,BLUE), \
           game.card(0,BLUE),
           game.card(WILD4,WILD), \
           game.card(4,BLUE), \
           game.card(WILD,WILD), \
           game.card(DRAW2,BLUE), \
           game.card(REVERSE,GREEN), \
           game.card(2,BLUE), \
           game.card(DRAW2,BLUE), \
           game.card(DRAW2,GREEN), \
           game.card(REVERSE,RED), \
           game.card(SKIP,BLUE), \
           game.card(SKIP,YELLOW), \
           game.card(2,GREEN), \
           game.card(DRAW2,YELLOW), \
           game.card(SKIP,GREEN), \
           game.card(2,RED), \
           game.card(REVERSE,YELLOW), \
           game.card(DRAW2,RED), \
           game.card(REVERSE,BLUE), \
           game.card(10,BLUE), \
           game.card(SKIP,RED), \
           game.card(2,YELLOW), \
           game.card(2,BLUE)]
    self.assertEqual(sort_hand(moves), None)
    self.assertEqual(moves, [ \
           game.card(WILD4,WILD), \
           game.card(WILD,WILD), \
           game.card(0,BLUE), \
           game.card(2,BLUE), \
           game.card(2,BLUE), \
           game.card(4,BLUE), \
           game.card(10,BLUE), \
           game.card(DRAW2,BLUE), \
           game.card(DRAW2,BLUE), \
           game.card(REVERSE,BLUE), \
           game.card(REVERSE,BLUE), \
           game.card(SKIP,BLUE), \
           game.card(2,GREEN), \
           game.card(DRAW2,GREEN), \
           game.card(REVERSE,GREEN), \
           game.card(SKIP,GREEN), \
           game.card(2,RED), \
           game.card(DRAW2,RED), \
           game.card(REVERSE,RED), \
           game.card(SKIP,RED), \
           game.card(2,YELLOW), \
           game.card(DRAW2,YELLOW), \
           game.card(REVERSE,YELLOW), \
           game.card(SKIP,YELLOW)])
  def test_sort_hand_single(self):
    print("""
This happens when you do not correctly handle lists with only a single entry.
""")
    from LabC2 import sort_hand
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(10,BLUE)]
    self.assertEqual(sort_hand(moves),None)
    self.assertEqual(moves, [game.card(10,BLUE)])
  def test_sort_hand_empty(self):
    print("""
This happens when you do not correctly handle empty lists.
""")
    from LabC2 import sort_hand
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[]
    self.assertEqual(sort_hand( moves),None)
    self.assertEqual(len( moves),0)
  def test_module_docstring(self):
    print("""
Your file must start with a docstring that explains the purpose and usage
of the file.
""")
    import LabC2
    self.assertGreater(len(LabC2.__doc__),20)
  def test_func_docstring(self):
    print("""
Your sort_hand function must start with a docstring that explains what the function
does.
""")
    from LabC2 import sort_hand
    self.assertGreater(len(sort_hand.__doc__),20)
  def test_illegal_names(self):
    import os, re
    dotend=re.compile(r'\.\s*(\\$|#)')
    dotsort=re.compile(r'\.\s*sort(ed)?\b')
    contsort=re.compile(r'^\s*sort(ed)?\b')
    for root, dirs, files in os.walk('.', followlinks=True):
      for name in files:
        ext=os.path.splitext(name)
        cont=False
        if ext[1]=='.py' and \
            (root!='.' or (ext[0]!='test' and ext[0]!='tests')):
          with open(os.path.join(root, name), 'r') as f:
            for n, line in enumerate(f,1):
              try:
                if cont:
                  self.assertEqual(contsort.search(line),None)
                else:
                  self.assertEqual(dotsort.search(line),None)
                cont=dotend.search(line)
              except:
                print("""
This tests that you do not cheat and use the sort built into Python.
The test can produce false positives. Avoid using "sort" or "sorted"
in your program to pass this test.

Illegal use of sort or sorted found on line {} of file {}
{}""".format(n, os.path.join(root, name), line))
                raise

if __name__=='__main__':
  unittest.main()
