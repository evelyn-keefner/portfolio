import pygame

class Experience(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, group, value):
        super().__init__(group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.image = pygame.image.load('assets/assets_ui/exp.webp')
        self.rect = self.image.get_rect(center = pos) # image_group needs an image and a rect in order to use it's built in functions draw() and update()
        self.value = value

    '''
    automatically called when the sprite group an enemy object belongs to has the .update() function called on it
    '''
    def update(self, player):
        pass

def main():
    print("Wrong file: please run run python3 main.py")

if __name__ == '__main__':
    main()
