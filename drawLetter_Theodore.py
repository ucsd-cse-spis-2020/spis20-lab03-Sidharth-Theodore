#Theodore Hui, draws letter T
import turtle
def drawT(theTurtle):
    '''Takes a turtle, uses it to draw letter T'''
    theTurtle.pd()
    theTurtle.forward(100)
    theTurtle.right(180)
    theTurtle.forward(50)
    theTurtle.left(90)
    theTurtle.forward(100)

bobRoss = turtle.Turtle()
myScreen = turtle.Screen()
myScreen.screensize(400,400)
drawT(bobRoss)