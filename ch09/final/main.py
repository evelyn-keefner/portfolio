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
from src.spawner import Spawner

class Game:

    def __init__(self):
        self.state = 'START'
        self.screen = pygame.display.set_mode()
        self.clock = pygame.time.Clock()
        self.game_time = 600000
        self.current_time = 0
        self.timer_time = 0
        self.time_update_check = True
        self.font = pygame.font.Font('assets/PokemonGb-RAeo.ttf', 15)
        self.window_x, self.window_y = self.screen.get_size()
        self.center_x = int(self.window_x / 2)
        self.center_y = int(self.window_y / 2)
        self.center_pos = (self.center_x, self.center_y)
        self.camera_group = CameraGroup()
        self.player_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.menu_button_group = pygame.sprite.Group()
        self.selection_button_group = pygame.sprite.Group()
        self.end_button_group = pygame.sprite.Group()
        self.experience_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        self.powerup_background_image = pygame.image.load("assets/assets_ui/upgrade_ui.webp")
        self.pbi_h, self.pbi_w = self.powerup_background_image.get_size()
        self.powerup_background_image = pygame.transform.scale(self.powerup_background_image, (self.pbi_h * 2, self.pbi_w * 2))

        self.main_player = Player(self.center_pos, self.camera_group, self.enemy_group, self.experience_group, self.bullet_group)

        self.enemy_spawner = Spawner(self.camera_group, self.enemy_group, self.experience_group, self.main_player)

        self.selection_queue = 0

        self.powerup = {}

        # unified enemy animation
        self.enemy_run = []
        self.frame_current = 0
        self.frame_speed = 150
        self.frame_next = False
        self.frame_num = 0
        for i in range(4):
            self.enemy_run.append(pygame.image.load(f'assets/sprite/enemy{self.enemy_spawner.enemy_type}_run{i+1}.webp'))

    def get_enemy_animation(self) :
        if (self.current_time - self.frame_current) > self.frame_speed:
            self.frame_next = False
            self.frame_num += 1
            if self.frame_num > 3:
                self.frame_num = 0

        if self.frame_next == False:
            self.frame_next = True
            self.frame_current = pygame.time.get_ticks()
        
        if self.enemy_spawner.enemy_type == 1:
            return pygame.transform.scale(self.enemy_run[self.frame_num], (60,60))
        else:
            return pygame.transform.scale(self.enemy_run[self.frame_num], (60,120))

    def randomize_powerup_selection(self):
        for selection_button in self.selection_button_group.sprites():
            keys = list(self.powerup.keys())
            choice = random.choice(keys)
            selection_button.text = choice

    def run_game(self):
        self.player_group.add(self.main_player)

        start_button = Button((self.window_x/2, self.window_y/2+200), self.menu_button_group, 'assets/assets_ui/start_button.webp', '')
        start_background = pygame.image.load('assets/assets_ui/start_screen.webp')
        start_background = pygame.transform.scale(start_background, (start_background.get_width()*3, start_background.get_height()*3))
        selection_button1 = Button((self.window_x/2, self.window_y/2+120), self.selection_button_group, 'assets/assets_ui/button.webp', 'PLACEHOLDER TEXT')
        selection_button2 = Button((self.window_x/2, self.window_y/2+20), self.selection_button_group, 'assets/assets_ui/button.webp', 'PLACEHOLDER TEXT')
        selection_button3 = Button((self.window_x/2, self.window_y/2-80), self.selection_button_group, 'assets/assets_ui/button.webp', 'PLACEHOLDER TEXT')
        exit_game_button = Button((self.center_x, self.center_y), self.end_button_group, 'assets/assets_ui/button.webp', 'Exit?')
        reset_button = Button((self.center_x, self.center_y + 100), self.end_button_group, 'assets/assets_ui/button.webp', 'Retry?')
        timer_text = self.font.render("", True, (255,255,225))

        # name, level, increment, is_increment, is_percentage
        gun_powerup = {
            "Gun Damage":Powerup('Gun Damage', 1, "damage", True, True, self.main_player.gun),
            "Gun Firerate":Powerup('Gun Firerate', 1, "fire_delay", False, True, self.main_player.gun),
            "Gun Amount":Powerup('Gun Amount', 1, "count", True, False, self.main_player.gun)
        }
        player_powerup = {
            "Health":Powerup('Health', 1, "max_health", True, True, self.main_player),
            "Speed":Powerup('Speed', 1, "velocity", True, True, self.main_player),
            "XP Gain":Powerup('XP Gain', 1, "xp_scaling", True, True, self.main_player)
        }

        # unused 
        aura_powerup = {
            "Aura Radius":Powerup('Aura Radius', 1, "radius", True, True, self.main_player.aura),
            "Aura Damage":Powerup('Aura Damage', 1, "damage", True, True, self.main_player.aura),
            "Aura Rate":Powerup('Aura Rate', 1, "fire_delay", False, True, self.main_player.aura),
            "Aura Frequency":Powerup('Aura Frequency', 1, "count", True, False, self.main_player.aura)
        }

        self.powerup.update(gun_powerup)

        self.powerup.update(player_powerup)

        # self.powerup.update({"Aura":Powerup('Aura', 0, None, True, True, self.main_player.aura)}) # aura check

        while True:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(start_background, (self.window_x/2 - 720, self.window_y/2 - 400))
            intruction_text1 = self.font.render('Press start to begin.', True, (255, 255, 255))
            instruction_text2 = self.font.render('Use WASD to move.', True, (255, 255, 255))
            self.screen.blit(intruction_text1,(100,250))
            self.screen.blit(instruction_text2,(100,300))

            if self.state == 'START':
                # any buttons don't need to be drawn, update() also handles drawing
                self.menu_button_group.update()
                instruction_text = self.font.render(f'Press Start then use WASD to control your character!', True, (0, 0, 0))
                self.screen.blit(instruction_text, (self.center_x, self.center_y))
                if start_button.pressed:
                    self.state = 'RUNNING'
            elif self.state == 'RUNNING' or self.state == 'SELECTION':
                if self.state != 'SELECTION': # main game loop
                    game_time_from_zero = 600000 - self.game_time
                    self.enemy_spawner.timer_scaled_enemy_spawning(game_time_from_zero)

                    # update every group that contains a sprite
                    self.player_group.update()
                    self.enemy_group.update(self.main_player, self.get_enemy_animation())
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

                    timer_text = self.font.render(f'Time: {self.game_time / 1000}', True, (0, 0, 0))
                    self.screen.blit(timer_text,(100,100))

                    # health amount
                    health_text = self.font.render(f'Health: {int(self.main_player.health)} / {int(self.main_player.max_health)}', True, (0, 0, 0))
                    self.screen.blit(health_text,(100,150))
                    # firerate
                    firerate_text = self.font.render(f'Firerate: {round(self.main_player.gun.fire_delay, 2)}ms', True, (0, 0, 0))
                    self.screen.blit(firerate_text,(100,250))
                    # damage
                    damage_text = self.font.render(f'Damage: {round(self.main_player.gun.damage, 2)}', True, (0, 0, 0))
                    self.screen.blit(damage_text,(100,300))
                    # speed
                    speed_text = self.font.render(f'Speed: {round(self.main_player.velocity, 2)}', True, (0, 0, 0))
                    self.screen.blit(speed_text,(100,350))
                    # xp
                    xp_text = self.font.render(f'XP: {round(self.main_player.xp, 2)}/{int(self.main_player.max_xp)}', True, (0, 0, 0))
                    self.screen.blit(xp_text,(100,200))
                    # xp scaling
                    xp_scaling_text = self.font.render(f'XP Scaling: {round(self.main_player.xp_scaling, 2)}x', True, (0, 0, 0))
                    self.screen.blit(xp_scaling_text,(100,400))
                    # gun amount
                    gun_amount_text = self.font.render(f'Gun Amount: {self.main_player.gun.count}', True, (0, 0, 0))
                    self.screen.blit(gun_amount_text,(100,450))
                    
                    if self.main_player.health <= 0:
                        self.state = 'BAD_END'
                        print("BAD ENDING")
                    
                    if self.game_time < 0:
                        self.state = 'GOOD_END'

                    if self.main_player.selection_check:
                        self.randomize_powerup_selection()
                        self.state = 'SELECTION'

                elif self.state == 'SELECTION': # in powerup selection screen
                    self.camera_group.custom_draw(self.main_player) # draw background before drawing buttons
                    self.screen.blit(self.powerup_background_image, self.powerup_background_image.get_rect(center = self.center_pos))
                    self.selection_button_group.update() # updates and draws buttons

                    for selection_button in self.selection_button_group.sprites(): # powerup selection
                        if selection_button.pressed == True:
                            # giving powerup
                            current_powerup = self.powerup[selection_button.text]
                            current_powerup_check = current_powerup.give_powerup()
                            if current_powerup_check == "Aura":
                                del self.powerup['Aura']
                                self.powerup.update(aura_powerup)
                                print('aura removed & powerups added')

                            # handles overflow xp
                            if self.main_player.selection_queue > 0:
                                self.main_player.selection_queue -= 1
                                self.randomize_powerup_selection()
                                self.state = 'SELECTION'
                            else:
                                self.state = 'RUNNING'

            elif self.state == 'BAD_END':
                self.camera_group.custom_draw(self.main_player)
                bad_end_text = self.font.render(f'You lost! You reached level {self.main_player.level}', True, (0, 0, 0))
                self.screen.blit(bad_end_text, (self.center_x - 200, self.center_y - 100))
                self.end_button_group.update()
                if reset_button.pressed == True:
                    self.game_time = 600000
                    enemies = self.enemy_group.sprites()
                    for enemy in enemies:
                        enemy.kill()
                    self.player_group.remove(self.main_player)
                    self.main_player.kill()
                    self.main_player = Player(self.center_pos, self.camera_group, self.enemy_group, self.experience_group, self.bullet_group)
                    self.player_group.add(self.main_player)
                    self.state = 'START'

                if exit_game_button.pressed == True:
                    pygame.quit()

            elif self.state == 'GOOD_END':
                self.camera_group.custom_draw(self.main_player)
                good_end_text = self.font.render(f'You won! You reached level {self.main_player.level}', True, (0, 0, 0))
                self.screen.blit(good_end_text, (self.center_x - 200, self.center_y - 100))
                self.end_button_group.update()

                if reset_button.pressed == True:
                    self.game_time = 600000
                    enemies = self.enemy_group.sprites()
                    for enemy in enemies:
                        enemy.kill()
                    self.player_group.remove(self.main_player)
                    self.main_player.kill()
                    self.main_player = Player(self.center_pos, self.camera_group, self.enemy_group, self.experience_group, self.bullet_group)
                    self.player_group.add(self.main_player)
                    self.state = 'START'

                if exit_game_button.pressed == True:
                    pygame.quit()

            pygame.display.update()

            # limit fps to 60
            self.clock.tick(60)

        pygame.quit()

def initialize_pygame():
    GAME_TITLE = "Swarm Computing"
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
