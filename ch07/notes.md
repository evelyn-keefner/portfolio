# OOP

Complexity == SLOC

- Source Lines of Code

- Web Browser: >100 Million
- ATM: 10000
- Mobile App: 60,000

## Complex Object

- made up of primitive and other complex objects
- Contains data and algorithms to work with the data
- Record: compiled data treated as a single object

- State
- Behavior

## Graph

State:

- range of x and y
- points

Behavior:

- make a line between coordinates
- add/remove points
- change points color

Type == Class

## Point

state: x, y

```py

class Point:


```

- Use classes to define an object
- Create objects, instantiate, from classes
- Each object from a class has its own state

## Python built-in classes

- int, Turtle, range

# Style rule for Python

- Enforced by many other language

One class per file


```py
accumulator=<starting value>
for _ in <list>:
    accumulator += _
```

## Design Patterns

### Model View Controller (MVC)

- Model
  - Data and state
  - contain data specific algorithms
- View
  - translates data to pixels
  - pygame does this for us
    - HTML/CSS/JS
- Controller
  - Ties events to algorithms, updates data, and displays the screen
