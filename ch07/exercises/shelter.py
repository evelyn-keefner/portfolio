import time

class Shelter:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.id = id(self)
        self.time = time.strftime("%d/%m/%Y")

    def __str__(self) -> str:
        return f'Name: {self.name}\nType: {self.type}\nID: {self.id}\nTime: {self.time}'

def main() -> None:
    fido = Shelter('Fido', 'cat')
    print(fido)

if __name__ == '__main__':
    main()
