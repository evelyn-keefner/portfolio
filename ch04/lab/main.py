import target
import turtle

'''
simulates a dart throwing game between two players
@param 
    pen: turtle.Turtle()
        The pen used to place darts on the target 
    sizes: int[]
        screen width [0] and height [1] that is needed to shoot darts on the target accurately
    rounds: int
        the number of rounds the game will go on 
    guess: int
        the users' guess on which player will win 1 or 2
@returns: int
    0 if game is a tie
    1 if player 1 (green) wins 
    2 if player 2 (red) wins
'''
def simulate_game(pen, sizes, rounds, guess) -> int:
    player1_score = 0
    player2_score = 0
    score_writer = turtle.Turtle()
    score_writer.color("white")
    score_writer.speed(0)

    for i in range(rounds):
        if (target.shoot_dart(pen, sizes, "green")):
            player1_score += 1
            print(f"player 1: {player1_score}")
        
        if (target.shoot_dart(pen, sizes, "red")):
            player2_score += 1
            print(f"player 2: {player2_score}")
        
        score_writer.clear()
        score_writer.penup()
        score_writer.goto(-sizes[0], sizes[1])
        score_writer.pendown()
        score_writer.write(f"Player 1 (Green): {player1_score}", align="left", font=('Arial', 24, 'normal'))
        score_writer.penup()
        score_writer.goto(sizes[0], sizes[1])
        score_writer.pendown()
        score_writer.write(f"Player 2 (Red): {player2_score}", align="right", font=('Arial', 24, 'normal'))
        score_writer.penup()

    score_writer.goto(0, 0)
    score_writer.pendown()
    if (player1_score > player2_score):
        if (guess == 1):
            score_writer.write("You guessed the winner correctly!", align="center", font=('Arial', 22, 'normal'))
        else:
            score_writer.write("You didn't guess the winner this time.", align="center", font=('Arial', 22, 'normal'))
        return 1 # player 1 wins
    elif (player2_score > player1_score):
        if (guess == 2):
            score_writer.write("You guessed the winner correctly!", align="center", font=('Arial', 22, 'normal'))
        else:
            score_writer.write("You didn't guess the winner this time.", align="center", font=('Arial', 22, 'normal'))
        return 2 # player 2 wins
    score_writer.write("It was a tie!", align="center", font=('Arial', 22, 'normal'))
    return 0 # in case of tie

'''
Asks user which player they think will win 
@param 
    window: turtle.Screen()
        The screen that will be called to prompt the user 
@returns: int 
    1 if user chose green 
    2 if user chose red
'''
def betting(window) -> int:
    input = window.textinput("Betting", "Which player do you think will win? Green, or Red?").lower()
    while ((input != "green") and (input != "red")):
        input = window.textinput("Betting", "Sorry that wasn't a valid option. Please type either Green or Red.").lower()

    if (input == "green"):
        return 1
    else:
        return 2

def main():
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
    
    target.draw_target(pen, sizes)
    simulate_game(pen, sizes, 10, betting(wn))

    wn.exitonclick()

if __name__ == "__main__":
    main()
