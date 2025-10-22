import pygame

def main():
    pygame.init()
    pygame.event.pump()
    screen = pygame.display.set_mode()
    
    for i in range(3):
        screen.fill("red")
        pygame.display.flip()
        pygame.time.wait(100)
     
        screen.fill("blue")
        pygame.display.flip()
        pygame.time.wait(100)
     
        screen.fill("green")
        pygame.display.flip()
        pygame.time.wait(100)

if __name__ == '__main__':
    main()
