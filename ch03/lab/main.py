import turtle
import random
import math

# screen and turtle setup
wn = turtle.Screen() 
wn.bgcolor("blue")
# makes screen into square
sizes = wn.screensize()
if (sizes[0] < sizes[1]):
    wn.screensize(sizes[0], sizes[0])
else:
    wn.screensize(sizes[1], sizes[1])
sizes = wn.screensize()

pen = turtle.Turtle()
pen.speed(10)

'''
draws a circle target the size of the screen 
@param 
    pen: turtle.Turtle()
        the pen the function uses to draw the circle
'''
def draw_target(pen):
    pen.color("pink")
    pen.penup()
    pen.right(90)
    pen.forward(sizes[0])
    pen.left(90)
    pen.pendown()
    pen.begin_fill()
    pen.circle(sizes[0])
    pen.end_fill()
    
    pen.color("black")
    pen.left(90)
    pen.forward(sizes[0] * 2)
    pen.left(180)
    pen.forward(sizes[0])
    pen.left(90)
    pen.forward(sizes[0])
    pen.left(180)
    pen.forward(sizes[0] * 2)
    
    pen.penup()
    pen.home()
    pen.right(90)
    pen.forward(sizes[0])
    pen.left(90)
    pen.pensize(5)
    pen.color("black")
    pen.pendown()
    pen.circle(sizes[0])
    pen.penup()

'''
returns whether or not a coordinate is within a circle based on the radius of the cirlce
@param 
     x: int 
        x coordinate of position
     y: int 
        y coordinate of position
     radius: int
        radius of circle
@returns bool 
    True if the cooridnate is on target 
    False if not
'''
def dart_on_target(x, y, radius):
    if (math.hypot(x, y) > radius):
        return False
    return True

'''
returns two random coordinates given the width and height of a screen
@param 
    sizes: int[]
    an array containing the width and height of a screen, index 0 being width, index 1 being height
@returns int[]
    an array with index 0 being an x coordinate and index 1 being a y coordinate
'''
def dart_coordinates(sizes):
    x = random.randrange(int(-sizes[0]), int(sizes[0]))
    y = random.randrange(int(-sizes[1]), int(sizes[1]))
    return [x, y]

'''
randomly places dots onto a screen given the screen's width and height 
@param 
    pen: turtle.Turtle()
        the turtle element that will be used to draw the points
    sizes: int[]
        an array for screen size in which index 0 contains screen width and index 1 contains screen height
'''
def shoot_dart(pen, sizes):
    shot = dart_coordinates(sizes)
    pen.goto(shot[0], shot[1])
    if (dart_on_target(shot[0], shot[1], sizes[0])):
        pen.color("green")
    else:
        pen.color("red")
    pen.pendown()
    pen.dot(5)
    pen.penup()

draw_target(pen)
for i in range(40):
    shoot_dart(pen, sizes)

wn.exitonclick()


