import turtle
def drawT(theTurtle):
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