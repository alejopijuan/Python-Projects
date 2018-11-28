"""Implementation of an Uno game."""

# Author: Dr. Steven P. Crain, steven.crain@plattsburgh.edu
# Date: 2/13/2017
# Licence: Licensed under a Creative Commons non-commercial attribution
#          license.
from itertools import chain
import random

RED="Red"
GREEN="Green"
BLUE="Blue"
YELLOW="Yellow"
SKIP="Skip"
REVERSE="Reverse"
DRAW2="Draw 2"
WILD="*Wild*"
WILD4="*Wild Draw 4*"

class GameUno:
  """Class representing an Uno Game."""
  def utility(game, card):
    """Return the value of the card. This is based on the penalty for
       holding the card at the end of a round.
    """
    return card[2]
  def card(game, value, color=None):
    """Return a tuple representing the card, based on the specified
       value and color. The value should be a number from 0 to 10 or
       one of the special constants SKIP, REVERSE, DRAW2, WILD or WILD4.
       Value should not have the same contents as these, but must actually
       reference the same value. Color must reference one of the constants
       RED, GREEN, BLUE or YELLOW, except that the color of a WILD or WILD4
       should be omitted.
    """
    if value in (SKIP, REVERSE, DRAW2):
      return (color, value, 20)
    if value in (WILD, WILD4):
      return (WILD, value, 50)
    return (color, value, value)
  def __init__(game):
    """Set up a new Uno game. A full set of Uno cards is in sorted order
       in the discard pile, and the deck is empty.
    """
    game.deck=[]
    game.discard=[]
    game.nextdraw=None
    for color in (RED, GREEN, BLUE, YELLOW):
      for value in chain(range(10), range(1,10), \
            (SKIP, REVERSE, DRAW2)*2):
        game.discard.append(game.card(value, color))
    for value in (WILD, WILD4)*4:
      game.discard.append(game.card(value))
    num=len(game.discard)
    first=num-1
    try:
      while game.discard[first][2]>10: # Choose a random number card
        first=random.randint(0,num-1)
    except:
      print("Error comparing {}".format(game.discard[first]))
      raise
    game.discard[-1], game.discard[first] = \
      game.discard[first], game.discard[-1]
  def draw(game):
    """ Draw a card from the top of the deck. If the deck is empty,
        reshuffle from the discard pile.
    """
    try:
      return game.deck.pop()
    except IndexError:
      game.reshuffle()
      if len(game.deck)==0:
        return None
      return game.deck.pop()
  def legal(game, hand):
    """ Return the list of cards that can be legally played from the hand.
    """
    if game.nextdraw != None:
      return []
    wild4=None
    hasColor=False
    legal=[]
    for card in hand:
      if card[1]==WILD4:
        wild4=card
      elif card[0]==game.discard[-1][0]:
        legal.append(card)
        hasColor=True
      elif card[1]==WILD or card[1]==game.discard[-1][1]:
        legal.append(card)
    if not hasColor and wild4 != None:
      legal.append(wild4)
    return legal
  def reshuffle(game):
    """ Leaving only the top card of the discard pile in place, shuffle
        all of the cards in the deck and discard pile together to form
        a new deck.
    """
    try:
      top=game.discard.pop()
      game.deck.extend(game.discard)
      game.discard=[top]
    except IndexError:
      pass
    random.shuffle(game.deck)

if __name__ == "__main__":
  game=GameUno()
  card=game.draw()
  print("We drew the card {}".format(card))
