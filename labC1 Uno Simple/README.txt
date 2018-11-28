Make a Python3 file that satisfies the following requirements:

    The file must define a function named best_move that takes two parameters,
    a game and a list of moves.

    The function should use the utility function provided by the game
    to see how good each move is.

    The function should use extreme value search to find and return the
    move that has the biggest utility.

    If the list is empty, the function should return None.

    You should not change the GameUno.py or test.py files.

    If the file is run, it should run the code provided in the intial LabC1.py
    file, and out exactly:

best_move(GameUno, [('Red', 7, 7), ('Red', 3, 3), ('Blue', 'Draw 2', 20)])
Expected answer: ('Blue', 'Draw 2', 20)
Actual answer: ('Blue', 'Draw 2', 20)
