import pygame

class Bullet(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, enemy_vector, damage, camera_group, bullet_group, enemy_group):
        super().__init__(camera_group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.camera_group = camera_group
        self.bullet_group = bullet_group
        self.bullet_group.add(self)
        self.enemy_group = enemy_group 

        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('assets/assets_ui/bullet.webp')
        # self.image = pygame.image.load()
        self.rect = self.image.get_rect(center = pos) # image_group needs an image and a rect in order to use it's built in functions draw() and update()

        self.damage = damage

        self.direction = enemy_vector
        self.velocity = 25 # how fast character moves
        
        self.spawn_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.bullet_lifetime = 2500 # 2.5 seconds
    
    def move(self):
        '''
        Updates sprite position
        args: None
        returns: None
        '''
        if self.direction.magnitude() != 0:
            self.rect.center += self.direction * self.velocity

    def out_of_bounds_bullet_kill_check(self):
        '''
        removes bullets that have flown off screen based on a timer
        args: None
        returns: None
        '''
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.spawn_time > self.bullet_lifetime:
            print('removed bullet')
            self.kill()
    
    def enemy_kill_check(self):
        '''
        Checks for collision with enemy, applies damage to enemy, then kills self
        args: None
        returns: None
        '''
        contacted_enemies = pygame.sprite.spritecollide(self, self.enemy_group, False)
        if contacted_enemies:
            contacted_enemies[0].health -= self.damage
            self.kill()

    def update(self):
        '''
        Updates bullet
        args: None
        returns: None
        '''
        self.move()
        self.out_of_bounds_bullet_kill_check()
        self.enemy_kill_check()

def main():
    print("Wrong file: please run python3 main.py")

if __name__ == '__main__':
    main()
