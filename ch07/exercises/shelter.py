import time

class Shelter:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.id = self.id()
        self.time = time.strftime("%d/%m/%Y")

    def get_id() -> int:
        return self.id()

def main() -> None:
    pass

if __name__ == '__main__':
    main()
