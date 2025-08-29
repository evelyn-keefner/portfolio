# Methods

`methods` work like fun ctions, except you must a have an object of a specific type

classes allow us to exapnd the scope of data


classes == dictionaries


# magic methods

any method starting and ending with `__` is a dunders


## Creating Models

```py
class Mario:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = "small"


    def change_status(self, new_status):
        self.status = new_status
```

```py
class Enemy:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("goomba.jpg")
        self.type = "turtle"


    def flatten(self):
        if self.type == "turtle":
            self.image = pygame.image.load("goomba_flattened.jpg")
        elif self.type == "goomba":
            pass

```

```py
class Box:
    def __init__(self, x, y, img):
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
```
