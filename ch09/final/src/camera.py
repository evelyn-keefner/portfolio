import pygame

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2 
        self.half_h = self.display_surface.get_size()[1] // 2 

        # ground
        self.ground_surf = pygame.image.load('assets/assets_ui/background.webp')
        w,h = self.ground_surf.get_size()
        self.ground_surf = pygame.transform.scale(self.ground_surf, (3*w,3*h))
        self.ground_width = self.ground_surf.get_width() 
        self.ground_height = self.ground_surf.get_height()

        self.ground_rect = self.ground_surf.get_rect(topleft = (0, 0))

    def center_target_camera(self, target):
        '''
        Calculates vector offset of an object with respect to the center of the screen, then updates self
        args: None
        returns: None
        '''
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def player_in_relation_to_ground(self, player, rects):
        '''
        determines which of the 9 ground rects the player is standing in, and sets the current rect to that rect
        args: 
            pygame.sprite
                the player object in order to check collision with the ground
            list
                list of pygame.rect objects containing all 9 ground rects
        '''
        for rect in rects:
            if player.rect.colliderect(rect):
                self.ground_rect = rect
                return None
 
    def draw_ground(self, player):
        '''
        calculates locations of ground rects, and blits all 9 to the screen in relation to the player
        args:
            pygame.sprite
                The player object needed for player_in_relation_to_ground()
        returns: None
        '''
        ground_rects = []
        current_x = self.ground_rect.topleft[0]
        current_y = self.ground_rect.topleft[1]

        ground_coordinates = [
            (current_x - self.ground_width, current_y - self.ground_height), 
            (current_x, current_y - self.ground_height), 
            (current_x + self.ground_width, current_y - self.ground_height), 
            (current_x - self.ground_width, current_y), 
            (current_x, current_y), 
            (current_x + self.ground_width, current_y), 
            (current_x - self.ground_width, current_y + self.ground_height), 
            (current_x, current_y + self.ground_height), 
            (current_x + self.ground_width, current_y + self.ground_height)
        ]   

        for i in range(9):
            ground_rects.append(self.ground_surf.get_rect(topleft = ground_coordinates[i]))

        self.player_in_relation_to_ground(player, ground_rects)

        for ground_rect in ground_rects:
            self.display_surface.blit(self.ground_surf, ground_rect.topleft - self.offset)
    
    def sprite_stacking(self):
        '''
        displays all sprites in group depending on their y value in order to create a false 3d effect
        args: None
        returns: None
        ''' 
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def custom_draw(self, player):
        '''
        draws all ground and sprites in group
        args:
            pygame.sprite
                The player object needed for center_target_camera()
        returns: None
        '''
        self.center_target_camera(player)
        self.draw_ground(player)
        self.sprite_stacking()
        

