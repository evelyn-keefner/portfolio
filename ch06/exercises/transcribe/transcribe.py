def main():
    fpt = open("transcribed_text.txt", "w")
    user_input = "hi"

    if (user_input):
        with open("transcribed_text.txt", "w") as fpt:
            while (user_input):
                user_input = input("Enter a string to transcribe, enter nothing to exit.")
                fpt.write(f"{user_input}\n")
   
    fpt.close()
    print("Goodbye!")

if __name__ == '__main__':
    main()
