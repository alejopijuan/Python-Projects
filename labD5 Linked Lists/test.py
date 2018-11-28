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

class LabD5Tests(unittest.TestCase):
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
    import LabD5
    exit()
  def test_LinkedList_class(self):
    enter()
    from LabD5 import LinkedList
    self.assertEqual(type(LinkedList).__name__,'type', msg='This means that your file does not define a class named "LinkedList."')
    exit()
  def test_init_function(self):
    msg=("""
This means that your LinkedList class does not define a constructor.
""")
    enter()
    from LabD5 import LinkedList
    from types import FunctionType
    self.assertEqual(type(LinkedList.__init__),FunctionType, msg=msg)
    exit()
  def test_len_function(self):
    msg=("""
This means that your LinkedList class does not define a __len__ method.
""")
    enter()
    from LabD5 import LinkedList
    from types import FunctionType
    self.assertEqual(type(LinkedList.__len__),FunctionType, msg=msg)
    exit()
  def test_getitem_function(self):
    msg=("""
This means that your LinkedList class does not define a __getitem__ method.
""")
    enter()
    from LabD5 import LinkedList
    from types import FunctionType
    self.assertEqual(type(LinkedList.__getitem__),FunctionType, msg=msg)
    exit()
  def test_append_function(self):
    msg=("""
This means that your LinkedList class does not define an append function.
""")
    enter()
    from LabD5 import LinkedList
    from types import FunctionType
    self.assertEqual(type(LinkedList.append),FunctionType, msg=msg)
    exit()
  def test_insert_function(self):
    msg=("""
This means that your LinkedList class does not define an insert function.
""")
    enter()
    from LabD5 import LinkedList
    from types import FunctionType
    self.assertEqual(type(LinkedList.insert),FunctionType, msg=msg)
    exit()
  def test_append_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabD5 import LinkedList
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
    l=LinkedList()
    buf=StringIO()
    try:
      sys.stdout=buf
      l.append(3.0)
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0, msg=msg)
    exit()
  def test_init_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabD5 import LinkedList
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
    buf=StringIO()
    try:
      sys.stdout=buf
      l=LinkedList()
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0, msg=msg)
    exit()
  def test_len_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabD5 import LinkedList
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
    l=LinkedList()
    buf=StringIO()
    try:
      sys.stdout=buf
      len(l)
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0, msg=msg)
    exit()
  def test_getitem_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabD5 import LinkedList
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
    l=LinkedList()
    l.append(3.14)
    buf=StringIO()
    try:
      sys.stdout=buf
      l[0]
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0, msg=msg)
    exit()
  def test_len3_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabD5 import LinkedList
    msg=("""
Most commonly your program fails this test if you use a print statement
in your __len__ function. You must not print anything in class methods.
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
    l=LinkedList()
    l.append(3.14)
    l.append(159.26)
    l.append(342)
    buf=StringIO()
    try:
      sys.stdout=buf
      len(l)
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0, msg=msg)
    exit()
  def test_insert_no_output(self):
    # Based on code from user1200039 http://stackoverflow.com/questions/5136611/capture-stdout-from-a-script-in-python
    import sys
    from io import StringIO
    from LabD5 import LinkedList
    msg=("""
Most commonly your program fails this test if you use a print statement
in your insert method. You must not print anything in class methods.
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
    l=LinkedList()
    buf=StringIO()
    try:
      sys.stdout=buf
      l.insert(0,3.0)
      l.insert(0,4.0)
      l.insert(1,4.2)
      l.insert(3,2.2)
    finally:
      sys.stdout=oldout
    self.assertEqual(len(buf.getvalue()),0, msg=msg)
    exit()
  def test_run(self):
    msg=("""
Your program must contain the test code stated in the instructions. The output
must have output that exactly matches the assignment when it runs.
""")
    enter()
    import subprocess
    result=subprocess.check_output(["python3","LabD5.py"], timeout=120, universal_newlines=True)
    self.assertMultiLineEqual(result, \
"""len(sample)
  Expected: 0
  Actual: 0
sample.insert(0, 0.7879183363699951)
sample.insert(1, 0.8249938154876826)
sample.insert(0, 0.41979511664048086)
sample.insert(2, 0.38311278079429256)
sample.insert(0, 0.02615745603398889)
sample.insert(0, 0.9096667329241896)
sample.insert(5, 0.5775226870686715)
sample.insert(6, 0.08178455962969056)
sample.insert(0, 0.8794845298926424)
sample.insert(7, 0.7065827932270193)
len(sample)
  Expected: 10
  Actual: 10
sample[6]
  Expect: 0.5775226870686715
  Actual: 0.5775226870686715
sample[8]
  Expect: 0.08178455962969056
  Actual: 0.08178455962969056
sample[0]
  Expect: 0.8794845298926424
  Actual: 0.8794845298926424
""", msg=msg)
    enter()
    exit()
  def test_first(self):
    msg=("""
This happens when you do not correctly return the first item in the list.
""")
    enter()
    from LabD5 import LinkedList
    l=LinkedList()
    l.append(3.14)
    l.append(159.26)
    l.append(342)
    self.assertEqual(l[0], 3.14, msg=msg)
    exit()
  def test_last(self):
    msg=("""
This happens when you do not correctly return the last item in the list.
""")
    enter()
    from LabD5 import LinkedList
    l=LinkedList()
    l.append(3.14)
    l.append(159.26)
    l.append(342)
    self.assertEqual(l[2], 342, msg=msg)
    exit()
  def test_middle(self):
    msg=("""
This happens when you do not correctly return an arbitrary item in the list.
""")
    enter()
    from LabD5 import LinkedList
    l=LinkedList()
    l.append(3.14)
    l.append(159.26)
    l.append(342)
    self.assertEqual(l[1], 159.26, msg=msg)
    exit()
  def test_missing(self):
    msg=("""
This happens when you do not correctly raise on IndexError for invalid items.
""")
    enter()
    from LabD5 import LinkedList
    l=LinkedList()
    l.append(3.14)
    l.append(159.26)
    l.append(342)
    with self.assertRaises(IndexError, msg=msg):
      l[3]
    exit()
  def test_invalid_insert(self):
    msg=("""
This happens when you do not correctly raise on IndexError for invalid insert.
""")
    enter()
    from LabD5 import LinkedList
    l=LinkedList()
    l.append(3.14)
    l.append(159.26)
    l.append(342)
    with self.subTest(idx="end+1"):
      with self.assertRaises(IndexError, msg=msg):
        l.insert(4,3)
    with self.subTest(idx=-4):
      with self.assertRaises(IndexError, msg=msg):
        l.insert(-4,3)
    exit()
  def test_missing_neg(self):
    msg=("""
This happens when you do not correctly raise on IndexError for invalid items.
""")
    enter()
    from LabD5 import LinkedList
    l=LinkedList()
    l.append(3.14)
    l.append(159.26)
    l.append(342)
    with self.assertRaises(IndexError, msg=msg):
      l[-10]
    exit()
  def seek(self, data, item):
    if data is item:
      return []
    try:
      for k,v in data.__dict__.items():
        if v is not data:
          trail=self.seek(v, item)
          if trail is not None:
            trail.insert(0,k)
            return trail
    except:
      pass
    try:
      idx=0
      for i in data:
        if i is not data:
          trail=self.seek(i, item)
          if trail is not None:
            trail.insert(0,idx)
            return trail
          idx+=1
    except:
      pass
    return None
  def structure(self, a, b):
    pre=[]
    link=[]
    post=[]
    idx=0
    try:
      while a[idx]==b[idx]:
        pre.append(a[idx])
        idx+=1
    except:
      pass
    a=a[idx:]
    b=b[idx:]
    idx=-1
    try:
      while a[idx]==b[idx]:
        post.insert(0,a[idx])
        idx-=1
    except:
      pass
    a=a[0:(len(a)+idx+1)]
    b=b[0:(len(b)+idx+1)]
    return (pre, post, a, b)
  def test_structure(self):
    enter()
    from LabD5 import LinkedList
    import numpy
    l=LinkedList()
    targets=("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K")
    for t in targets:
      l.append(t)
    print(l.__dict__.items())
    for t in range(len(targets)):
      with self.subTest(step="seek", idx=t):
        path=self.seek(l, targets[t])
        print(path)
        if t==0:
          path0=path
        elif t==1:
          struct1=self.structure(path0, path)
          self.assertEqual(len(struct1[2]),0, msg="""
              You do not seem to have a proper linked list, because the link
              to the first node is not consistent.""")
          self.assertGreater(len(struct1[3]),0, msg="""
              You do not seem to have a proper linked list, because there is
              no link to the second item.""")
        elif t>1:
          struct=self.structure(path0, path)
          self.assertListEqual(struct1[0], struct[0], msg="""
              You do not seem to have a proper linked list, because the item
              was found in a list with the first item.""")
          self.assertListEqual(struct1[1], struct[1], msg="""
              You do not seem to have a proper linked list, because the item
              was not found in a consistent location in the node.""")
          self.assertListEqual(struct1[3]*t, struct[3], msg="""
              You do not seem to have a proper linked list, because the link
              between nodes is not consistent.""")
    exit()
  def test_len(self):
    enter()
    from LabD5 import LinkedList
    l=LinkedList()
    for i in range(35):
      with self.subTest(size=i):
        self.assertEqual(len(l), i*2, msg="This happens when the len is wrong.")
      l.append(95)
      l.insert(1,13)
    exit()
  def test_module_docstring(self):
    msg=("""
Your file must start with a docstring that explains the purpose and usage
of the file.
""")
    enter()
    import LabD5
    self.assertGreater(len(LabD5.__doc__),20, msg=msg)
    exit()
  def test_class_docstring(self):
    msg=("""
Your LinkedList class must start with a docstring that explains
what the class is used for.
""")
    enter()
    from LabD5 import LinkedList
    self.assertGreater(len(LinkedList.__doc__),20, msg=msg)
    exit()
  def test_func_docstring(self):
    enter()
    from LabD5 import LinkedList
    from types import FunctionType
    for name, f in LinkedList.__dict__.items():
      if type(f)==FunctionType:
        with self.subTest(function=name):
          self.assertGreater(len(f.__doc__),20, msg="This happens when this function does not have an adequate docstring.")
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
