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
        if name == 'gun':
            self.gun()
        elif name == 'aura':
            self.aura()

    def calculate_distance_tuples(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def gun(self):
        if self.enemy_group.sprites():
            nearest_enemy = self.player.find_nearest_enemy(self.enemy_group.sprites())
            if self.calculate_distance_tuples(self.player.rect.center, nearest_enemy.rect.center) <= 500:
                if nearest_enemy:
                    bullet = Bullet(self.player.rect.center, self.player.enemy_vector_normalized(nearest_enemy), self.damage, self.camera_group, self.bullet_group, self.enemy_group)

    def aura(self):
        pass
        # aura = Aura(self.position, self )

def main() -> None:
    pass

if __name__ == '__main__':
    main()
