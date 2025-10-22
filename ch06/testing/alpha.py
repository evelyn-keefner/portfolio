def get_filename() -> str:
    filename = None
    while(not filename):
        try:
            filename = input("Which file?")
            test = open(filename)
        except:
            print("That wasn't a valid filename please try again")
            filename = None
    return filename

def get_file(filename):
    return open(filename)

def count_alphanum(file) -> int:
    count: int = 0
    for char in file.read():
        if char.isalnum():
            count += 1
    return count

def write_data(filename, data):
    file = open(filename + ".dat", 'w')
    file.write(f"Number of alphanumeric characters: {data}")
    file.close()

def main():
    filename = get_filename()
    file = get_file(filename)
    write_data(filename, count_alphanum(file))

if __name__ == '__main__':
  main()
