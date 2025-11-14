import pygame

class Bullet(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, enemy_vector, damage, group):
        super().__init__(group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.image.load('assets/assets_ui/start_button.webp')
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center = pos) # image_group needs an image and a rect in order to use it's built in functions draw() and update()
        self.direction = enemy_vector
        self.velocity = 25 # how fast character moves

    '''
    
    '''
    def update(self):
        self.input()

def main():
    print("Wrong file: please run python3 main.py")

if __name__ == '__main__':
    main()
