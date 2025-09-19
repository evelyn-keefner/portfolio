def number_to_letter_grade(grade) -> str:
    if (grade >= 90):
        return "A"
    if (grade >= 80):
        return "B"
    if (grade >= 70):
        return "C"
    if (grade >= 60):
        return "D"
    return "F"

def main():
    grade: int = int(input("Enter your grade out of 100: "))
    print(f"Your grade is: {number_to_letter_grade(grade)}")

if (__name__ == "__main__"):
    main()
