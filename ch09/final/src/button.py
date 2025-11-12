import pygame

class Button(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, group, image, text):
        super().__init__(group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.image = pygame.image.load('assets/assets_UI/start_button.webp')
        w,h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (2*w,2*h))
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.SysFont('Arial', 25)
        self.image = pygame.image.load(image)
        self.text = text
        self.rect = self.image.get_rect(center = pos) # image_group needs an image and a rect in order to use it's built in functions draw() and update()
        self.pressed = False

    def mouse_click(self) -> bool:
        return pygame.mouse.get_pressed(num_buttons=3)[0]

    def input(self):
        mouse_position = pygame.mouse.get_pos() 
        if self.rect.collidepoint(mouse_position):
            if self.mouse_click():
                if self.pressed:
                    pass
                else:
                    self.pressed = True
            else:
                self.pressed = False
        else:
            self.pressed = False

    '''
    automatically called when the sprite group a button object is contained in has the .update() method called on it
    update handles button input AND drawing of button and text to the screen
    '''
    def update(self):
        self.input()
        self.display_surface.blit(self.image, self.rect.topleft)
        text = self.font.render(self.text, True, 'black')
        text_rect = text.get_rect(center=self.rect.center)
        self.display_surface.blit(text, text_rect)

def main():
    print("Wrong file: please run python3 main.py")

if __name__ == '__main__':
    main()
