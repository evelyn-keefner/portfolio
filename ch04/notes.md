## CH4: While Loops Notes

```py
size = pygame.display.get_window_size() # [w, h]
width = size[0]
length = size[1]

width, height = screen.get_size()
print(width
print(height)
```

```py
# only one
# required
if `<boolean expression>`:
    #code
#optional, can have as many as you need
elif `<boolean expression>`:
elif `<boolean expression>`:
# else:
else: optional, only one

num = int(input("enter a num"))
if num > 5:
    print("A")
elif num > 10: #will never run because previous rule matches
    print("B")
else:
    print("C")

num = int(input("enter a num"))
if num > 10: # most exclusive condition first
    print("A")
elif num > 5:
    print("B")
else:
    print("C")
```

```py
# event loop
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos)
    elif event.type = pygame.KEYDOWN:
        print(event.key)
        if event.key == pygame.K_SPACE:
            #do something
        elif ...
```

# Iteration

Something you can loop through

```
for i in obj:
  print(i)
```

onj is iterable

# Sample code from

```py
import pygame

pygame.init()

while True:
    pygame.time.wait(2000)
    num_events = len(pygame.event.get())
    print(num_events)
    print(pygame.event.get())


for i in [1, 2, 3, 4]:
    print(i)

for c in "Hello":
    print(c)


# MUTABLE VS IMMUTABLE

# strings are immutable

var = "Hello"
# var[0] = "J" # ERROR

var.lower()
print(var)

var2 = var.lower()
print(var2, var)

var = var.lower()
print(var)

# Slicing
var = "Goodbye"
print(var[1:-1])

var = "Goodbye"
print(var[1:])
var = "Goodbye"
print(var[:-1])
var = "Hello"
print("j" + var[1:])

Lists are Mutable

var[0] = "j"  # str, error

mylist = [3, 2, 4, 5, 1]
mylist_half = [3, 2, 4, 5, 1]
mylist2 = [3, 2, 4, 5, 1]
# mylist[0] = 10
mylist[2:2] = [6, 7]  # between
mylist_half[2:6] = [6, 7]  # overwrites index 3, up to 4
mylist2[2] = [6, 7]  # overwites index 3
print(mylist, mylist_half, mylist2, sep="\n")
mylist[2:4] = [6, 7]
print(mylist)

SLicing

iterable[start:stop]
start is inclusive index
stop is an exclusive index

for i in mylist:  # just getting the value
    i = 0
print(mylist)

mylist = [1, 2, 3]
for value in mylist:
    value = value * 2
print(mylist)

# enumerate
# get index to access the original object
mylist = ["A", "B", "C"]
for green, blue in enumerate(mylist):
    print(green, blue)
    mylist[green] = blue * 2
print(mylist)
```

## Iterable Objects Review

containers

- lists
- str

## Mutability vs Immutability

- Can it change?

```py
mystr = "Hello"
mystr[0] = "Y" #ERROR - str are immutable
```

```py
mystr = "Hello"
mylist = list(mystr)
mylist[0] = "Y" #NO ERROR - lists are mutable
```

# While

for loops solve the problem of repeating an algorithms consecutively a number of times

## Slicing Review

iterable: list, str

```py
mylist = ['a','b','c']
print(mylist[0])
print(mylist[0:2]) #['a','b']
print(mylist[:-1]) #['a','b']
print(mylist[0:10]) #???

otherlist = ['z', 'y']

print(mylist[1:1]) = otherlist #['a','z', 'y', 'b','c']
print(mylist)
mylist[1:-1] = otherlist #['a','z', 'y','c']
print(mylist)
```

# Tuple

immutable list
defined with `()`

The location of the data has nothing to do with the value of the data

The index (or key) is related to the data itself in some way

# Dictionary

- defined with `{}`
- key => value
- keys must be unique
- keys must be immutable, usually str
- values can be any valid python object

# GUI

Graphical User Interface

## mainloop

drives your entire GUI program

```py

while True:
    # one frame i.e. one picture of your program
    #1. event loop

    #2. Update data

    #3. redraw the frame

    #4. flip/update
```
