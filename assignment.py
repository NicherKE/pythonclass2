print('Write a program that checks whether a year is a leap year or not')

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input year from the user
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")



#program that checks whether an alphabet letter is a consonant or a vowel

# Get user input
letter = input("Enter a letter: ")

# Convert the input to lowercase to handle both uppercase and lowercase letters
letter = letter.lower()

# Check if the input is a single alphabet character
if len(letter) == 1 and letter.isalpha():
    # Check if the letter is a vowel
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
else:
    print("Please enter a single alphabet character.")
