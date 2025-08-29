# Functions Class Notes

- Algorithms
- Data

Vending Machine

- money
- item_code

money, item_code -> Vending Machine -> item

GUI - abstract interface

- Interface
- Black Box
  - Takes input
  - Produces out
  - Who cares how?

```py
def function_name():
    #python code
```

## Max Value

- ask the user for 3 numbers
- tell the user what number is the largest

### In Class Code - Monday 10/16

```py
# "hello" -> print -> None
val = print("hello")  # x -> func -> result
# print(val)


def myfunc():
    # Any valid python
    print("hi")
    print("bye")


myfunc()
myfunc()


def find_max():
    max = numbers[0]
    if numbers[1] > max:
        max = numbers[1]
    if numbers[2] > max:
        max = numbers[2]

    print(max)


# Driver Code

number = input("Please enter 3 numbers separated by commas: ")
numbers = number.split(",")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

find_max()

# other code

number = input("Please enter 3 numbers separated by commas: ")
numbers = number.split(",")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

find_max()

for i in range(100):
    number = input("Please enter 3 numbers separated by commas: ")
    numbers = number.split(",")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    find_max()
```

## Parameters

- Single Responsibility Principle
  - "A code block, function, or class should be responsible for one thing"
- Always get data outside of a function

## SCOPE

- Global
  - anything not in a function (or class)
  - Global scope is accessible anywhere in the file
- Local
  - limited to the function (or class) that it was defined in
  - parameters are define in the function

### In Class Code - Monday 10/23

```py
def myfunction(x):  # x = y
    # x = 6
    x = str(x + 5) * 10  # "11" => 111111..., 11 => 110
#     print(x)


def myfunction(x):  # x = y
    # gathering data
    # x = input("What is your number?")
    x = str(x + 5) * 10  # processing data
    print(x)


# x = 7
# x = str(x + 5) * 10
# print(x)
y = 7
x = input("What is your number?")
myfunction(y)
print(myfunction)
# x = 9
# x = str(x + 5) * 10
# print(x)
y = 10
myfunction(y)
# x = 7
# x = str(x + 5) * 10
# print(x)
y = 2.3
myfunction(y)

y = "2"
myfunction(y)

print()
print(5, 7)
print(7)


#This s not running code
def myfunction(x, y, z):  # x = y
    print(x, y, z)

#This is

myfunction(5, 6, 7) # positional arguments
myfunction(y=5, z=6, x=7) # keyword arguments


def myfunction(y, x, z=1):  # x = y
    x = 1
    y = 2
    z = 3
    total = x + y + z  # created
    print(total)
    # x,y,z,total


my_value = 10

# Positional arguments - Required
myfunction(5, 6)

# keyword arguments - Optional if given a default value
myfunction(y=5, z=1, x=7)

# a = 1
# b = 2
# c = 3
x = 100
y = 200
z = 300
jhgfliasdghalkwhvaCHGKJF = 7
myfunction(y=x, z=y, x=jhgfliasdghalkwhvaCHGKJF)
print(total)


import turtle
myt = turtle.Turtle()

def myfunc(theturtle, length, sides):
    pass
    #hgfklasreh

l = 5
s = 1000
myfunc(myt, l, s)

def find_max(numbers=[1,2,3]): # {"numbers":[1,2,3]}
    max = numbers[0]
    if numbers[1] > max:
        max = numbers[1]
    if numbers[2] > max:
        max = numbers[2]

    print(max)


num_list = input("Please enter 3 numbers separated by commas: ")
num_list  = num_list.split(",")
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

find_max(numbers=num_list) #find_max["numbers"] = num_list
```

## Function Formula

```
f(x) = y
```

f(input) = output
