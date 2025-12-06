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
        '''
        Handles incrementing or decrementing values
        args: None
        returns: str
            In the case the player selects a new weapon and not an upgrade a string is returned to be used in main() to update powerup list
        '''
        if self.increment == None:
            return self.name

        if self.increment != None:
            self.level += 1
            if self.is_percentage: # multiplicative scaling
                if self.is_increment: # multiplicative & increasing
                    if self.name == 'Gun Damage':
                        new_value = getattr(self.object, self.increment) * 1.5
                    elif self.name == 'Health':
                        new_value = getattr(self.object, self.increment) * 1.2
                        setattr(self.object, 'health', new_value) # heals the player to max when picking up
                    else:
                        new_value = getattr(self.object, self.increment) * 1.25

                    setattr(self.object, self.increment, new_value)

                else: # multiplicative & decreasing
                    new_value = getattr(self.object, self.increment) * 0.85
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
