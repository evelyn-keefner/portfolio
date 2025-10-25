def capitals():
    capitals = {
        "USA":"Washington, D.C.",
        "France":"Paris",
        "Japan":"Tokyo"
    }

    for country, capital in capitals.items():
        print(f"Country: {country}\nCapital: {capital}")

    user = input("\nEnter a country name to get its capital\n")
    value = capitals.get(user)
    if (value != None):
        print(value)
    else:
        print("get real")

def main():
    fruit_colors = {
        'apple':'red',
        'banana':'yellow',
        'cherry':'red',
        'mango':'orange'
    }

    print(fruit_colors)

    print(fruit_colors['banana'])
    
    print()
    print(fruit_colors['apple'])
    fruit_colors['apple'] = 'green'
    print(fruit_colors['apple'])
    
    print()
    print(fruit_colors)
    fruit_colors['grapes'] = 'purple'
    print(fruit_colors)

    print()
    print(len(fruit_colors))

    print()
    for k, v in fruit_colors.items():
        print(f"{k} -- {v}")

    capitals()

if (__name__ == "__main__"):
    main()

