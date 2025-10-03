from random import randint

'''
simulates a number guessing game in the terminal
@param
    max: int
    Sets the range of numbers to be randomly chosen from. The range will be set to a value of 1 to max
'''
def guess_number_game(max):
    rand_num: int = randint(1, max)   
    print(f"The minimum number of tries you can realistically get this in is {binary_search_maximum(rand_num, max)} guesses")
    print(f"Guess the number from 1 to {max}! You are three tries!")
    user_guess: int = 0
    count: int = 0
    while (user_guess != rand_num):
        count += 1
        user_guess: int = int(input(f"Guess number {count}: "))

        if (user_guess < rand_num):
            print("Too low!")
        elif (user_guess > rand_num):
            print("Too high!")
        else:
            print(f"The secret number was {rand_num} and you got it in {count} guesses!")

'''
runs through binary search and returns how many interations it takes to find a certain number
@param
    num: int
        The number that is being searched for in the binary search
    max: int
        The maximum number of values in the binary search, the function takes the entire range of values of 1 to this maximum
@returns: int
    the number of interations it will take to find a number over the range of 1 to the max
'''
def binary_search_maximum(num, max) -> int:
    lower: int = 1
    upper: int = max
    guess: int = max // 2
    count: int = 0

    while (guess != num):
        count += 1
        if (guess < num):
            lower = guess    
        elif (guess > num):
            upper = guess

        guess = (upper + lower) // 2

    return count + 1

def main():
    guess_number_game(1000)
    

if (__name__ == "__main__"):
    main()
