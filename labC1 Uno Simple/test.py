#!/usr/bin/python3

import unittest

class LabC1Tests(unittest.TestCase):
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
    import LabC1
  def test_best_move_function(self):
    print("""
Your program failed test 2.  
This means that your file does not define a function named "best_move."
If you defined a function, make sure it is named best_move.
Otherwise, you should review p. 20 in the textbook about how to define
functions.
""")
    from LabC1 import best_move
    from types import FunctionType
    self.assertEqual(type(best_move),FunctionType)
  def test_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabC1 import best_move
    from GameUno import GameUno, RED
    print("""
Most commonly your program fails this test if you use a print statement
in your best_move function. You must not print anything in this function.
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
    moves=[game.card(3,RED)]
    try:
      sys.stdout=buf
      best_move(game, moves)
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0)
  def test_run(self):
    print("""
Your program must contain the test code stated in the instructions. The output
must have output that exactly matches the assignment when it runs.
""")
    import subprocess
    result=subprocess.check_output(["python3","LabC1.py"], timeout=120, universal_newlines=True)
    self.assertMultiLineEqual(result,"""best_move(GameUno, [('Red', 7, 7), ('Red', 3, 3), ('Blue', 'Draw 2', 20)])
Expected answer: ('Blue', 'Draw 2', 20)
Actual answer: ('Blue', 'Draw 2', 20)
""")
  def test_best_move_first(self):
    print("""
This happens when you do not best_move the first entry in a list.
""")
    from LabC1 import best_move
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(WILD), game.card(4,BLUE), game.card(DRAW2,BLUE),\
           game.card(10,BLUE), game.card(REVERSE,BLUE), game.card(0,BLUE)]
    self.assertEqual(best_move(game, moves),moves[0])
  def test_best_move_multiples(self):
    print("""
This happens when you do not correctly return the first location of a value
that is in the list multiple times.
""")
    from LabC1 import best_move
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(2,BLUE), game.card(4,BLUE), game.card(DRAW2,BLUE),\
           game.card(10,BLUE), game.card(REVERSE,BLUE), game.card(0,BLUE)]
    self.assertEqual(best_move(game, moves),moves[2])
  def test_best_move_middle(self):
    print("""
This happens when you do not correctly best_move an entry in the middle of the list.
""")
    from LabC1 import best_move
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(2,BLUE), game.card(4,BLUE), game.card(DRAW2,BLUE),\
           game.card(10,BLUE), game.card(8,BLUE), game.card(0,BLUE)]
    self.assertEqual(best_move(game, moves),moves[2])
  def test_best_move_last(self):
    print("""
This happens when you do not correctly best_move the last item in the list.
""")
    from LabC1 import best_move
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(2,BLUE), game.card(4,BLUE), game.card(7,BLUE),\
           game.card(9,BLUE), game.card(3,BLUE), game.card(10,BLUE)]
    self.assertEqual(best_move(game, moves),moves[-1])
  def test_best_move_single(self):
    print("""
This happens when you do not correctly handle lists with only a single entry.
""")
    from LabC1 import best_move
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(10,BLUE)]
    self.assertEqual(best_move(game, moves),moves[0])
  def test_best_move_single_small(self):
    print("""
This happens when you do not correctly handle lists with only a single entry
and the value is small.
""")
    from LabC1 import best_move
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(0,BLUE)]
    self.assertEqual(best_move(game, moves),moves[0])
  def test_best_move_single_big(self):
    print("""
This happens when you do not correctly handle lists with only a single entry
and the value is not found.
""")
    from LabC1 import best_move
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[game.card(WILD4)]
    self.assertEqual(best_move(game, moves),moves[0])
  def test_best_move_empty(self):
    print("""
This happens when you do not correctly handle empty lists.
""")
    from LabC1 import best_move
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4
    game=GameUno()
    moves=[]
    self.assertEqual(best_move(game, moves),None)
  def test_module_docstring(self):
    print("""
Your file must start with a docstring that explains the purpose and usage
of the file.
""")
    import LabC1
    self.assertGreater(len(LabC1.__doc__),20)
  def test_func_docstring(self):
    print("""
Your best_move function must start with a docstring that explains what the function
does.
""")
    from LabC1 import best_move
    self.assertGreater(len(best_move.__doc__),20)
  def test_exception_safe(self):
    print("""
Your best_move function is not careful with its exception handling. It is
masking illegitimate errors generated by the Game utility() function.

If you have code that looks like:

try:
  some code
except:
  more code

you need to specify the excpetion you are intending to handle:

try:
  some code
except SpecificError:
  more code
""")
    class Nasty:
      def utility(game, move):
        raise IndexError("This should not be handled by the student.")
    from LabC1 import best_move
    game=Nasty()
    moves=[1,2,3]
    with self.assertRaises(IndexError):
      best_move(game, moves)

if __name__=='__main__':
  unittest.main()
