import turtle

'''
from a starting value, halves a number if it is even, multiplies by 3 and adds 1 to a number if it is odd, until the number reaches 1 or less
@param
    n : int
        starting value for algorithm
@returns : int
    the number of iterations it takes a value to reach 1 or less
'''
def threenp1(n) -> int:
    count = 0
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        count += 1
    return count

'''
creates a dictionary of the inputs and outputs of the 3n+1 sequence (see threenp1(n)) 
@param
    upper_limit : int
        the highest input you want to see up to
@returns : dict
    dictionary formatted {input value to 3n+1 sequence, output count of how long it takes input value to reach 1 or less}
'''
def threenp1range(upper_limit) -> dict:
    dict = {}
    for i in range (2, (upper_limit + 1)):
        dict[i] = threenp1(i)
    return dict

'''
creates a graph utilizing the turtle module and a set of x and y points
@param
    threenp1_iters_dict : dict
        dictionary formatted as {x, y}
'''
def graph_coordinates(threenp1_iters_dict):
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, 10, 10)
    wn.bgcolor("black")

    graph = turtle.Turtle()
    graph.color("white")
    graph.speed(5)
    graph.penup()
    graph.goto(0, 0)
    graph.pendown()

    pen = turtle.Turtle()
    pen.color("white")
    pen.speed(5)
    pen.penup()
    pen.goto(0, 10)

    max_so_far = 0
    for k, v in threenp1_iters_dict.items():
        wn.setworldcoordinates(0, 0, (k + 10), (max_so_far + 10))
         
        if (v > max_so_far):
            max_so_far = v
            pen.clear()
            wn.setworldcoordinates(0, 0, (k + 10), (max_so_far + 10))
            pen.goto(0, max_so_far + 9)
            pen.pendown()
            pen.write(f"Max so far: {max_so_far}")
            pen.penup()
         
        graph.goto(k, v)

    wn.exitonclick()

def main():
    dict = threenp1range(10)
    print(dict)
    graph_coordinates(dict)

if (__name__ == "__main__"):
    main()
