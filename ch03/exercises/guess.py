from random import randint

def guess_number_game():
    rand_num: int = randint(1, 10)   
    print("Guess the number from 1 to 10! You are three tries!")
    for i in range(1, 4):
        user_guess: int = int(input(f"Guess number {i}: "))

        if (user_guess == rand_num):
            print("You got it!")
            break

        if (user_guess < rand_num):
            print("Too low!")
        else:
            print("Too high!")

def main():
    guess_number_game()

if (__name__ == "__main__"):
    main()
