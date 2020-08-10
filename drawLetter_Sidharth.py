import turtle

def drawA(turt):
    turt.pendown()
    turt.forward(30)
    turt.left(90)
    turt.forward(50)
    turt.left(90)
    turt.forward(30)
    turt.right(90)
    turt.forward(50)
    turt.right(90)
    turt.forward(30)
    turt.penup()

myTurtle = turtle.Turtle() 
turt2 = turtle.Turtle()
turt2.penup()
turt2.setposition(0,-200)
turt2.pendown()

drawA(myTurtle)  
drawA(turt2)