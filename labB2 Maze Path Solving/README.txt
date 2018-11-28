Make a Python3 file that satisfies the following requirements:

    The file must define a class named Stack that implements a stack.

    The Stack class should implement all of the methods required for
    stacks and no additional methods.

    The file must define a function solve that is used to solve a maze.
  
    Solve must use the stack to find the solution to the maze, as described
    in the provided pseudocode. You do not need to follow the pseudocode
    exactly, but you will need to follow it closely to pass the tests.

    The provided pseudocode will explore the same path multiple times
    if there are any loops in the maze. In some cases (consider nomaze.txt),
    it can take a very long time to solve the maze. Modify the procedure
    for finding paths so that it does not explore more paths than necessary.

    You must not use built in sorting functions, including "index," "sort" and
    "sorted."

    If the file is run, it should run the code provided in the intial LabC3.py
    file. It will draw a maze on the screen and show the solutions as they
    are attemoted and then output exactly:

PATH:
[(0, 6), (1, 6), (2, 6), (3, 6), (3, 5), (3, 4), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 8), (10, 8), (11, 8)]
