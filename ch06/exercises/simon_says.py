import random
import pygame

def main():
    pygame.init()
    pygame.event.pump()
    screen = pygame.display.set_mode()

    colors = ["red", "blue", "green", "purple"]

    random.shuffle(colors)

    for color in colors:
        screen.fill(color)
        pygame.display.flip()
        pygame.time.wait(500)
        screen.fill("black")
        pygame.display.flip()
        pygame.time.wait(250)

    msg = """
    Your arrow keys correspond to the following colors: 
    UP: red
    DOWN: purple
    LEFT: green
    RIGHT: blue
    Click on the window, enter the sequence, then press <enter> in the console
    """

    input(msg)

if __name__ == '__main__':
    main()
