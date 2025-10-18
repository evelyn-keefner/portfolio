import turtle
import random

'''
Draws window background
'''
def draw_background() -> None:
    SUN_X_COORDINATE = -190
    SUN_Y_COORDINATE = 190
    SUN_SIZE = 50
    SUN_COLOR = "yellow"
    GROUND_WIDTH = 18
    GROUND_COLOR = "palegreen4"
    GROUND_LEFT_BOUND = -250
    GROUND_RIGHT_BOUND = 250
    pen = turtle.Turtle()

    pen.speed(10)
    pen.penup()
    pen.goto(SUN_X_COORDINATE, SUN_Y_COORDINATE)
    pen.pendown()
    pen.dot(SUN_SIZE, SUN_COLOR)
    pen.width(GROUND_WIDTH)
    pen.penup()
    pen.goto(GROUND_LEFT_BOUND, 0)
    pen.pendown()
    pen.color(GROUND_COLOR)
    pen.goto(GROUND_RIGHT_BOUND, 0)

'''
draws a trunk
@param
    pen: turtle.Turtle()
        pen used to draw trunk
    length: int
        length of trunk
    width: float
        width of trunk
'''
def draw_trunk(pen: turtle.Turtle(), length: float, width: float) -> None:
    TRUNK_COLOR = "brown"

    pen.color(TRUNK_COLOR)
    pen.setheading(90)
    pen.width(width)
    pen.forward(length)
    return None

'''
draws a leaf
@param
    pen: turtle.Turtle()
        pen used to draw leaf
    x: int
        x position for leaf 
    y: int
        y position for leaf
'''
def draw_leaf(pen: turtle.Turtle(), x: int, y: int) -> None:
    LEAF_COLOR = "green"

    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.dot(random.randint(8, 16), LEAF_COLOR)
    pen.penup()
    
    return None

'''
recursively draws branches, decreasing length for each new branch off of an existing branch
@param
    pen: turtle.Turtle()
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
def draw_branches(pen: turtle.Turtle(), x: int, y: int, size: float, branch_frequency: float, size_decay: float, leaf_frequency: float, random_leaf_frequency: float, degree_range: float, degree_growth: float) -> None:
    MINIMUM_BRANCH_SIZE = 10
    BRANCH_COLOR = "brown"
    # End condition of size
    if (size < MINIMUM_BRANCH_SIZE):
        # Rolls to draw leaves on the end of branches that fall below minimum branch size
        leaf_chance = 100 * (random.random())
        if leaf_frequency >= leaf_chance:
            draw_leaf(pen, x, y)
        return None 
    
    # Calculates new values for next branch iteration
    step_size = int(size / 10)
    new_size = size / size_decay # Size decay must be above 1 in order to decrease size and fulfull the end condition
    new_degree_range = degree_range + degree_growth * random.random()
    
    # choose random direction
    direction = random.uniform(-degree_range, degree_range)
    
    # set up pen
    pen.penup()
    pen.goto(x, y)
    pen.pensize(length_to_width(size))
    pen.color(BRANCH_COLOR)
    pen.setheading(90)
    pen.left(direction)
    pen.pendown()
    
    # Breaks each movement into 10 steps
    branch_points = []
    for i in range(10):
        pen.forward(step_size)
        current_x = pen.xcor()
        current_y = pen.ycor()
        branch_points.append((current_x, current_y))
    pen.penup()
    
    for current_x, current_y in branch_points:
        branch_chance = 100 * (random.random())
        random_leaf_chance = 100 * (random.random())
        if random_leaf_frequency >= random_leaf_chance:
            draw_leaf(pen, current_x, current_y)
        if branch_frequency >= branch_chance:
            draw_branches(pen, current_x, current_y, size, branch_frequency, size_decay, leaf_frequency, random_leaf_frequency, new_degree_range, degree_growth)
    
    # Calculates new values for next branch to begin, this cannot be done before the pen moves as these coordiinates are dependent on the random direction pen goes
    new_x: int = pen.xcor() 
    new_y: int = pen.ycor()

    # Creation of new branches at the end of the current branch
    for i in range(random.randint(2, int(branch_frequency))):
        draw_branches(pen, new_x, new_y, new_size, branch_frequency, size_decay, leaf_frequency, random_leaf_frequency, new_degree_range, degree_growth)
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
def draw_tree(x: int, y: int, size: float, branch_frequency: float, size_decay: float, leaf_frequency:float, random_leaf_frequency: float, degree_range: float, degree_growth: float) -> None: 
    pen = turtle.Turtle()
    pen.speed(10)

    draw_trunk(pen, size, length_to_width(size))
    new_y = size
    for i in range(random.randint(1, int(branch_frequency))):
        draw_branches(pen, x, new_y, size, branch_frequency, size_decay, leaf_frequency, random_leaf_frequency, degree_range, degree_growth)
    pen.hideturtle()
    return None

'''
@param
returns a width value from branch length using a set equation
    length : float
        length of a branch
@returns : float
    the width of a branch
'''
def length_to_width(length: float) -> float:
    return length / 6

'''
Prompts user for a float value
@param 
    message : str
        Message to prompt user with
@returns : float
    float value that the user types in
'''
def user_input(message: str) -> float:
    user_input = None
    print(message)
    while type(user_input) != type(1.0):
        try:
            user_input = float(input(":"))
        except:
            print("Please enter a positive float value.")
    return user_input

def main() -> None:
    wn = turtle.Screen()
    NEGATIVE_X_BOUND = -250
    NEGATIVE_Y_BOUND = 0
    POSITIVE_X_BOUND = 250
    POSITIVE_Y_BOUND = 250
    TITLE = "Random Tree"
    BG_COLOR = "lightskyblue"
    
    wn.screensize(POSITIVE_X_BOUND + abs(NEGATIVE_X_BOUND), POSITIVE_Y_BOUND + abs(NEGATIVE_Y_BOUND)) 
    wn.setworldcoordinates(NEGATIVE_X_BOUND, NEGATIVE_Y_BOUND, POSITIVE_X_BOUND, POSITIVE_Y_BOUND)
    wn.title(TITLE)
    wn.bgcolor(BG_COLOR)
    draw_background()
    x = 0
    y = 0

    # fast mode query
    print("Do you want to turn on fast generation? This will make it so you will not see the pen tracing out the tree. Respond either 'y' or 'n'")
    try:
        fast_mode_query = input(":")
    except: 
        pass
    while (fast_mode_query.lower() != 'y') and (fast_mode_query.lower() != 'n'):
        print("Please try again. Please enter either 'y' or 'n'")
        fast_mode_query = input(":")


    if fast_mode_query == 'y': 
        wn.tracer(False)

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
    wn.update()
    wn.exitonclick()
    return None

if __name__ == '__main__':
    main()
