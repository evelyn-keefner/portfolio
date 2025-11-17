class Player:
    def __init__(self, sprites, speed, jump_height):
        self.lives = 3
        self.size = 'Normal'
        self.sprites = sprites
        self.speed = speed
        self.jump_height = jump_height
        self.powerup_time = 0
        self.invincible = False

    def movement(self):
        pass

    def jump(self):
        pass

    def give_powerup(self, powerup):
        if powerup == 'star': 
            self.invincible_star()
        elif powerup == 'fire':
            self.fire_flower()
    
    def clear_powerups(self):
        pass

    def invincible_star(self):
        self.invincible = True
        self.powerup_time = 100

    def fire_flower(self):
        pass

    def ground_collision(self):
        pass

class Goomba:
    def __init__(self, speed, path_x1, path_x2):
        self.speed = speed
        self.path_x1 = path_x1
        self.path_x2 = path_x2

    def move(self):
        pass
        
    def player_collision(self, player):
        pass

    def top_collision(self, player):
        pass # kill 

    def ground_collision(self):
        pass

class Pipe:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def player_collision(self, player):
        pass

    def teleport(self, player):
        pass

class QuestionBlock:
    def __init__(self, location, item):
        self.location = location
        self.item = item
    
    def player_collision(self, player):
        pass

class Flag:
    def __init__(self, location):
        self.location = location
    
    def award_points(self, location):
        pass

    def ending_animation(self, player):
        pass

    def next_level(self, player):
        pass

    def player_collision(self, player):
        pass

