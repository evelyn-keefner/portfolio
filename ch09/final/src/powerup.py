class Powerup:
    def __init__(self, name):
        self.name = name

    def __init__(self, name, level, increment, is_increment, is_percentage, object):
        self.name = name
        self.level = level
        self.increment = increment
        self.is_increment = is_increment
        self.is_percentage = is_percentage
        self.object = object

    def give_powerup(self) -> str:
        if self.increment == None:
            return self.name

        if self.increment != None:
            self.level += 1
            if self.is_percentage: # multiplicative scaling
                if self.is_increment: # multiplicative & increasing
                    new_value = getattr(self.object, self.increment) * 1.05
                    setattr(self.object, self.increment, new_value)
                else: # multiplicative & decreasing
                    new_value = getattr(self.object, self.increment) * 0.95
                    setattr(self.object, self.increment, new_value)
            else: # additive scaling
                if self.is_increment: # additive & increasing
                    new_value = getattr(self.object, self.increment) + 1
                    setattr(self.object, self.increment, new_value)
                else: # additive & decreasing
                    new_value = getattr(self.object, self.increment) - 1
                    setattr(self.object, self.increment, new_value)
            return ''

def main() -> None:
    pass

if __name__ == '__main__':
    main()
