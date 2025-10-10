def square(a: int, pow: int) -> int:
    return multiply(a, a)

def multiply(a: int, b: int) -> int:
    sum: int = 0
    for i in range(b):
        sum += a
    return sum

def main():
    print(multiply(5, 100))
    print(square(6, 2))

if (__name__ == '__main__'):
    main()
