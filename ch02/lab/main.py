import turtle  # 1. import modules
import random
import math

# Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor("lightblue")

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

def reset_turtles(turtle1, turtle2):
    turtle1.goto(-100, 20)
    turtle2.goto(-100, -20)

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
reset_turtles(michelangelo, leonardo)

## 5. Your PART A code goes here
michelangelo.forward(random.randrange(1, 101))
leonardo.forward(random.randrange(1, 101))
reset_turtles(michelangelo, leonardo)

for i in range(0, 50):
    michelangelo.forward(random.randrange(1, 11))
    leonardo.forward(random.randrange(1, 11))
reset_turtles(michelangelo, leonardo)

michelangelo.hideturtle()
leonardo.hideturtle() 

# PART B - complete part B here

def calculate_external_angle(sides):
    return 360 / sides

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
