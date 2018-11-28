#!/usr/bin/python3
#Alejo Pijuan

def best_move(thegame, bmove):
        """If bmove is empty, the program will return "None". The program will
         inspect "bomve" and return the best possible move."""
        bestmove = None
        bestmovevalue = None
        for value in bmove:
            utility = thegame.utility(value)
            try:
                if utility > bestmovevalue:
                    bestmove = value
                    bestmovevalue = utility
            except TypeError:
                bestmove = value
                bestmovevalue = utility
        return bestmove

if __name__ == "__main__":
    from GameUno import GameUno, RED, GREEN, BLUE, YELLOW, \
                        REVERSE, SKIP, DRAW2, WILD, WILD4

    thegame=GameUno()
    bmove=[thegame.card(7,RED), thegame.card(3,RED), thegame.card(DRAW2, BLUE)]
    print('best_move(GameUno, {})'.format(bmove));
    print('Expected answer: {}'.format(bmove[2]))
    print('Actual answer: {}'.format(best_move(thegame, bmove)))
