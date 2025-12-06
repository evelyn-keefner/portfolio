import pygame
import random
from src.enemy import Enemy

class Spawner():
    def __init__(self, camera_group, enemy_group, experience_group, player):
        self.display_surface = pygame.display.get_surface()
        self.screen_width = self.display_surface.get_width()
        self.screen_height = self.display_surface.get_height()
        self.camera_group = camera_group
        self.enemy_group = enemy_group
        self.experience_group = experience_group
        self.player = player
        self.enemy_type = random.randint(1,2)

        self.scaled_spawning_interval = 5000

        self.scaled_health = 20
        self.scaled_damage = 1
        self.scaled_experience = 3

        self.current_time = pygame.time.get_ticks()
        self.time_last_spawned = 0
        self.current_interval = 5000

        self.spawning_gap = 50
        self.random_position_array = [True, False]

    def timer_scaled_enemy_spawning(self, time):
        '''
        Handles enemy scaling and timing of the game
        args: int
            the time in milliseconds that has passed in the game
        returns: None
        '''
        self.current_time = pygame.time.get_ticks()
        interval = self.current_time - self.time_last_spawned
        if time > 540000: # 9 to end (10 minutes)
            self.current_interval = 100
            self.scaled_experience = 500
        elif time > 480000: # 8 minutes to 9 minutes
            self.current_interval = 250
            self.scaled_experience = 200
        elif time > 450000: # 7.5 minutes to 8 minutes
            self.current_interval = 500
            self.scaled_health = 250
            self.scaled_damage = 5
            self.scaled_experience = 100
        elif time > 300000: # 5 minutes to 7.5 minutes
            self.current_interval = 250 # 2.5 seconds
        elif time > 150000: # 2.5 minutes to 5 minutes
            self.scaled_experience = 50
            self.scaled_health = 100
            self.scaled_damage = 3
            self.current_interval = 500 # 7.5 seconds
        elif time > 120000: # 2 - 2.5 minutes
            self.current_interval = 100
            self.scaled_experience = 20
        elif time > 105000: # 1.75 - 2
            self.current_interval = 250
        elif time > 90000: # 1.5 - 1.75
            self.current_interval = 500
        elif time > 60000: # 1 - 1.5 minutes
            self.scaled_health = 50
            self.scaled_experience = 10
            self.scaled_damage = 2
            self.current_interval = 1000
        elif time > 54000: # 0.9 - 1
            self.current_interval = 250
        elif time > 45000: # 0.75 - 0.9
            self.current_interval = 500
        elif time > 30000: # 0.5 - 0.75
            self.scaled_experience = 5
            self.current_interval = 1000
        elif time > 0: # 0 - 0.5 minutes
            self.current_interval = 2500
        if interval >= self.current_interval:
            self.spawn_enemy()

    def spawn_enemy(self):
        '''
        Creates a new enemy object with proper stats
        args: None
        returns: None
        '''
        self.time_last_spawned = pygame.time.get_ticks()

        position = self.get_random_position()
        # Enemy(pos, health, damage, experience, group, experience_group)
        enemy = Enemy(position, self.scaled_health, self.scaled_damage, self.scaled_experience, self.camera_group, self.experience_group, self.enemy_type)
        self.enemy_group.add(enemy)

    def get_random_position(self) -> tuple:
        '''
        Returns a random position in a ring around the player
        args: None
        returns: (int)
            a tuple with the new position in the format (x, y)
        '''
        player_position = self.player.rect.center
        positive_x = random.choice(self.random_position_array)
        positive_y = random.choice(self.random_position_array)

        if positive_x:
            min_x = player_position[0]
            max_x = ((player_position[0] + int(self.screen_width / 2)) - self.spawning_gap)
        else:
            min_x = ((player_position[0] - int(self.screen_width / 2)) - self.spawning_gap)
            max_x = player_position[0]

        random_x = random.randint(min_x, max_x) + self.spawning_gap

        if positive_y:
            min_y = player_position[1]
            max_y = ((player_position[1] + int(self.screen_height / 2)) - self.spawning_gap)
        else:
            min_y = ((player_position[1] - int(self.screen_height / 2)) - self.spawning_gap)
            max_y = player_position[1]

        random_y = random.randint(min_y, max_y) + self.spawning_gap

        return (random_x, random_y)

def main():
    print("Wrong file: please run run python3 main.py")

if __name__ == '__main__':
    main()
