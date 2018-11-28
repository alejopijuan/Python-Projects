#!/usr/bin/python3

import unittest

class LabB1Tests(unittest.TestCase):
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
    import LabB1
  def test_Plates_class(self):
    print("""
This means that your file does not define a class named "Plates."
""")
    from LabB1 import Plates
    self.assertEqual(type(Plates).__name__,'type')
  def test_init_function(self):
    print("""
This means that your Plates class does not define a constructor.
""")
    from LabB1 import Plates
    from types import FunctionType
    self.assertEqual(type(Plates.__init__),FunctionType)
  def test_findByPlate_function(self):
    print("""
This means that your Plates class does not define a findByPlate function.
""")
    from LabB1 import Plates
    from types import FunctionType
    self.assertEqual(type(Plates.findByPlate),FunctionType)
  def test_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabB1 import Plates
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
    try:
      sys.stdout=buf
      Plates('sampleplates.txt').findByPlate('Test')
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0)
  def test_run(self):
    print("""
Your program must contain the test code stated in the instructions. The output
must have output that exactly matches the assignment when it runs.
""")
    import subprocess
    result=subprocess.check_output(["python3","LabB1.py"], timeout=120, universal_newlines=True)
    self.assertMultiLineEqual(result,"""Plates file: sampleplates.txt
findByPlate('GPA1905')
Expected answer: ['Chevrolet', 'Corvette Coupe', '2008', 'pink', 'Sylvia Cheers']
Actual answer: ['Chevrolet', 'Corvette Coupe', '2008', 'pink', 'Sylvia Cheers']
""")
  def test_first(self):
    print("""
This happens when you do not correctly return the first item in the file.
""")
    from LabB1 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('GPA1905'), ['Chevrolet', \
        'Corvette Coupe', '2008', 'pink', 'Sylvia Cheers'])
  def test_last(self):
    print("""
This happens when you do not correctly return the last item in the file.
""")
    from LabB1 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('Y2C5NSM'), \
        ['Meaningless notes about car with plate Y2C5NSM'])
  def test_middle(self):
    print("""
This happens when you do not correctly return an arbitrary item in the list.
""")
    from LabB1 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('AY6D670'), \
        ['Meaningless notes about car with plate AY6D670'])
  def test_missing(self):
    print("""
This happens when you do not correctly return None when not found.
""")
    from LabB1 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('NOVELPLATE'), None)
  def test_sortedfirst(self):
    print("""
This happens when you do not correctly return the first item in the file
by sorted order.
""")
    from LabB1 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('0015V73'), \
        ['Meaningless notes about car with plate 0015V73'])
  def test_small(self):
    print("""
This happens when you do not correctly return None for something too small.
""")
    from LabB1 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('0015V72'), None)
  def test_sortedlast(self):
    print("""
This happens when you do not correctly return the last licence plate
in sorted order.
""")
    from LabB1 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('ZYD2067'),
        ['Meaningless notes about car with plate ZYD2067'])
  def test_big(self):
    print("""
This happens when you do not correctly return None for something too big.
""")
    from LabB1 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('ZYD2068'), None)
  def test_empty(self):
    print("""
This happens when you do not correctly handle a license with no other data.
""")
    from LabB1 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('MZZZ000'), [])
  def test_none(self):
    print("""
This happens when you do not correctly handle the license "None".
""")
    from LabB1 import Plates
    plates=Plates('sampleplates.txt')
    self.assertEqual(plates.findByPlate('None'), ['None'])
  def test_altfile(self):
    print("""
This happens when you do not correctly read the specified filename.
""")
    from LabB1 import Plates
    plates=Plates('other.txt')
    self.assertEqual(plates.findByPlate('8LW1A4F'), \
        ['Meaningless notes about car with plate 8LW1A4F'])
  def test_module_docstring(self):
    print("""
Your file must start with a docstring that explains the purpose and usage
of the file.
""")
    import LabB1
    self.assertGreater(len(LabB1.__doc__),20)
  def test_class_docstring(self):
    print("""
Your Plates class must start with a docstring that explains
what the class is used for.
""")
    from LabB1 import Plates
    self.assertGreater(len(Plates.__doc__),20)
  def test_init_docstring(self):
    print("""
Your constructor (__init__) must start with a docstring that explains
how the class is instantiated.
""")
    from LabB1 import Plates
    self.assertGreater(len(Plates.__init__.__doc__),20)
  def test_func_docstring(self):
    print("""
Your methods must start with a docstring that explains
what the method is used for.
""")
    from LabB1 import Plates
    self.assertGreater(len(Plates.findByPlate.__doc__),20)
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
  @classmethod
  def setUpClass(cls):
      from random import shuffle
      import sys
      from time import process_time
      from LabB1 import Plates
      plates=Plates('sampleplates.txt')
      targ=[]
      with open('targets.txt', 'r') as targets:
        for line in targets:
          targ.append(line.rstrip())
      start=process_time()
      for t in targ:
        plates.findByPlate(t)
      cls.time=process_time()-start
  def test_timing1(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(1, self.time);
  def test_timing2(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(2, self.time);
  def test_timing1(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(2, self.time);
  def test_timing3(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(3, self.time);
  def test_timing1(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(4, self.time);
  def test_timing1(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(4, self.time);
  def test_timing6(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(6, self.time);
  def test_timing8(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(8, self.time);
  def test_timing12(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(12, self.time);
  def test_timing16(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(16, self.time);
  def test_timing24(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(24, self.time);
  def test_timing32(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(32, self.time);
  def test_timing48(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(48, self.time);
  def test_timing64(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(64, self.time);
  def test_timing96(self):
    print("""
This tests that your program handles 50 queries per second.
""")
    self.assertGreater(96, self.time);

if __name__=='__main__':
  unittest.main()
