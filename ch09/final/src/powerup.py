class Powerup:
    def __init__(self, name):
        self.name = name

    def __init__(self, name, level, increment, is_increment, is_percentage):
        self.name = name
        self.level = level
        self.increment = increment
        self.is_increment = is_increment
        self.is_percentage = is_percentage

    def give_powerup(self):
        self.level += 1
        print("before", self.increment)
        if self.is_percentage: # multiplicative scaling
            if self.is_increment: # multiplicative & increasing
                self.increment *= 2
            else: # multiplicative & decreasing
                self.increment *= 0.95
        else: # additive scaling
            if current_powerup.is_increment: # additive & increasing
                self.increment += 1
            else: # additive & decreasing
                self.increment -= 1
                            
        print("after", self.increment)
        print("after 2", self.main_player.velocity)

def main() -> None:
    pass

if __name__ == '__main__':
    main()
