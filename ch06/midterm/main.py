import turtle
import random

'''
draws a trunk
@param
    length: int
        length of trunk
    width: float
        width of trunk
'''
def draw_trunk(length, width) -> None:
    pen = turtle.Turtle()
    pen.color("brown")
    pen.left(90)
    pen.width(width)
    pen.forward(length)
    pen.hideturtle()
    return None

'''
draws a leaf
@param
    x: int
        x position for leaf 
    y: int
        y position for leaf
'''
def draw_leaf(x, y) -> None:
    pen = turtle.Turtle()
    pen.speed(10)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.dot(random.randint(8, 16), "green")
    pen.penup()
    pen.hideturtle()
    
    return None

'''
recursively draws branches, decreasing length for each new branch off of an existing branch
@param
    x: int
        starting x position for branch
    y: int
        staring y position for branch
    size: float 
        size of branch
    branch_frequency: float 
        chance of new branch appearing, higher values means more branches will appear
    size_decay: float 
        determines the decay rate of new branches, and how small childen branches will be off of their parents
    leaf_frequency: float
        determines the chance for leaves to be spawned on the end of a small branch
    random_leaf_frequency: float
        determines the chance for leaves to be spawned along the side of a branch of any size
    degree_range: float
        determines the range of degrees in which the next branch can be
    degree_growth: float
        determines if degree_range will increase as branches get smaller
'''
def draw_branches(x, y, size, branch_frequency, size_decay, leaf_frequency, random_leaf_frequency, degree_range, degree_growth) -> None:
    if (size < 10):
        leaf_chance = 100 * (random.random())
        if leaf_frequency >= leaf_chance:
            draw_leaf(x, y)
        return None
    
    step_size = int(size / 10)

    new_size = size / size_decay

    new_degree_range = degree_range + degree_growth * random.random()
    
    # set up turtle
    pen = turtle.Turtle()
    pen.color("brown")
    pen.speed(10)
    pen.penup()
    pen.goto(x, y)
    pen.pensize(length_to_width(size))
    pen.left(90)
    # choose random direction
    pen.left(random.uniform(-degree_range, degree_range))
    pen.pendown()
    
    for i in range(10):
        pen.forward(step_size)
        branch_chance = 100 * (random.random())
        random_leaf_chance = 100 * (random.random())
        if random_leaf_frequency >= random_leaf_chance:
            draw_leaf(pen.xcor(), pen.ycor())

        if branch_frequency >= branch_chance:
            draw_branches(pen.xcor(), pen.ycor(), size, branch_frequency, size_decay, leaf_frequency, random_leaf_frequency, new_degree_range, degree_growth)
        
    pen.penup()
    pen.hideturtle()
    
    new_x: int = pen.xcor() 
    new_y: int = pen.ycor()

   
    for i in range(random.randint(2, int(branch_frequency))):
        draw_branches(new_x, new_y, new_size, branch_frequency, size_decay, leaf_frequency, random_leaf_frequency, new_degree_range, degree_growth)
    return None

'''
draws a tree
@param
    x: int
    y: int
    size: float 
    branch_frequency: float 
    size_decay: float
    leaf_frequency: float
    random_leaf_frequency: float
    degree_range: float
    degree_growth: float
        To be entered into draw_branches() function
'''
def draw_tree(x, y, size, branch_frequency, size_decay, leaf_frequency, random_leaf_frequency, degree_range, degree_growth) -> None:
    draw_trunk(size, length_to_width(size))
    new_y = size
    for i in range(random.randint(1, int(branch_frequency))):
        draw_branches(x, new_y, size, branch_frequency, size_decay, leaf_frequency, random_leaf_frequency, degree_range, degree_growth)
    return None

'''
@param
returns a width value from branch length using a set equation
    length : float
        length of a branch
@returns : float
    the width of a branch
'''
def length_to_width(length) -> float:
    return length / 6

'''
Prompts user for a float value
@param 
    message : str
        Message to prompt user with
@returns : float
    float value that the user types in
'''
def user_input(message) -> float:
    user_input = ""
    print(message)
    while type(user_input) != type(1.0):
        try:
            user_input = float(input(":"))
        except:
            print("Please enter a positive float value.")
    return user_input

def draw_background() -> None:
    pen = turtle.Turtle()
    pen.speed(10)
    pen.penup()
    pen.goto(-190, 190)
    pen.pendown()
    pen.dot(50, "yellow")
    pen.width(18)
    pen.penup()
    pen.goto(-250, 0)
    pen.pendown()
    pen.color("palegreen4")
    pen.goto(250, 0)

def main() -> None:
    wn = turtle.Screen()
    wn.setworldcoordinates(-250, 0, 250, 250)
    wn.title("Random Tree")
    wn.bgcolor("lightskyblue")
    draw_background()
    x = 0
    y = 0
    # get initial size
    size = user_input("Enter an initial size for the trunk. Reccomended size 50.")
    # branch frequency
    branch_frequency = user_input("Enter a value for branch frequency. Reccomended value 3, value must be above 1. WARNING: Higher values will exceptionally increase generation time")
    # branch size decay
    size_decay = user_input("Enter a value for branch decay, higher values mean the branches will decay faster. Reccomended value is 1.5, values between 0 and 1 are not valid")
    # leaf frequency on small branches
    leaf_frequency = user_input("Enter a value for leaf frequency. Higher values will mean that there is a greater chance for a leaf to be generated on small branches. Enter on a scale of 0 to 100. Reccomended value 5.")
    # leaf frequency on any branch 
    random_leaf_frequency = user_input("Enter a value for random leaf frequency. Higher values will mean there is a greater chance for a leaf to appear randomly along any branch. Enter on a scale of 0 to 100 reccomended value 5.")
    # degree range
    degree_range = user_input("Enter a value for degree range. Recommended value is 60")
    # degree growth factor
    degree_growth = user_input("Enter a value for degree growth. Higher values mean that the tree branches will have a wider spread toward the top. Prefers smaller values 1 - 5")

    draw_tree(x, y, size, branch_frequency, size_decay, leaf_frequency, random_leaf_frequency, degree_range, degree_growth)

    wn.exitonclick()
    return None

if __name__ == '__main__':
    main()
