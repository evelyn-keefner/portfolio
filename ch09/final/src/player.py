import pygame
import math
from src.bullet import Bullet

class Player(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, camera_group, enemy_group, experience_group):
        super().__init__(camera_group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.image = pygame.image.load('assets/sprite/sprite_run1.webp')
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect(center = pos) # image_group needs an image and a rect in order to use it's built in functions draw() and update()
        
        # groups
        self.camera_group = camera_group
        self.enemy_group = enemy_group
        self.experience_group = experience_group

        # animation
        self.player_sprite_run = []
        self.player_sprite_idle = []
        self.frame_speed = 150 # milliseconds per frame
        self.frame_current = 0
        self.frame_next = False
        self.frame_num = 0
        for i in range(4):
            self.player_sprite_idle.append(pygame.image.load(f'assets/sprite/sprite_idle{i+1}.webp'))
            self.player_sprite_run.append(pygame.image.load(f'assets/sprite/sprite_run{i+1}.webp'))

        # movement
        self.direction = pygame.math.Vector2()
        self.velocity = 5 # how fast character moves
        
        # leveling
        self.xp = 0
        self.level = 1
        self.max_xp = self.max_xp_from_level(self.level)
        self.selection_check = False
        self.selection_queue = 0

        
        # current time needed for many checks
        self.current_time = pygame.time.get_ticks()

        # damage & health
        self.health = 20
        self.invulnerable = False
        self.invulnerable_time = 500 # invincibility time in milliseconds (0.5 seconds)
        self.damage_time = 0

        # gun and bullets
        self.fire_delay = 500 # 0.5 seconds in milliseconds
        self.fire_check = False
        self.fire_time = 0 # time since last bullet fired
        
    def max_xp_from_level(self, level) -> int:
        L = 100 
        k = 0.1
        o = 50
        return int((L / (1 + math.exp(-k * (level - o)))) * 10)

    def enemy_vector_normalized(self, enemy):
        enemy_vector_normalized = pygame.math.Vector2()
        player_coords = self.rect.center 
        enemy_coords = enemy.rect.center
        enemy_vector_normalized.x = (player_coords[0] - enemy_coords[0])
        enemy_vector_normalized.y = (player_coords[1] - enemy_coords[1])
        return enemy_vector_normalized.normalize()

    ''' 
    is called in the update() function to get player input before updating the player's direction vector
    '''
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # left
            self.direction.x = -1
        elif keys[pygame.K_d]: # right
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_w]: # up
            self.direction.y = -1
        elif keys[pygame.K_s]: # down
            self.direction.y = 1
        else:
            self.direction.y = 0
    
    '''
    automatically called when the sprite group a player object is contained in has the .update() method called on it
    '''
    def update(self):
        # movement 
        keys = pygame.key.get_pressed() # for distinguishing run animation from idle animation
        self.input()
        if self.direction.magnitude() != 0: 
            self.direction = self.direction.normalize() 
            self.rect.center += self.direction * self.velocity # rect.center is a tuple and vector2's are compatable with operations involving tuples'
        
        # invulnerability frames
        self.current_time = pygame.time.get_ticks()
        if (self.current_time - self.damage_time) > self.invulnerable_time:
            self.invulnerable = False
        
        # enemy collision to cause damage
        contacted_enemies = pygame.sprite.spritecollide(self, self.enemy_group, False)
        if contacted_enemies and not self.invulnerable:
            self.health -= contacted_enemies[0].damage
            self.damage_time = pygame.time.get_ticks()
            self.invulnerable = True
            print(f'Player Health: {self.health}')

        # firing gun
        

        # experience and leveling
        if self.xp < self.max_xp:
            self.selection_check = False
        contacted_experience = pygame.sprite.spritecollide(self, self.experience_group, False)
        if contacted_experience:
            print(f'{self.xp} / {self.max_xp} Level: {self.level}')
            self.xp += contacted_experience[0].value
            print(f'{self.xp} / {self.max_xp} Level: {self.level}')
            while self.xp >= self.max_xp:
                self.xp -= self.max_xp
                self.level += 1
                self.max_xp = self.max_xp_from_level(self.level)
                self.selection_check = True
                self.selection_queue += 1
                if self.xp < self.max_xp:
                    self.xp = 0
                print(f'{self.xp} / {self.max_xp} Level: {self.level}')
            self.camera_group.remove(contacted_experience[0])
            self.experience_group.remove(contacted_experience[0])

        # animation handling
        if (self.current_time - self.frame_current) > self.frame_speed:
            self.frame_next = False
            self.frame_num += 1
            if self.frame_num > 3:
                self.frame_num = 0
        if self.frame_next == False:
            self.frame_next = True
            self.frame_current = pygame.time.get_ticks()
            if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
                self.image = self.player_sprite_run[self.frame_num]
                self.image = pygame.transform.scale(self.image, (60,60))
                if self.direction.x < 0:
                    self.image = pygame.transform.flip(self.image, True, False)
            else:
                self.image = self.player_sprite_idle[self.frame_num]
                self.image = pygame.transform.scale(self.image, (60,60))

def main():
    print("Wrong file: please run run python3 main.py")

if __name__ == '__main__':
    main()
