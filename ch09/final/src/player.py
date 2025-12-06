import pygame
import math
from src.weapon import Weapon

class Player(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, camera_group, enemy_group, experience_group, bullet_group):
        super().__init__(camera_group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.image = pygame.image.load('assets/sprite/sprite_run1.webp')
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect(center = pos) # image_group needs an image and a rect in order to use it's built in functions draw() and update()
        self.frames = 0

        # groups
        self.camera_group = camera_group
        self.enemy_group = enemy_group
        self.experience_group = experience_group
        self.bullet_group = bullet_group

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
        self.xp_scaling = 1
        self.level = 1
        self.max_xp = self.max_xp_from_level(self.level)
        self.selection_check = False
        self.selection_queue = 0


        # current time needed for many checks
        self.current_time = pygame.time.get_ticks()

        # damage & health
        self.health = 20
        self.max_health = 20
        self.invulnerable = False
        self.invulnerable_time = 500 # invincibility time in milliseconds (0.5 seconds)
        self.damage_time = 0

        # weapons
        # name, player, fire_delay, damage, radius, count, camera_group, enemy_group, bullet_group
        self.gun = Weapon('gun', self, 500, 5, 0, 1, self.camera_group, self.enemy_group, self.bullet_group)
        self.aura = Weapon('aura', self, 500, 1, 50, 1, self.camera_group, self.enemy_group, self.bullet_group)
        self.active_weapons = [
            self.gun,
        ]

    def max_xp_from_level(self, level) -> int:
        L = 100
        k = 0.1
        o = 50
        return int((L / (1 + math.exp(-k * (level - o)))) * 10)

    def find_nearest_enemy(self, enemy_list):
        if not enemy_list:
            return None
        player_pos = self.rect.center  # Caching the player's position
        return min(
            enemy_list,
            key=lambda enemy: (enemy.rect.centerx - player_pos[0]) ** 2 + (enemy.rect.centery - player_pos[1]) ** 2
        )

    def enemy_vector_normalized(self, enemy):
        enemy_vector_normalized = pygame.math.Vector2()
        player_coords = self.rect.center
        enemy_coords = enemy.rect.center
        enemy_vector_normalized.x = (enemy_coords[0] - player_coords[0])
        enemy_vector_normalized.y = (enemy_coords[1] - player_coords[1])
        if enemy_vector_normalized.magnitude() != 0:
            return enemy_vector_normalized.normalize()
        else:
            return enemy_vector_normalized

    def calculate_distance_tuples(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    '''
    is called in the update() function to get player input before updating the player's direction vector
    '''
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = (keys[pygame.K_d] - keys[pygame.K_a])  # 1 for right, -1 for left
        self.direction.y = (keys[pygame.K_s] - keys[pygame.K_w])  # 1 for down, -1 for up

    '''
    automatically called when the sprite group a player object is contained in has the .update() method called on it
    '''
    def update(self):
        self.frames += 1

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

        if self.frames % 10 == 0:
            # enemy collision to cause damage
            contacted_enemies = pygame.sprite.spritecollide(self, self.enemy_group, False)
            if contacted_enemies and not self.invulnerable:
                self.health -= contacted_enemies[0].damage
                self.damage_time = pygame.time.get_ticks()
                self.invulnerable = True

        # firing weapons
        for weapon in self.active_weapons:
            weapon.update()

        # experience and leveling
        if self.xp < self.max_xp:
            self.selection_check = False
        contacted_experience = pygame.sprite.spritecollide(self, self.experience_group, False)
        if contacted_experience:
            print(f'{self.xp} / {self.max_xp} Level: {self.level}')
            self.xp += (contacted_experience[0].value * self.xp_scaling)
            print(f'{self.xp} / {self.max_xp} Level: {self.level}')
            while self.xp >= self.max_xp:
                self.xp -= self.max_xp
                self.level += 1
                self.max_xp = self.max_xp_from_level(self.level)
                self.selection_check = True
                if self.xp < self.max_xp:
                    pass
                else:
                    self.selection_queue += 1
                print(f'{self.xp} / {self.max_xp} Level: {self.level}')
            contacted_experience[0].kill()

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
