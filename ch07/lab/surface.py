from rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
        self.rect = Rectangle(x, y, h, w)
        self.image = filename
    
    ''' Returns the rectangle object of surface
    @param
        None
    @returns: rectangle.Rectangle
    '''
    def getRect(self) -> Rectangle: 
        return self.rect

def main():
    pass

if __name__ == '__main__':
    main()
        
