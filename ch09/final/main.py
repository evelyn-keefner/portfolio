import pygame
import sys
import player

def initialize_pygame():
    GAME_TITLE = "The Great Emu War"
    pygame.init() 
    pygame.event.pump() # keeps window responsive
    pygame.display.set_caption(GAME_TITLE)

def run_game():
    screen = pygame.display.set_mode() # sets window to default size of the monitor
    clock = pygame.time.Clock()
    
    window_x, window_y = screen.get_size()
    x = int(window_x / 2)
    y = int(window_y / 2)
    pos = (x, y)

    camera_group = pygame.sprite.Group() # sprite group to handle all sprites

    main_player = player.Player(pos, camera_group)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill("beige") # fills screen to a set background color

        camera_group.update() # calls update() on every sprite within the group
        camera_group.draw(screen) # draws every sprite within the camera_group to the screen

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
