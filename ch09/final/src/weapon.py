import pygame
from src.bullet import Bullet
from src.aura import Aura

class Weapon:
    def __init__(self, name, player, fire_delay, damage, radius, count, camera_group, enemy_group, bullet_group):
        self.current_time = pygame.time.get_ticks()
        self.name = name
        self.player = player
        self.fire_delay = fire_delay
        self.fire_check = False
        self.fire_time = 0
        self.damage = damage
        self.radius = radius
        self.count = count
        self.camera_group = camera_group
        self.enemy_group = enemy_group
        self.bullet_group = bullet_group

    def update(self):
        self.current_time = pygame.time.get_ticks()
        adjusted_fire_delay = self.fire_delay / self.count
        if (self.current_time - self.fire_time) > adjusted_fire_delay:
            self.fire_check = True
        if (self.fire_check):
            self.fire_check = False
            self.fire_time = pygame.time.get_ticks()
            self.fire(self.name)

    def fire(self, name):
        '''
        Calls proper method based on name
        args: str
            name of weapon
        returns: None
        '''
        if name == 'gun':
            self.gun()
        elif name == 'aura':
            self.aura()

    def calculate_distance_tuples(self, pos1, pos2):
        '''
        returns the absolute distance between two coordinate pair values
        args:
            (int)
                tuple of first position
            (int)
                tuple of second position
        returns: None
        ''' 
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def enemy_vector_normalized(self, enemy):
        '''
        returns a vector normalized to 1 that points in the direction of the enemy based off of player position
        args: pygame.sprite
            the enemy
        returns: pygame.math.Vector2
            a vector pointin to the enemy 
        '''
        enemy_vector_normalized = pygame.math.Vector2()
        player_coords = self.player.rect.center
        enemy_coords = enemy.rect.center
        enemy_vector_normalized.x = (enemy_coords[0] - player_coords[0])
        enemy_vector_normalized.y = (enemy_coords[1] - player_coords[1])
        if enemy_vector_normalized.magnitude() != 0:
            return enemy_vector_normalized.normalize()
        else:
            return enemy_vector_normalized

    def gun(self):
        '''
        creates a bullet object
        args: None
        returns: None
        '''
        if self.enemy_group.sprites():
            nearest_enemy = self.player.find_nearest_enemy(self.enemy_group.sprites())
            if self.calculate_distance_tuples(self.player.rect.center, nearest_enemy.rect.center) <= 500:
                if nearest_enemy:
                    bullet = Bullet(self.player.rect.center, self.enemy_vector_normalized(nearest_enemy), self.damage, self.camera_group, self.bullet_group, self.enemy_group)

    def aura(self):
        pass
        # aura = Aura(self.position, self )

def main() -> None:
    pass

if __name__ == '__main__':
    main()
