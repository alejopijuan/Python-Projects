#!/usr/bin/python3
#Alejo Pijuan
'''This program will will look at a hand of cards and sort them by color, then value and then type'''

def sort_hand(l):
    """sort the list  with quicksort """
    if len(l) == 1:
        return None
    sortiter(l,0,len(l)-1)

def cutit(l,firstinlist,lastinlist):
   thepivot = l[firstinlist]
   left = firstinlist+1
   right = lastinlist
   done = False
   while not done:
       while left <= right and l[left] <= thepivot:
           left = left + 1
       while l[right] >= thepivot and right >= left:
           right = right -1
       if right < left:
           done = True
       else:
           temporal = l[left]
           l[left] = l[right]
           l[right] = temporal

   temporal = l[firstinlist]
   l[firstinlist] = l[right]
   l[right] = temporal
   return right



def sortiter(l,firstinlist,lastinlist):
    if firstinlist<lastinlist:
       splitit = cutit(l,firstinlist,lastinlist)
       sortiter(l,firstinlist,splitit-1)
       sortiter(l,splitit+1,lastinlist)


if __name__ == "__main__":
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4

    game=GameUno()
    moves=[game.card(7,RED), game.card(3,RED), game.card(DRAW2, BLUE)]
    print('sort_hand({})'.format(moves));
    print("Expected answer: [('Blue', 'Draw 2', 20), ('Red', 3, 3), ('Red', 7, 7)]")
    sort_hand(moves)
    print('Actual answer: {}'.format(moves))
