import turtle  # 1. import modules
import random
import math

# Part A

# Initialize Window
window = turtle.Screen()  
window.bgcolor("lightblue")

# Initialize turtles
michelangelo = turtle.Turtle() 
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

'''
resets two turtles to a set position on the screen
Parameters
----------
turtle1: turtle.Turtle()
    A turtle object to be reset to the position -100, 20
turtle2: turtle.Turtle()
    A turtle object to be reset to the position -100, -20
'''
def reset_turtles(turtle1, turtle2):
    turtle1.goto(-100, 20)
    turtle2.goto(-100, -20)

# Get the turtles into position
michelangelo.up() 
leonardo.up()
reset_turtles(michelangelo, leonardo)

# Your PART A code goes here

# Race 1, move turtles forward once
michelangelo.forward(random.randrange(1, 101))
leonardo.forward(random.randrange(1, 101))
reset_turtles(michelangelo, leonardo)

# Race 2, move turtles forward over multiple iterations
for i in range(0, 50):
    michelangelo.forward(random.randrange(1, 11))
    leonardo.forward(random.randrange(1, 11))
reset_turtles(michelangelo, leonardo)

michelangelo.hideturtle()
leonardo.hideturtle() 

# PART B - complete part B here
'''
Calculates the external angle of a regular polygon
Parameters
---------- 
sides : int 
    The number of sides in a regular polygon 

Returns
------- 
float
    The value of the external angle of a regular polygon with the inputted amount of sides
'''
def calculate_external_angle(sides):
    return 360 / sides

'''
Creates a turtle, draws a regular polygon, then clears the screen after finished
Parameters
----------
sides : int
    The number of sides of the regular polygon that is to be drawn on the screen 
'''
def draw_shape(sides):
    shape_pen = turtle.Turtle()
    shape_pen.shape("arrow")

    for i in range(0, sides):
        shape_pen.forward(500 / sides)
        shape_pen.right(calculate_external_angle(sides))

    shape_pen.clear()

draw_shape(3)
draw_shape(4)
draw_shape(6)
draw_shape(20)
draw_shape(100)
draw_shape(360)

window.exitonclick()
