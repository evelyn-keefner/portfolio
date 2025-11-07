import pygame
import sys
from src.player import Player
from src.enemy import Enemy
from src.camera import CameraGroup
from src.button import Button

class Game:
    def __init__(self):
        self.state = 'START'
        
        self.screen = pygame.display.set_mode()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 36)
        self.game_title = 'game1'

    def run_game(self):
        window_x, window_y = self.screen.get_size()
        x = int(window_x / 2)
        y = int(window_y / 2)
        pos = (x, y)

        camera_group = CameraGroup() # sprite group to handle all sprites every sprite must be added into this group
        player_group = pygame.sprite.Group()
        enemy_group = pygame.sprite.Group()
        button_group = pygame.sprite.Group()
    
        main_player = Player(pos, camera_group)
        player_group.add(main_player)
    
        # REMOVE ME! KILL ME END MY SUFFERING
        test_enemy = Enemy((0, 0), camera_group)
        enemy_group.add(test_enemy)
    
        start_button = Button((100, 100), running_status, button_group)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            self.screen.fill("beige") # fills screen to a set background color
        
            if self.state == 'START':
                button_group.update()
                button_group.draw(self.screen)
                if start_button.pressed == True:
                    self.state == 'RUNNING'

            elif self.state == 'RUNNING':
                # update every group that contains a sprite
                enemy_group.update(main_player)
                player_group.update()
        
                # camera group contains all sprites, handles all drawing including the ground, enemies and player
                camera_group.custom_draw(main_player) 

            # update() the display to put work onto screen
            pygame.display.update()

            # limit fps to 60
            self.clock.tick(60)

        pygame.quit()

def main():
    GAME_TITLE = 'GAME'
    pygame.init()
    pygame.font.init()
    pygame.event.pump()
    pygame.display.set_caption(GAME_TITLE)
    game = Game()   
    game.run_game()
    #initialize_pygame()
    #run_game()

if __name__ == '__main__':
    main()
