import pygame

def initialize_pygame():
    pygame.init() 
    pygame.event.pump() # keeps window responsive

def run_game():
    screen = pygame.display.set_mode() # sets window to default size of the monitor
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black") 

        # RENDER GAME HERE

        # flip() the display to put work onto screen
        pygame.display.flip()

        # limit fps to 60
        clock.tick(60)

    pygame.quit()

def main():
    initialize_pygame()
    run_game()

if __name__ == '__main__':
    main()
