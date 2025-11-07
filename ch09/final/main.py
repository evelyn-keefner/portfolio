import pygame
import sys
from src.player import Player
from src.enemy import Enemy
from src.camera import CameraGroup
from src.button import Button

def initialize_pygame():
    GAME_TITLE = "The Great Emu War"
    pygame.init() 
    pygame.font.init()
    pygame.event.pump() # keeps window responsive
    pygame.display.set_caption(GAME_TITLE)

def running_status():
    return 'RUNNING'
    print('running test ok')

def run_game():
    screen = pygame.display.set_mode() # sets window to default size of the monitor
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('arial', 36)
    state = 'START'

    window_x, window_y = screen.get_size()
    x = int(window_x / 2)
    y = int(window_y / 2)
    pos = (x, y)
    
    camera_group = CameraGroup() # sprite group to handle all sprites every sprite must be added into this group
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    menu_button_group = pygame.sprite.Group()
    
    main_player = Player(pos, camera_group)
    player_group.add(main_player)
    
    # REMOVE ME! KILL ME END MY SUFFERING
    test_enemy = Enemy((0, 0), camera_group)
    enemy_group.add(test_enemy)
    
    start_button = Button(pos, menu_button_group)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill("beige") # fills screen to a set background color
        
        if state == 'START':
            menu_button_group.update()
            menu_button_group.draw(screen)
            if start_button.pressed:
                state = 'RUNNING'

        elif state == 'RUNNING':
            # update every group that contains a sprite
            enemy_group.update(main_player)
            player_group.update(enemy_group)
        
            # camera group contains all sprites, handles all drawing including the ground, enemies and player
            camera_group.custom_draw(main_player) 

        # update() the display to put work onto screen
        pygame.display.update()

        # limit fps to 60
        clock.tick(60)

    pygame.quit()

def main():
    initialize_pygame()
    run_game()

if __name__ == '__main__':
    main()
