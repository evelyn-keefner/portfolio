def main():
    mytuple = ("what's up", "i dont get it", 1, 1.044, 9)

    print(mytuple) 
    print()

    print(mytuple[1]) # "i don't get it"
    print()

    # mytuple[3] = "why"
    # you can't change a value in a tuple
    #
    for x in mytuple:
        print(x)
    print()

    for i, val in enumerate(mytuple):
        print(i, val)
    print()

    print(1 in mytuple) # True
    print()
    # print(mytuple.len()) 
    # You can't take the length of a tuple
    

if (__name__ == "__main__"):
    main()
