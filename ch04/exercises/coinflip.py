import turtle
import random

'''
determines whether a turtle is in bounds of the screen 
@param
    pen: turtle.Turtle()
        the turtle to be declared in bounds or not
    dimensions: int[]
        from the .screensize() method of a screen object, index 0 is x value, index 1 is y value
@returns: bool
    returns True if turtle is in bounds returns False if not
'''
def turtle_in_bounds(pen, dimensions) -> bool:
    x, y = pen.position()
    return (abs(x) < abs(dimensions[0])) and (abs(y) < abs(dimensions[1]))

def coin_turtle():
    wn = turtle.Screen()
    wn.bgcolor("black")
    dimensions = wn.screensize()        
    print(f"x: {dimensions[0]} y: {dimensions[1]}")

    pen = turtle.Turtle()
    pen.color("white")
    pen.goto(0, 0)
    
    while(turtle_in_bounds(pen, dimensions)):
        flip = random.randint(0, 2)
        if (flip == 0):
            pen.left(90)
            print("Heads!")
        else:
            pen.right(90)
            print("Tails!")
        pen.forward(50)
        print(f"x: {pen.xcor()} y: {pen.ycor()}")
    
    print("Turtle left bounds!")

    wn.exitonclick()

def main():
    coin_turtle()

if (__name__ == "__main__"):
    main()
