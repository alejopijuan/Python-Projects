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

class LabD6Tests(unittest.TestCase):
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
    enter()
    import LabD6
    exit()
  def test_Plates_class(self):
    print("""
This means that your file does not define a class named "Plates."
""")
    enter()
    from LabD6 import Plates
    self.assertEqual(type(Plates).__name__,'type')
    exit()
  def test_init_function(self):
    print("""
This means that your Plates class does not define a constructor.
""")
    enter()
    from LabD6 import Plates
    from types import FunctionType
    self.assertEqual(type(Plates.__init__),FunctionType)
    exit()
  def test_findByPlate_function(self):
    print("""
This means that your Plates class does not define a findByPlate function.
""")
    enter()
    from LabD6 import Plates
    from types import FunctionType
    self.assertEqual(type(Plates.findByPlate),FunctionType)
    exit()
  def test_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabD6 import Plates
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
    enter()
    oldout = sys.stdout
    buf=StringIO()
    try:
      sys.stdout=buf
      Plates('sampleplates.txt').findByPlate('Test')
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0)
    exit()
  def test_run(self):
    print("""
Your program must contain the test code stated in the instructions. The output
must have output that exactly matches the assignment when it runs.
""")
    enter()
    import subprocess
    result=subprocess.check_output(["python3","LabD6.py"], timeout=120, universal_newlines=True)
    self.assertMultiLineEqual(result,"""Plates file: sampleplates.txt
findByPlate('GPA1905')
Expected answer: ['Chevrolet', 'Corvette Coupe', '2008', 'pink', 'Sylvia Cheers']
Actual answer: ['Chevrolet', 'Corvette Coupe', '2008', 'pink', 'Sylvia Cheers']
""")
    exit()
  def test_first(self):
    print("""
This happens when you do not correctly return the first item in the file.
""")
    enter()
    from LabD6 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('GPA1905'), ['Chevrolet', \
        'Corvette Coupe', '2008', 'pink', 'Sylvia Cheers'])
    exit()
  def test_last(self):
    print("""
This happens when you do not correctly return the last item in the file.
""")
    enter()
    from LabD6 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('Y2C5NSM'), \
        ['Meaningless notes about car with plate Y2C5NSM'])
    exit()
  def test_middle(self):
    print("""
This happens when you do not correctly return an arbitrary item in the list.
""")
    enter()
    from LabD6 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('AY6D670'), \
        ['Meaningless notes about car with plate AY6D670'])
    exit()
  def test_missing(self):
    print("""
This happens when you do not correctly return None when not found.
""")
    enter()
    from LabD6 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('NOVELPLATE'), None)
    exit()
  def test_sortedfirst(self):
    print("""
This happens when you do not correctly return the first item in the file
by sorted order.
""")
    enter()
    from LabD6 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('0015V73'), \
        ['Meaningless notes about car with plate 0015V73'])
    exit()
  def test_small(self):
    print("""
This happens when you do not correctly return None for something too small.
""")
    enter()
    from LabD6 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('0015V72'), None)
    exit()
  def test_sortedlast(self):
    print("""
This happens when you do not correctly return the last licence plate
in sorted order.
""")
    enter()
    from LabD6 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('ZYD2067'),
        ['Meaningless notes about car with plate ZYD2067'])
    exit()
  def test_big(self):
    print("""
This happens when you do not correctly return None for something too big.
""")
    enter()
    from LabD6 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('ZYD2068'), None)
    exit()
  def test_empty(self):
    print("""
This happens when you do not correctly handle a license with no other data.
""")
    enter()
    from LabD6 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('MZZZ000'), [])
    exit()
  def test_none(self):
    print("""
This happens when you do not correctly handle the license "None".
""")
    enter()
    from LabD6 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('None'), ['None'])
    exit()
  def test_altfile(self):
    print("""
This happens when you do not correctly read the specified filename.
""")
    enter()
    from LabD6 import Plates
    plates=Plates('other.txt')
    self.assertEqual(plates.findByPlate('8LW1A4F'), \
        ['Meaningless notes about car with plate 8LW1A4F'])
    exit()
  def test_module_docstring(self):
    print("""
Your file must start with a docstring that explains the purpose and usage
of the file.
""")
    enter()
    import LabD6
    self.assertGreater(len(LabD6.__doc__),20)
    exit()
  def test_class_docstring(self):
    print("""
Your Plates class must start with a docstring that explains
what the class is used for.
""")
    enter()
    from LabD6 import Plates
    self.assertGreater(len(Plates.__doc__),20)
    exit()
  def test_init_docstring(self):
    print("""
Your constructor (__init__) must start with a docstring that explains
how the class is instantiated.
""")
    enter()
    from LabD6 import Plates
    self.assertGreater(len(Plates.__init__.__doc__),20)
    exit()
  def test_func_docstring(self):
    print("""
Your methods must start with a docstring that explains
what the method is used for.
""")
    enter()
    from LabD6 import Plates
    self.assertGreater(len(Plates.findByPlate.__doc__),20)
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
    exit()
  def test_timing(self):
    enter(1200)
    from random import shuffle
    import sys
    from time import process_time
    from LabD6 import Plates
    plates=Plates('huge.txt')
    targ=[]
    with open('hugetargets.txt', 'r') as targets:
      for line in targets:
        targ.append(line.rstrip())
    start=process_time()
    for t in targ:
      plates.findByPlate(t)
    time=(process_time()-start)*100
    print(time)
    for i in range(1,100):
      with self.subTest(time=i):
        self.assertLessEqual(time,i, msg="This tests the time required to process 10000 queries.")
    exit()

if __name__=='__main__':
  unittest.main()
