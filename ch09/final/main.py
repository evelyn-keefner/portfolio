import pygame
import sys
import time
from src.player import Player
from src.enemy import Enemy
from src.camera import CameraGroup
from src.button import Button
from src.experience import Experience
from src.bullet import Bullet

class Game:
    
    def __init__(self):
        self.state = 'START'
        self.screen = pygame.display.set_mode()
        self.clock = pygame.time.Clock()
        self.game_time = 600000
        self.current_time = 0
        self.timer_time = 0
        self.time_update_check = True 
        self.font = pygame.font.SysFont('arial', 36)
        self.window_x, self.window_y = self.screen.get_size()
        self.x = int(self.window_x / 2)
        self.y = int(self.window_y / 2)
        self.pos = (self.x, self.y)
        self.camera_group = CameraGroup()
        self.player_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.menu_button_group = pygame.sprite.Group()
        self.selection_button_group = pygame.sprite.Group()
        self.experience_group = pygame.sprite.Group()

        self.powerup_background_image = pygame.image.load("assets/assets_ui/upgrade_ui.webp")
        self.pbi_h, self.pbi_w = self.powerup_background_image.get_size()
        self.powerup_background_image = pygame.transform.scale(self.powerup_background_image, (self.pbi_h * 2, self.pbi_w * 2))

        self.main_player = Player(self.pos, self.camera_group, self.enemy_group, self.experience_group)

        self.selection_queue = 0

    def run_game(self):
        self.player_group.add(self.main_player)
    
        # Enemy(pos, health, damage, experience, group, experience_group)
        test_enemy = Enemy((0, 0), 20, 1, 700, self.camera_group, self.experience_group)
        self.enemy_group.add(test_enemy)
    
        start_button = Button(self.pos, self.menu_button_group, 'assets/assets_ui/start_button.webp', '')
        selection_button1 = Button((self.window_x/2, self.window_y/2+75), self.selection_button_group, 'assets/placeholder_assets/small_button.png', 'PLACEHOLDER TEXT')
        selection_button2 = Button((self.window_x/2, self.window_y/2), self.selection_button_group, 'assets/placeholder_assets/small_button.png', 'PLACEHOLDER TEXT')
        selection_button3 = Button((self.window_x/2, self.window_y/2-125), self.selection_button_group, 'assets/placeholder_assets/small_button.png', 'PLACEHOLDER TEXT')


        timer_text = self.font.render("hello, gamers!", True, (255,255,225))

        while True:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("beige") # fills screen to a set background color
        
            if self.state == 'START':
                # any buttons don't need to be drawn, update() also handles drawing
                self.menu_button_group.update()
                if start_button.pressed:
                    self.state = 'RUNNING'

            elif self.state == 'RUNNING' or self.state == 'SELECTION':
                if self.state != 'SELECTION': # main game loop
                    # update every group that contains a sprite
                    self.enemy_group.update(self.main_player)
                    self.player_group.update()
                    self.camera_group.custom_draw(self.main_player) 
                    
                    # timer 
                    self.current_time = pygame.time.get_ticks()
                    if self.current_time - self.timer_time >= 100:
                        self.time_update_check = True
                        self.game_time -= 100
                    if self.time_update_check:
                        self.timer_time = pygame.time.get_ticks()
                        self.time_update_check = False
                    timer_text = self.font.render(str(self.game_time / 1000), True, (0, 0, 0))
                    self.screen.blit(timer_text,(100,100))
                    
                    test_enemy.health -= 1

                    if self.main_player.selection_check:
                        self.state = 'SELECTION'

                elif self.state == 'SELECTION': # in powerup selection screen
                    self.camera_group.custom_draw(self.main_player) # draw background before drawing buttons
                    self.screen.blit(self.powerup_background_image, self.powerup_background_image.get_rect(center = self.pos))
                    self.selection_button_group.update() # updates and draws buttons
                    for selection_button in self.selection_button_group.sprites():
                        if selection_button.pressed == True:
                            if selection_button.text == 'example powerup':
                                print("do thing")
                            elif selection_button.text == 'other powerup':
                                print("do other thing")
                            else:
                                print("powerup not given, error")
                                if self.main_player.selection_queue > 0:
                                    self.main_player.selection_queue -= 1 
                                    self.state = 'SELECTION'
                                    print("again")
                                else:
                                    self.state = 'RUNNING'
        
            pygame.display.update()

            # limit fps to 60
            self.clock.tick(60)

        pygame.quit()

def initialize_pygame():
    GAME_TITLE = "The Great Emu War"
    pygame.init() 
    pygame.font.init()
    pygame.event.pump() # keeps window responsive
    pygame.display.set_caption(GAME_TITLE)

def main():
    initialize_pygame()
    game = Game()
    game.run_game() 

if __name__ == '__main__':
    main()
