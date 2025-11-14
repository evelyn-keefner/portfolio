import pygame
import sys
import time
from src.player import Player
from src.enemy import Enemy
from src.camera import CameraGroup
from src.button import Button
from src.experience import Experience

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
    selection_button_group = pygame.sprite.Group()
    experience_group = pygame.sprite.Group()
    
    main_player = Player(pos, camera_group, enemy_group, experience_group)
    player_group.add(main_player)
    
    # REMOVE ME! KILL ME END MY SUFFERING
    # Enemy(pos, health, damage, experience, group, experience_group)
    test_enemy = Enemy((0, 0), 20, 1, 700, camera_group, experience_group)
    enemy_group.add(test_enemy)
    
    start_button = Button(pos, menu_button_group, 'assets/placeholder_assets/small_button.png', 'START')
    selection_button1 = Button((100, 100), selection_button_group, 'assets/placeholder_assets/small_button.png', 'PLACEHOLDER TEXT')
    selection_button2 = Button((200, 200), selection_button_group, 'assets/placeholder_assets/small_button.png', 'PLACEHOLDER TEXT')
    selection_button3 = Button((300, 300), selection_button_group, 'assets/placeholder_assets/small_button.png', 'PLACEHOLDER TEXT')
    
    selection_queue = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill("beige") # fills screen to a set background color
        
        if state == 'START':
            # any buttons don't need to be drawn, update() also handles drawing
            menu_button_group.update()
            if start_button.pressed:
                state = 'RUNNING'

        elif state == 'RUNNING' or state == 'SELECTION':
            if state != 'SELECTION': # main game loop
                # update every group that contains a sprite
                enemy_group.update(main_player)
                player_group.update()
                camera_group.custom_draw(main_player) 
                test_enemy.health -= 1 # remove me

                if main_player.selection_check:
                    state = 'SELECTION'
            elif state == 'SELECTION': # in powerup selection screen
                camera_group.custom_draw(main_player) # draw background before drawing buttons
                selection_button_group.update()
                for selection_button in selection_button_group.sprites():
                    if selection_button.pressed == True:
                        if selection_button.text == 'example powerup':
                            print("do thing")
                        elif selection_button.text == 'other powerup':
                            print("do other thing")
                        else:
                            print("powerup not given, error")
                            if main_player.selection_queue > 0:
                                main_player.selection_queue -= 1 
                                state = 'SELECTION'
                                print("again")
                            else:
                                state = 'RUNNING'
        
        pygame.display.update()

        # limit fps to 60
        clock.tick(60)

    pygame.quit()

def main():
    initialize_pygame()
    run_game()

if __name__ == '__main__':
    main()
