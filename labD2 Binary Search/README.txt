Make a Python3 file that satisfies the following requirements:

    The file must define a function named hunt that takes two parameters,
    a list and a value. The list will be in sorted order.

    The function should hunt for the value in the list. That is, it must
    loop over the list looking for an entry that matches the value.

    The function must use binary search for the search algorithm.

    If the value is found in the list, the function should return the
    location of the value in the list. For example, if the value is the
    first thing in the list, it should return 0.

    If the value is not found in the list, the function should return None.

    If the file is run, it should use the hunt function to search for 2 
    in the list [1, 2, 3] and then print out the answer.

    If your program is run, its output must exactly match the following:

Test: hunt([1,2,3], 2)
Expected response: 1
Actual response: 1
