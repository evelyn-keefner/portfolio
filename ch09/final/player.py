import pygame

class Player(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, group):
        super().__init__(group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.image = pygame.image.load('sprites/placeholder_sprites/placeholder_character.png')
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.velocity = 5 # how fast character moves
        self.health = 20
    
    def get_image(self):
        return self.image

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

    def update(self):
        self.input()
        self.rect.center += self.direction * self.velocity

def main():
    print("Wrong file: please run run python3 main.py")

if __name__ == '__main__':
    main()
