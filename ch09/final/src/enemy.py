import pygame
from src.experience import Experience 

class Enemy(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, health, damage, experience, group, experience_group):
        super().__init__(group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.image = pygame.image.load('assets/sprite/enemy2_run1.webp')
        self.image = pygame.transform.scale(self.image, (60,120))        
        self.camera_group = group
        self.experience_group = experience_group
        self.enemy_run = []
        self.frame_speed = 150 # milliseconds per frame
        self.frame_current = 0
        self.frame_next = False
        self.current_time = pygame.time.get_ticks()
        self.frame_num = 0
        for i in range(4):
            self.enemy_run.append(pygame.image.load(f'assets/sprite/enemy2_run{i+1}.webp'))
        self.rect = self.image.get_rect(center = pos) # image_group needs an image and a rect in order to use it's built in functions draw() and update()
        self.direction = pygame.math.Vector2()
        self.velocity = 2 # how fast character moves
        self.health = health 
        self.damage = damage
        self.experience = experience

    def player_direction(self, player):
        player_coords = player.rect.center 
        enemy_coords = self.rect.center
        self.direction.x = (player_coords[0] - enemy_coords[0])
        self.direction.y = (player_coords[1] - enemy_coords[1])

    '''
    automatically called when the sprite group an enemy object belongs to has the .update() function called on it
    '''
    def update(self, player):
        old_rect = self.rect.copy() # holds a copy of the current rect before movement, in case of a collision with another object
        self.player_direction(player)

        if self.direction.magnitude() != 0: # magnitude is absolute length of the vector given x and y (a^2 + b^2 = c^2)
            self.direction = self.direction.normalize() # normalize sets the magnitude to 1, so if two directions are pressed, the vector will be normalized to 1 instead of sqrt(2) 
        self.rect.center += self.direction * self.velocity # rect.center is a tuple and vector2's are compatable with operations involving tuples'

        # animation handling
        self.current_time = pygame.time.get_ticks()
        if (self.current_time - self.frame_current) > self.frame_speed:
            self.frame_next = False
            self.frame_num += 1
            if self.frame_num > 3:
                self.frame_num = 0
        if self.frame_next == False:
            self.frame_next = True
            self.frame_current = pygame.time.get_ticks()
            self.image = self.enemy_run[self.frame_num]
            self.image = pygame.transform.scale(self.image, (60,120))
            if self.direction.x < 0:
                self.image = pygame.transform.flip(self.image, True, False)

        if self.health <= 0:
            xp = Experience(self.rect.center, self.camera_group, self.experience) # pos, group, value
            self.experience_group.add(xp)
            groups = self.groups()
            for group in groups:
                group.remove(self)
                print('removed')


def main():
    print("Wrong file: please run run python3 main.py")

if __name__ == '__main__':
    main()
