import turtle

'''
Determines the external angle of a regular polygon with a given number of sides
parameters
---------- 
sides: int
    number of sides of a regular polygon

returns
------- 
float
    value of external angle
'''
def external_angle(sides):
    return (360 / sides)

'''
uses turtle module to draw a regular polygon onto the screen 
parameters
---------- 
sides: int 
    the number of sides in the regular polygon
length: int 
    the length of each of the sides in the regular polygon
'''
def draw_shape(sides, length):
    wn = turtle.Screen()
    wn.bgcolor("black")

    turtle1 = turtle.Turtle()
    turtle1.color("white")

    for i in range(sides):
        turtle1.forward(length)
        turtle1.right(external_angle(sides))

    wn.exitonclick()

try:
    print("Please enter the amount of sides you want your shape to have.")
    sides = int(input("# of sides: "))
    print("Please enter how long you want each of your sides to be.")
    length = int(input("Length of sides: "))

    draw_shape(sides, length)
except ValueError:
    print("There was an error. Please try again using valid numbers.")
