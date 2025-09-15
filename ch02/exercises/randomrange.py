import random

'''
Generates specified amount of random numbers across a specified range to print out.
parameters
---------- 
low: int
    bottom limit for random number generation 
high: int 
    upper limit for random number generation 
num_numbers: 
    the amount of numbers to be printed over the range specified by low and high 
'''
def generate_random_numbers(low, high, num_numbers):
    for i in range(num_numbers):
        generated_number = random.randint(low, high)
        print(f"Random number {i + 1}: {generated_number}")

try:
    print("Please enter two numbers, a low and a high limit within which you want to generate random numbers between.")
    low = int(input("Low: "))
    high = int(input("High: "))
    print("Please enter how many random numbers you want to generate.")
    num_numbers = int(input("Total numbers: "))

    generate_random_numbers(low, high, num_numbers)
except:
    print("There was an error please try again.")
