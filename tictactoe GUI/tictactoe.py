#! /usr/bin/env python3
# Tyler Whitney
# Tic Tac Toe Game

import turtle

turnNum = 1

def drawLine(t, a, b, x, y):
    # Draw a simple line from point a, b to point x, y
    t.penup()
    t.setpos(a, b)
    t.pendown()
    t.setpos(x, y)

def getGridCoords(grid):
    # Return the coordinates for the center of the 
    # square at the grid number specific, starting at
    # the left of the grid going down it is 1, 2, and 3
    # the next column going down is 4, 5 and 6, and the 
    # third column to the right going down is 7, 8, and 9
    if(grid == 1 or grid == 2 or grid == 3):
        x = 50
    if(grid == 4 or grid == 5 or grid == 6):
        x = 150
    if(grid == 7 or grid == 8 or grid == 9):
        x = 250
    if(grid == 1 or grid == 4 or grid == 7):
        y = 250
    if(grid == 2 or grid == 5 or grid == 8):
        y = 150
    if(grid == 3 or grid == 6 or grid == 9):
        y = 50
    return x, y

def drawO(t, grid):
    # Determine the coordinates by the grid
    # number specified
    x, y = getGridCoords(grid)
    t.penup()
    # Rather than set position at center of 
    # the grid coordinate, start at the bottom
    # because we're drawing a circle above our turtle
    t.setpos(x, y-45)
    t.pendown()
    t.pensize(5)
    t.circle(45)

def drawX(t, grid):
    # Determine the coordinates by the grid 
    # number specified
    x, y = getGridCoords(grid)
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.pensize(3)
    # Draw a line in 4 directions to crate X symbol using 
    # 45 degree angles
    for i in [45, -45, 135, -135]:
        t.rt(i)
        t.forward(50)
        t.setpos(x, y)
        t.setheading(0)

def drawShape(t, shape, grid):
    if shape.lower() == "o":
        drawO(t, grid)
    elif shape.lower() == "x":
        drawX(t, grid)
    else:
       raise Exception('You can only draw "x" or "o"')

def drawBoard(t):
    # Draw lines at bottom and top horizontall 
    # then left and right vertically
    drawLine(t, 0, 100, 300, 100)
    drawLine(t, 0, 200, 300, 200)
    drawLine(t, 100, 300, 100, 0)
    drawLine(t, 200, 300, 200, 0)

def doTurn(x, y):
    global turnNum
    tess = turtle.Turtle()
    if (turnNum %2==0):
        shape="o"
    else:
        shape="x"
    if (x<100 and y>200):
        drawShape(tess, shape, 1)
    elif (x<100 and y<200 and y>100):
        drawShape(tess, shape, 2)
    elif (x<100 and y<100):
        drawShape(tess, shape, 3)
    elif (x>100 and x<200 and y>200):
        drawShape(tess, shape, 4)
    elif (x>100 and x<200 and y>100 and y<200):
        drawShape(tess, shape, 5)
    elif (x>100 and x<200 and y<100):
        drawShape(tess, shape, 6)
    elif (x>200 and y>200):
        drawShape(tess, shape, 7)    
    elif (x>200 and y<200 and y>100):
        drawShape(tess, shape, 8)
    elif (x>200 and y<100):
        drawShape(tess, shape, 9)

    turnNum=turnNum+1

def main():
    # Create the window, set bg color, create turtle
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    tic = turtle.Turtle()
    
    # Setup the canvas
    wn.setup(300, 300)
    wn.screensize(300, 300)
    wn.setworldcoordinates(0, 0, 300, 300)

    # Draw the tic tac toe board
    drawBoard(tic)
   
    # When user clicks, draw a shape on the board
    wn.onclick(doTurn) 
 
    # Keep the window open
    wn.mainloop()

# Conditional call to main
if __name__ == "__main__":
    main()
