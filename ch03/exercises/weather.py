def weather(weather, temp):
    items = []
    if (weather == "rainy"):
        items.append("umbrella")
    else:
        items.append("sunglasses")

    if (temp < 32):
        items.append("coat")
    else:
        items.append("shorts")
    
    print(f"Bring your {items[0]} and your {items[1]}!")

def main():
    weather("rainy", 11)
    weather("rainy", 35)
    weather("sunny", 35)

if (__name__ == "__main__"):
    main()
