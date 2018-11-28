#! /usr/bin/env python3

# Tyler Whitney
# 10/20/2016
# Test suite for lab08

import sys
import lists # import our lab08 lists.py file

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def main():
    """ Run the suite of tests for code in this module (this file).
    """
    test(lists.productOfEven([1,2,3,4]) == 8)
    test(lists.productOfEven([2,2,2,2]) == 16)
    test(lists.productOfEven([1,2,1,2]) == 4)
    test(lists.productOfEven([4,6,7,8]) == 192)
    test(lists.productOfEven([1,1,1,3]) == 1)

    test(lists.sumOfOdd([1,2,3,4]) == 4)
    test(lists.sumOfOdd([2,2,2,2]) == 0)
    test(lists.sumOfOdd([1,2,1,2]) == 2)
    test(lists.sumOfOdd([4,6,7,8]) == 7)
    test(lists.sumOfOdd([1,1,1,3]) == 6)
  
    test(lists.oddMembers([1,2,3,4]) == [1,3])
    test(lists.oddMembers([2,4,6,8]) == [])
    test(lists.oddMembers([1,2,3,4,5,6,7,8,9,10]) == [1,3,5,7,9])
    test(lists.oddMembers([3,4,5,6]) == [3,5])
    test(lists.oddMembers([10,11,12,14]) == [11])

    mylist = [1,2,3,4]
    lists.changeList(mylist)
    test(mylist == [10,1,14,2]) # Test 1
    mylist = [4,5,6,7]
    lists.changeList(mylist)
    test(mylist == [2,18,3,22]) # Test 2

    test(lists.isReverse([1,2,3,4],[4,3,2,1]) == True)
    test(lists.isReverse([1,2,3,4],[2,3,2,1]) == False)
    test(lists.isReverse([1,2,3,4],[3,2,1,0]) == False)
    test(lists.isReverse([4,5,6,7],[7,6,5,4]) == True)
    test(lists.isReverse([9,8,7,6],[6,7,8,9]) == True)

if __name__ == '__main__':
    main()
