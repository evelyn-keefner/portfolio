import pygame

class Button(pygame.sprite.Sprite): # class inherits from the sprite class to be able to add it to a sprite group and use update() and draw()
    def __init__(self, pos, group, image, text):
        super().__init__(group) # adds player sprite into the camera_group sprite group calling the sprite constructor Sprite(self, group)
        self.image = pygame.image.load(image)
        w,h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (2*w,2*h)) if image == 'assets/assets_ui/start_button.webp' else self.image
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('assets/PokemonGb-RAeo.ttf', 25)
        self.text = text
        self.rect = self.image.get_rect(center = pos) # image_group needs an image and a rect in order to use it's built in functions draw() and update()
        self.pressed = False
        self.not_on_delay = True
        self.current_time = 0
        self.click_time = 0
        self.click_buffer = 100

    def mouse_click(self) -> bool:
        '''
        returns whether or not the left mouse button has been clicked
        args: None
        returns: bool
            State of left mouse button
        '''
        return pygame.mouse.get_pressed(num_buttons=3)[0]

    def input(self):
        '''
        handles user input, and updates object state to reflect if self is pressed or not
        args: None
        returns: None
        '''
        self.current_time = pygame.time.get_ticks()
        mouse_position = pygame.mouse.get_pos() 

        if (self.current_time - self.click_time) >= self.click_buffer:
            self.not_on_delay = True
        if self.rect.collidepoint(mouse_position):
            if self.mouse_click():
                if self.pressed:
                    self.pressed = False
                else:
                    if self.not_on_delay:
                        self.pressed = True
                        self.not_on_delay = False
                        self.click_time = pygame.time.get_ticks()
            else:
                self.pressed = False
        else:
            self.pressed = False
    
    def display_updates(self):
        '''
        handles rendering of text and background of button and draws it to the screen
        args: None
        returns: None
        '''
        self.display_surface.blit(self.image, self.rect.topleft)
        text = self.font.render(self.text, True, 'black')
        text_rect = text.get_rect(center=self.rect.center)
        self.display_surface.blit(text, text_rect)

    def update(self):
        '''
        updates input and displays button to the screen
        args: None
        returns: None
        '''
        self.input()
        self.display_updates()
        
def main():
    print("Wrong file: please run python3 main.py")

if __name__ == '__main__':
    main()
