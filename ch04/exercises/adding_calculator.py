'''
asks user for integers and adds them together, returning their sum
@returns: int
    the sum of all entered integers
'''
def get_sum() -> int:
    sum = 0
    while (True):
        value = input(':')
        if (value.isdigit()):
            value = int(value)
            sum += value 
        elif (value != 'q'):
            print("not a valid number please try again")
        else:
            return sum

def main():
    print("Please enter a series of numbers to sum ['q' to quit]:")
    print(f"Your sum is {get_sum()}")

if (__name__ == '__main__'):
    main()
