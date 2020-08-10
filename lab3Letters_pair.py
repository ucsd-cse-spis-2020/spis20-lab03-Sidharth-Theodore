#Sidharth and Theodore
#1.the "anonymous turtle" is the default turtle used if none are created in Code, or the first created if multiple are created
#2."turtle" refers to the turtle library while "Turtle()" refers to the turtle class
#3.myTurtle.sety(100)

import turtle
def drawT(theTurtle, size):
    '''Takes a turtle, uses it to draw letter T'''
    theTurtle.pd()
    theTurtle.forward(10*size)
    theTurtle.right(180)
    theTurtle.forward(5*size)
    theTurtle.left(90)
    theTurtle.forward(10*size)

bobRoss = turtle.Turtle()
myScreen = turtle.Screen()
myScreen.screensize(400,400)
drawT(bobRoss, 20)