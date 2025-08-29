import turtle

# Set up turtle screen
screen = turtle.Screen()

# Create a turtle instance
pen = turtle.Turtle()

# Move the turtle into position
pen.penup()
pen.goto(0, 0)
pen.pendown()

# Set colors
screen.bgcolor("pink")
pen.color("white")

# Write message
pen.write("Hello, Evelyn!")

# Keep the window open until clicked
screen.exitonclick()
