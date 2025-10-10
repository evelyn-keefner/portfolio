def star_pyramid(rows):
    pyramid = ''
    for i in range(1, (rows + 1)):
        pyramid += '*'
        print(pyramid)
    return None

def rstar_pyramid(rows):
    pyramid = '*' * rows
    for i in range((rows), 0, -1):
        pyramid = pyramid[0:i]
        print(pyramid)
    return None

def main():
    rows = int(input("How many rows?\n"))
    star_pyramid(rows)
    rstar_pyramid(rows)

if (__name__ == '__main__'):
    main()
