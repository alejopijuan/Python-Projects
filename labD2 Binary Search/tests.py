#!/usr/bin/python3

import unittest

class LabD2Tests(unittest.TestCase):
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
    import LabD2
  def test_hunt_function(self):
    print("""
Your program failed test 2.  
This means that your file does not define a function named "hunt."
If you defined a function, make sure it is named hunt.
Otherwise, you should review p. 20 in the textbook about how to define
functions.
""")
    from LabD2 import hunt
    from types import FunctionType
    self.assertEqual(type(hunt),FunctionType)
  def test_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabD2 import hunt
    print("""
Most commonly your program fails this test if you use a print statement
in your hunt function. You must not print anything in this function.
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
    needle=3
    try:
      sys.stdout=buf
      hunt(haystack, needle)
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0)
  def test_run(self):
    print("""
Your program must contain the test code stated in the instructions. The output
must have output that exactly matches the assignment when it runs.
""")
    import subprocess
    result=subprocess.check_output(["python3","LabD2.py"], timeout=120, universal_newlines=True)
    self.assertMultiLineEqual(result,"""Test: hunt([1,2,3], 2)
Expected answer: 1
Actual answer: 1
""")
  def test_hunt_first(self):
    print("""
This happens when you do not hunt the first entry in a list.
""")
    from LabD2 import hunt
    haystack=[3,3.1415926535,3.7,4,4,4.9,5,6]
    needle=3
    self.assertEqual(hunt(haystack, needle),0)
  def test_hunt_multiples(self):
    print("""
This happens when you do not correctly return the first location of a value
that is in the list multiple times.
""")
    from LabD2 import hunt
    haystack=[3,3.1415926535,3.7,4,4,4.9,5,6]
    needle=4
    self.assertIn(hunt(haystack, needle),[3,4])
  def test_hunt_middle(self):
    print("""
This happens when you do not correctly hunt an entry in the middle of the list.
""")
    from LabD2 import hunt
    haystack=[3,3.1415926535,3.7,4,4,4.9,5,6]
    needle=3.7
    self.assertEqual(hunt(haystack, needle),2)
  def test_hunt_last(self):
    print("""
This happens when you do not correctly hunt the last item in the list.
""")
    from LabD2 import hunt
    haystack=[3,3.1415926535,3.7,4,4,4.9,5,6]
    needle=6
    self.assertEqual(hunt(haystack, needle),7)
  def test_hunt_not_big(self):
    print("""
This heppens when you do not handle the case where the needle is bigger than
anything in the list.
""")
    from LabD2 import hunt
    haystack=[3,3.1415926535,3.7,4,4,4.9,5,6]
    needle=7
    self.assertEqual(hunt(haystack, needle),None)
  def test_hunt_small(self):
    print("""
This happens when the needle is smaller than anything in the haystack.
""")
    from LabD2 import hunt
    haystack=[3,3.1415926535,3.7,4,4,4.9,5,6]
    needle=0
    self.assertEqual(hunt(haystack, needle),None)
  def test_hunt_not_found(self):
    print("""
This heppens when you do not return the special keyword None when the value
is not found in the list.

Good:
    return None

Bad:
    return "None"
""")
    from LabD2 import hunt
    haystack=[3,3.1415926535,3.7,4,4,4.9,5,6]
    needle=3.5
    self.assertEqual(hunt(haystack, needle),None)
  def test_center(self):
    print("""
This tests correct handling of hunting for the value in the exact center.
""")
    from LabD2 import hunt
    haystack=[3,3.1415926535,3.7,4,4.9,5,6]
    needle=4
    self.assertEqual(hunt(haystack, needle),3)
  def test_hunt_single(self):
    print("""
This happens when you do not correctly handle lists with only a single entry.
""")
    from LabD2 import hunt
    haystack=[3]
    needle=3
    self.assertEqual(hunt(haystack, needle),0)
  def test_hunt_single_small(self):
    print("""
This happens when you do not correctly handle lists with only a single entry
and the value is small.
""")
    from LabD2 import hunt
    haystack=[3]
    needle=1
    self.assertEqual(hunt(haystack, needle),None)
  def test_hunt_single_big(self):
    print("""
This happens when you do not correctly handle lists with only a single entry
and the value is not found.
""")
    from LabD2 import hunt
    haystack=[3]
    needle=4
    self.assertEqual(hunt(haystack, needle),None)
  def test_hunt_strings(self):
    print("""
This happens when you do not correctly handle lists of strings.
""")
    from LabD2 import hunt
    haystack=["A", "cat", "in", "the", "zoo"]
    needle="cat"
    self.assertEqual(hunt(haystack, needle),1)
  def test_hunt_empty(self):
    print("""
This happens when you do not correctly handle empty lists.
""")
    from LabD2 import hunt
    haystack=[]
    needle=3
    self.assertEqual(hunt(haystack, needle),None)
  def test_module_docstring(self):
    print("""
Your file must start with a docstring that explains the purpose and usage
of the file.
""")
    import LabD2
    self.assertGreater(len(LabD2.__doc__),20)
  def test_func_docstring(self):
    print("""
Your hunt function must start with a docstring that explains what the function
does.
""")
    from LabD2 import hunt
    self.assertGreater(len(hunt.__doc__),20)
  def timing_ratio(self):
    """Get the timing ratio, used in multiple tests."""
    try:
      return self.timeM/self.timeT
    except:
      from time import process_time
      from LabD2 import hunt
      haystack=range(1024)
      start=process_time()
      for i in range(10):
        j=hunt(haystack,1023-i*3)
      self.timeT=process_time()-start
      haystack=range(1024*1024)
      start=process_time()
      for i in range(10):
        j=hunt(haystack,(1024*1024)-1-i*3)
      self.timeM=process_time()-start
      return self.timeM/self.timeT
  def test_timing3(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(3, self.timing_ratio());
  def test_timing4(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(4, self.timing_ratio());
  def test_timing6(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(6, self.timing_ratio());
  def test_timing8(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(8, self.timing_ratio());
  def test_timing12(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(12, self.timing_ratio());
  def test_timing16(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(16, self.timing_ratio());
  def test_timing24(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(24, self.timing_ratio());
  def test_timing32(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(32, self.timing_ratio());
  def test_timing48(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(48, self.timing_ratio());
  def test_timing64(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(64, self.timing_ratio());
  def test_timing96(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(96, self.timing_ratio());
  def test_timing128(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(128, self.timing_ratio());
  def test_timing192(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(192, self.timing_ratio());
  def test_timing256(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(256, self.timing_ratio());
  def test_timing384(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(384, self.timing_ratio());
  def test_timing512(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(512, self.timing_ratio());
  def test_timing768(self):
    print("""
This tests that your program is O(log n) (binary search) and not O(n)
(linear search).
""")
    self.assertGreater(768, self.timing_ratio());

if __name__=='__main__':
  unittest.main()
