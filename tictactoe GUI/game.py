#! /usr/bin/env python3
# Alejo Pijuan
# 9/29/16
"""This program will continuously play a number guessing game with the user
until the user decides to quit """
from random import randint
def main():
    win=0
    lose=0
    
    print("Welcome to the game, I will guess a number betweeb 1 and 10. The goal is to guess the number within 1 number of accuracy. We will keep playing until you choose the number 0 to exit.")
    while(1):
        n = eval(input("Guess the number I picked. If you choose 0, the game will end: "))
        if(n==0):
            print("The game is over, we played " + str(win+lose) + " rounds")
            print ("You lost " + str(lose) + " rounds")
            print ("You won " + str(win) + " rounds")
            break
        print("Round " + str(win+lose+1) + " - You chose: " + str(n))
        r= randint(1,10)
           
        if (r==n or r==n+1 or r==n-1):
            win=win+1
            print("You won round " + str(win+lose) + "! I picked: " + str(r))
        else:
            lose=lose+1
            print("You lost round "  + str(win+lose) + "! I picked: " + str(r) )
        


if __name__ == "__main__":
    main()
