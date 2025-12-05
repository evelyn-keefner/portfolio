import pygame
import random
from src.experience import Experience

class Enemy(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, health, damage, experience, group, experience_group, type):
        super().__init__(group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.type  = type
        self.image = pygame.image.load(f'assets/sprite/enemy{self.type}_run1.webp')
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2,self.image.get_height()*2))
        self.camera_group = group
        self.experience_group = experience_group
        self.current_time = pygame.time.get_ticks()
        self.rect = self.image.get_rect(center = pos) # image_group needs an image and a rect in order to use it's built in functions draw() and update()
        self.direction = pygame.math.Vector2()
        self.velocity = 2 # how fast character moves
        self.health = health
        self.damage = damage
        self.experience = experience
        self.tracking_range = 500
        self.frame = 0

    def player_direction(self, player):
        player_coords = player.rect.center
        enemy_coords = self.rect.center
        self.direction.x = (player_coords[0] - enemy_coords[0])
        self.direction.y = (player_coords[1] - enemy_coords[1])

    def calculate_distance_tuples(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    '''
    automatically called when the sprite group an enemy object belongs to has the .update() function called on it
    '''
    def update(self, player, image):
        self.frame += 1

        player_distance = self.calculate_distance_tuples(self.rect.center, player.rect.center)
        if player_distance < self.tracking_range:
            # animation handled in main class
            self.image = image
            self.rect.center += self.direction * self.velocity

            if self.frame % 10 == 0:
                self.player_direction(player)
                if self.direction.magnitude() != 0: # magnitude is absolute length of the vector given x and y (a^2 + b^2 = c^2)
                    self.direction = self.direction.normalize() # normalize sets the magnitude to 1, so if two directions are pressed, the vector will be normalized to 1 instead of sqrt(2) 

            if self.frame % 25 == 0:
                if self.direction.x < 0:
                    self.image = pygame.transform.flip(self.image, True, False)

                if self.health <= 0:
                    xp = Experience(self.rect.center, self.camera_group, self.experience) # pos, group, value
                    self.experience_group.add(xp)
                    self.kill()

def main():
    print("Wrong file: please run run python3 main.py")

if __name__ == '__main__':
    main()
