# Sidharth and Theodore working on the irma illustration

import turtle
import csv

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.
       :return: a tuple containing the Turtle and the Screen
       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

        

def irma():
    """Animates the path of hurricane Irma
    """
    # Do not change this line
    # t is the turtle, and you will not need the other variables
    (t, wn, map_bg_img) = irma_setup()
    #moving the position of the turtle to initial pos
    t.penup()
    t.setpos(16.4,-30.3)
    t.pendown()
    hurricaneFile = "data/irma.csv"
    # The line below is a little magical. It opens the file,
    # with awareness of any errors that might occur.
    with open(hurricaneFile, 'r') as csvfile:
        # This line gives you an "iterator" you can use to get each line
        # in the file.
        pointreader = csv.reader(csvfile)
        next(pointreader)
        # You'll need to add some code here, before the loop
        # One thing you'll need to figure out how to do is to
        # skip the first line of the file (which is the header).
        # You might use a boolean variable, or you can
        # look into Python's built-in next function
        #(https://docs.python.org/3/library/functions.html#next)
        # pointreader is an iterator

        for row in pointreader:
            # row is a list representing each line in the csv file
            # Each comma separated element is in its own index position
            # This code just prints out the date and time elements of each
            # row in the file.
            # Make sure you understand what is happening here.
            # Then, you'll need to change this code
            lat = row[3] #x-value/latitude of turtle
            long = row[2] #y-value/ longitude of turtle
            windspd = row[4] #windspeed value of turtle
            #print("Date:", row[0], "Time:", row[1], "Lat: ", lat, "Long: ", long, "Windspeed: ", windspd)
            move(lat,long, t) #moving the turtle from previous position to new position
            #print("moved to", lat, long)
            categorize(windspd, t) #the color and display of the hurricane intensity at position
            
            





    # Hack to make sure a reference to the background image stays around
    #canvas = wn.getcanvas()
    #t.shape(map_bg_img)
    # Do not remove or change this line
    return map_bg_img


# Feel free to add "helper" functions here
def move(lat, long, turt):
   '''move turtle according to lat/long'''
   floatLat = float(lat) #converting string lat value to float
   floatLong = float(long)#converting string long value to float
   turt.setx(floatLat)#setting x position to lat
   print("floatLat: " + str(floatLat))
   turt.sety(floatLong)#setting y position to long
   print("floatLong: " + str(floatLong))

def categorize(windSpeed, turt):
    '''Storm Category - category strength, color code, line thickness based off of windSpeed'''
    #Cat 0: 0-73: white width 1
    #Cat 1: 74-85 blue width 1
    #2: 96-110 green width 2
    #3: 111-129 yellow width 4
    #4: 130-155 orange width 6
    #5: 156+ red width 8
    intWindSpeed = int(windSpeed)
    if intWindSpeed < 73:
        turt.color("white")
        turt.width(1)
        print("Cat 0")
    elif intWindSpeed < 95:
        turt.color("blue")
        turt.width(1)
        turt.write("1",False,"right")
        print("Cat 1")
    elif intWindSpeed < 110:
        turt.color("green")
        turt.width(2)
        turt.write("2",False,"right")
        print("Cat 2")
    elif intWindSpeed < 129:
        turt.color("yellow")
        turt.width(4)
        turt.write("3",False,"right")
        print("Cat 3")
    elif intWindSpeed < 156:
        turt.color("orange")
        turt.width(6)
        turt.write("4",False,"right")
        print("Cat 4")
    else:
        turt.color("red")
        turt.width(8)
        turt.write("5",False,"right")
        print("Cat 5")

if __name__ == "__main__":
    bg=irma()