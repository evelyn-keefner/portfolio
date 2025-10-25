'''
raises a number to a power
@param
    a : int
        the base number
    pow : int
        the exponent
@returns : int
'''
def exponentiate(a, pow) -> int:
    result: int = a
    for i in range(pow - 1):
        result *= a
    return result

'''
returns the value of the input squared
@param:
    a : int
        number to be squared
@returns : int
    squared value of input
'''
def square(a: int) -> int:
    return exponentiate(a, 2)

'''
multiplies two numbers together
@param: 
    a : int
        first number
    b : int
        second number
@returns : int
    product of multiplication
''' 
def multiply(a: int, b: int) -> int:
    sum: int = 0
    for i in range(b):
        sum += a
    return sum

def main() -> None:
    print(multiply(5, 100))
    print(exponentiate(3, 3))
    print(square(6))

if (__name__ == '__main__'):
    main()
