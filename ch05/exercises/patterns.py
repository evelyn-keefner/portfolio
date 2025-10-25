'''
prints an increasing number of stars
@param
    rows : int
        The number of rows to be printed
@returns : None
'''
def star_pyramid(rows) -> None:
    pyramid: str = ''
    for i in range(1, (rows + 1)):
        pyramid += '*'
        print(pyramid)
    return None

'''
prints a decreasing number of stars
@param
    rows : int
        The number of rows to be printed
@returns : None
'''
def rstar_pyramid(rows) -> None:
    pyramid: str = '*' * rows
    for i in range((rows), 0, -1):
        pyramid = pyramid[0:i]
        print(pyramid)
    return None

def main() -> None:
    rows = int(input("How many rows?\n"))
    star_pyramid(rows)
    rstar_pyramid(rows)

if (__name__ == '__main__'):
    main()
