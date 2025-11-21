import pygame
import sys
import time
import random
from src.player import Player
from src.enemy import Enemy
from src.camera import CameraGroup
from src.button import Button
from src.experience import Experience
from src.bullet import Bullet
from src.powerup import Powerup

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
        self.center_x = int(self.window_x / 2)
        self.center_y = int(self.window_y / 2)
        self.center_pos = (self.center_x, self.center_y)
        self.camera_group = CameraGroup()
        self.player_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.menu_button_group = pygame.sprite.Group()
        self.selection_button_group = pygame.sprite.Group()
        self.experience_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        self.powerup_background_image = pygame.image.load("assets/assets_ui/upgrade_ui.webp")
        self.pbi_h, self.pbi_w = self.powerup_background_image.get_size()
        self.powerup_background_image = pygame.transform.scale(self.powerup_background_image, (self.pbi_h * 2, self.pbi_w * 2))

        self.main_player = Player(self.center_pos, self.camera_group, self.enemy_group, self.experience_group, self.bullet_group)

        self.selection_queue = 0

        self.powerup = []
    
    def randomize_powerup_selection(self):
        for selection_button in self.selection_button_group.sprites():
            choice = random.choice(self.powerup)
            if type(choice) != type([]):
                selection_button.text = choice.name
            else:
                sub_choice = random.choice(choice)
                selection_button.text = sub_choice.name

    def run_game(self):
        self.player_group.add(self.main_player)
    
        # Enemy(pos, health, damage, experience, group, experience_group)
        test_enemy = Enemy((0, 0), 20, 1, 700, self.camera_group, self.experience_group)
        self.enemy_group.add(test_enemy)
    
        start_button = Button(self.center_pos, self.menu_button_group, 'assets/assets_ui/start_button.webp', '')
        selection_button1 = Button((self.window_x/2, self.window_y/2+120), self.selection_button_group, 'assets/assets_ui/button.webp', 'PLACEHOLDER TEXT')
        selection_button2 = Button((self.window_x/2, self.window_y/2+20), self.selection_button_group, 'assets/assets_ui/button.webp', 'PLACEHOLDER TEXT')
        selection_button3 = Button((self.window_x/2, self.window_y/2-80), self.selection_button_group, 'assets/assets_ui/button.webp', 'PLACEHOLDER TEXT')

        timer_text = self.font.render("", True, (255,255,225))

        # name, level, increment, is_increment, is_percentage
        gun_powerup = [
            Powerup('Gun Damage', 1, self.main_player.gun.damage, True, True),
            Powerup('Gun Firerate', 1, self.main_player.gun.fire_delay, False, True),
            Powerup('Gun Amount', 1, self.main_player.gun.count, True, False)
        ]
        player_powerup = [
            Powerup('Health', 1, self.main_player.health, True, True),
            Powerup('Speed', 1, self.main_player.velocity, True, True),
            Powerup('XP Gain', 1, self.main_player.xp_scaling, True, True),
        ]
        aura_powerup = {
            Powerup('Aura Radius', 1, self.main_player.aura.radius, True, True),
            Powerup('Aura Damage', 1, self.main_player.aura.damage, True, True),
            Powerup('Aura Rate', 1, self.main_player.aura.fire_delay, False, True),
            Powerup('Aura Frequency', 1, self.main_player.aura.count, True, False)
        }
        self.powerup.append(gun_powerup)
        self.powerup.append(player_powerup)
        self.powerup.append(Powerup('Aura', 0, None, True, True)) # aura check

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
                    self.bullet_group.update()
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

                    if self.main_player.selection_check:
                        self.randomize_powerup_selection()
                        self.state = 'SELECTION'

                elif self.state == 'SELECTION': # in powerup selection screen
                    self.camera_group.custom_draw(self.main_player) # draw background before drawing buttons
                    self.screen.blit(self.powerup_background_image, self.powerup_background_image.get_rect(center = self.center_pos))
                    self.selection_button_group.update() # updates and draws buttons

                    for selection_button in self.selection_button_group.sprites(): # powerup selection
                        if selection_button.pressed == True:

                            if self.main_player.selection_queue > 0:
                                self.main_player.selection_queue -= 1 
                                self.randomize_powerup_selection() 
                                self.state = 'SELECTION'
                                print("again")
                            else:
                                self.state = 'RUNNING'

                elif self.state == 'BAD_END':
                    self.camera_group.custom_draw(self.main_player)

                elif self.state == 'GOOD_END':
                    self.camera_group.custom_draw(self.main_player)
        
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
