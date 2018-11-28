#!/usr/bin/python3

import unittest

class LabD3Tests(unittest.TestCase):
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
    import LabD3
  def test_sort_list_function(self):
    print("""
Your program failed test 2.  
This means that your file does not define a function named "sort_list."
If you defined a function, make sure it is named sort_list.
Otherwise, you should review p. 20 in the textbook about how to define
functions.
""")
    from LabD3 import sort_list
    from types import FunctionType
    self.assertEqual(type(sort_list),FunctionType)
  def test_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabD3 import sort_list
    print("""
Most commonly your program fails this test if you use a print statement
in your sort_list function. You must not print anything in this function.
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
    haystack=[3,3.1415926535,3.7,4,4,4.9,5,6]
    try:
      sys.stdout=buf
      sort_list(haystack)
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0)
  def test_run(self):
    print("""
Your program must contain the test code stated in the instructions. The output
must have output that exactly matches the assignment when it runs.
""")
    import subprocess
    result=subprocess.check_output(["python3","LabD3.py"], timeout=120, universal_newlines=True)
    self.assertMultiLineEqual(result,"""sort_list(['the', 'cat', 'in', 'the', 'hat', 'is', 'back'])
Expected answer: ['back', 'cat', 'hat', 'in', 'is', 'the', 'the']
Actual answer: ['back', 'cat', 'hat', 'in', 'is', 'the', 'the']
""")
  def test_sort_sorted(self):
    print("""
This happens when you do correctly sort a list of numbers.
""")
    from LabD3 import sort_list
    haystack=[3,3.1415926535,3.7,4,4.9,5,6]
    self.assertEqual(sort_list(haystack),None);
    self.assertEqual(haystack,[3,3.1415926535,3.7,4,4.9,5,6])
  def test_sort_list_multiples(self):
    print("""
This happens when you do not correctly sort a list with duplicates.
""")
    from LabD3 import sort_list
    haystack=[46, 10, 24, 36, 24, 1, 29, 23, 41]
    self.assertEqual(sort_list(haystack),None);
    self.assertEqual(haystack,[1, 10, 23, 24, 24, 29, 36, 41, 46])
  def test_sort_numbers(self):
    print("""
This happens when you do not correctly sort a list of numbers.
""")
    from LabD3 import sort_list
    haystack=[46, 10, 24, 36, 1, 29, 23, 41]
    self.assertEqual(sort_list(haystack),None)
    self.assertEqual(haystack,[1, 10, 23, 24, 29, 36, 41, 46])
  def test_sort_text(self):
    print("""
This happens when you do not correctly sort strings.
""")
    from LabD3 import sort_list
    haystack=["this", "is", "a", "test"]
    self.assertEqual(sort_list(haystack),None)
    self.assertEqual(haystack,["a", "is", "test", "this"])
  def test_sort_list_single(self):
    print("""
This happens when you do not correctly handle lists with only a single entry.
""")
    from LabD3 import sort_list
    haystack=[3]
    self.assertEqual(sort_list(haystack),None)
    self.assertEqual(haystack,[3])
  def test_sort_list_strings(self):
    print("""
This happens when you do not correctly handle sorted lists of strings.
""")
    from LabD3 import sort_list
    haystack=["A", "cat", "in", "the", "zoo"]
    self.assertEqual(sort_list(haystack),None)
    self.assertEqual(haystack, ["A", "cat", "in", "the", "zoo"])
  def test_sort_list_empty(self):
    print("""
This happens when you do not correctly handle empty lists.
""")
    from LabD3 import sort_list
    haystack=[]
    self.assertEqual(sort_list(haystack),None)
    self.assertEqual(haystack,[])
  def test_module_docstring(self):
    print("""
Your file must start with a docstring that explains the purpose and usage
of the file.
""")
    import LabD3
    self.assertGreater(len(LabD3.__doc__),20)
  def test_func_docstring(self):
    print("""
Your sort_list function must start with a docstring that explains what the function
does.
""")
    from LabD3 import sort_list
    self.assertGreater(len(sort_list.__doc__),20)
  def timing_ratio(self):
    """Get the timing ratio, used in multiple tests."""
    return [self.timeM/self.timeT, self.timeM0/self.timeT0]
  @classmethod
  def setUpClass(cls):
      from random import shuffle
      import sys
      from time import process_time
      from LabD3 import sort_list
      sys.setrecursionlimit(11000)
      cls.timeT=0;
      for i in range(10):
        haystack=list(range(1024))
        shuffle(haystack)
        start=process_time()
        sort_list(haystack)
        cls.timeT+=process_time()-start
      cls.timeM=0;
      for i in range(10):
        haystack=list(range(1024*1024))
        shuffle(haystack)
        start=process_time()
        sort_list(haystack)
        cls.timeM+=process_time()-start
      cls.timeT0=0;
      haystack=[0]*100
      for i in range(10):
        start=process_time()
        sort_list(haystack)
        cls.timeT0+=process_time()-start
      cls.timeM0=0;
      haystack=[0]*(100*100)
      for i in range(10):
        start=process_time()
        sort_list(haystack)
        cls.timeM0+=process_time()-start
  def test_timing3(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(3*2048, self.timing_ratio()[0]);
  def test_timing4(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(4*2048, self.timing_ratio()[0]);
  def test_timing6(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(6*2048, self.timing_ratio()[0]);
  def test_timing8(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(8*2048, self.timing_ratio()[0]);
  def test_timing12(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(12*2048, self.timing_ratio()[0]);
  def test_timing16(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(16*2048, self.timing_ratio()[0]);
  def test_timing24(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(24*2048, self.timing_ratio()[0]);
  def test_timing32(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(32*2048, self.timing_ratio()[0]);
  def test_timing48(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(48*2048, self.timing_ratio()[0]);
  def test_timing64(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(64*2048, self.timing_ratio()[0]);
  def test_timing96(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(96*2048, self.timing_ratio()[0]);
  def test_timing128(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(128*2048, self.timing_ratio()[0]);
  def test_timing192(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(192*2048, self.timing_ratio()[0]);
  def test_timing256(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(256*2048, self.timing_ratio()[0]);
  def test_timing384(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(384*2048, self.timing_ratio()[0]);
  def test_timing512(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(512*2048, self.timing_ratio()[0]);
  def test_timing768(self):
    print("""
This tests that your program is O(n log n) (quicksort with random data) and
not O(n^2) (insertion sort).
""")
    self.assertGreater(768*2048, self.timing_ratio()[0]);
  def test_timing_zero(self):
    print("""
This tests that your program is O(n^2) (quicksort worst-case) and
not O(n log n) (merge sort).
""")
    self.assertLess(65, self.timing_ratio()[1]);
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
