Make a Python3 file that satisfies the following requirements:

    The file must define a function named sort_hand that takes a list
    of cards as its parameter.

    The function should sort the cards in the hand in place, using any
    sorting algorithm.

    The cards are encoded as tuples of three items, first the color (card[0]),
    then the kind of card (card[1]) and finally the value (card[2]). 
    The cards must be sorted by color. If the color matches, it should
    be sorted by value. If the color and value both match, it should be sorted
    by kind of card.
  
    You should not change the GameUno.py or test.py files.

    You must not use built in sorting functions, including "sort" and
    "sorted."

    If the file is run, it should run the code provided in the intial LabC1.py
    file, and out exactly:

sort_hand([('Red', 7, 7), ('Red', 3, 3), ('Blue', 'Draw 2', 20)])
Expected answer: [('Blue', 'Draw 2', 20), ('Red', 3, 3), ('Red', 7, 7)]
Actual answer: [('Blue', 'Draw 2', 20), ('Red', 3, 3), ('Red', 7, 7)]
