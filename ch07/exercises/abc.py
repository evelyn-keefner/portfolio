from point import Point
from random import Random

def main():
    p1 = Point()
    print(Point)
    print(p1)
    p2 = Point()
    print(f'{p1.x}, {p1.y}, {p1.color}')
    print(f'{p2.x}, {p2.y}, {p2.color}')
    p2.x = 100
    print(f'{p2.x}, {p2.y}, {p2.color}')


if __name__ == '__main__':
    main()
