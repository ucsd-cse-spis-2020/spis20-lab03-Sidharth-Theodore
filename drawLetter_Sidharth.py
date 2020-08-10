#Sidharth working on part 1.2
import turtle

def drawA(turt):
    turt.pendown()
    turt.forward(30)
    print("moved 30 steps forward")
    turt.left(90)
    print("turned left")
    turt.forward(50)
    print("moved 50 steps forward")
    turt.left(90)
    print("turned left")
    turt.forward(30)
    print("moved 30 steps forward")
    turt.right(90)
    print("turned right")
    turt.forward(50)
    print("moved 50 steps forward")
    turt.right(90)
    print("turned right")
    turt.forward(30)
    print("moved 30 steps forward")
    turt.penup()

myTurtle = turtle.Turtle() 
turt2 = turtle.Turtle()
turt2.penup()
turt2.setposition(0,-200)
turt2.pendown()

drawA(myTurtle)  
drawA(turt2)