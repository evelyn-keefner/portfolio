def create_notes():
    f = open("notes.txt", "w")
    for i in range(10):
        f.write(f"__{i}___\n")
    f.close()

def read_notes() -> str:
    f = open("notes.txt", "r")
    notes = f.read()
    f.close()
    return notes

def readline_notes() -> str:
    f = open("notes.txt", "r")
    notes = f.readline()
    f.close()
    return notes

def readlines_notes() -> []:
    f = open("notes.txt", "r")
    notes = f.readlines()
    f.close()
    return notes

def append_notes() -> int:
    f = open("notes.txt", "a")
    f.write("Hello!")
    f.close()
    return 0 
    

def main():
    create_notes()
    print(read_notes())
    print(readline_notes())
    print(readlines_notes())
    append_notes()
    print(read_notes())


if __name__ == '__main__':
    main()
