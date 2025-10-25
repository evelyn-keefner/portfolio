import pygame

# pygame setup
pygame.init()
# keeps window responsive
pygame.event.pump()
# init window to the default size, which is the size of the monitor
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen (switches to next image)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
