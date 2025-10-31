class Rectangle:
    def __init__(self, x, y, height, width):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(height)
        self.width = abs(width)
    
    ''' Determined how to handle a rectangle object as a string, returning a description with all variables
    @param
        None
    @returns: str
        A description of all variables that a rectangle object has, c, y, width, height 
    '''
    def __str__(self):
        return f'(x: {self.x}, y: {self.y}) height: {self.height}, width: {self.width}'

def main():
    pass

if __name__ == '__main__':
    main()
