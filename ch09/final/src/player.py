import pygame

class Player(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, group):
        super().__init__(group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.image = pygame.image.load('assets/sprite/sprite_run1.webp')
        self.image = pygame.transform.scale(self.image, (60,60))
        self.rect = self.image.get_rect(center = pos) # image_group needs an image and a rect in order to use it's built in functions draw() and update()
        self.direction = pygame.math.Vector2()
        self.velocity = 5 # how fast character moves
        self.health = 20
        self.invulnerable = False
        self.invulnerable_time = 500 # invincibility time in milliseconds (0.5 seconds)
        self.current_time = pygame.time.get_ticks()
        self.damage_time = 0
    
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
    def update(self, enemy_group):
        old_rect = self.rect.copy() # holds a copy of the current rect before movement, in case of a collision with another object
        keys = pygame.key.get_pressed() # for distinguishing run animation from idle animation
        self.input()
        if self.direction.magnitude() != 0: # magnitude is absolute length of the vector given x and y (a^2 + b^2 = c^2)
            self.direction = self.direction.normalize() # normalize sets the magnitude to 1, so if two directions are pressed, the vector will be normalized to 1 instead of sqrt(2) 
        self.rect.center += self.direction * self.velocity # rect.center is a tuple and vector2's are compatable with operations involving tuples'
        
        self.current_time = pygame.time.get_ticks()
        if (self.current_time - self.damage_time) > self.invulnerable_time:
            self.invulnerable = False

        contacted_enemies = pygame.sprite.spritecollide(self, enemy_group, False)
        if contacted_enemies and not self.invulnerable:
            self.health -= contacted_enemies[0].damage
            self.damage_time = pygame.time.get_ticks()
            self.invulnerable = True
            print(self.health)

        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
            tick = pygame.time.get_ticks()
            image = f'assets/sprite/sprite_run{tick%4+1}.webp'
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (60,60))
        else:
            tick = pygame.time.get_ticks()
            image = f'assets/sprite/sprite_idle{tick%4+1}.webp'
            self.image = pygame.image.load(image)
            self.image = pygame.transform.scale(self.image, (60,60))


def main():
    print("Wrong file: please run run python3 main.py")

if __name__ == '__main__':
    main()
