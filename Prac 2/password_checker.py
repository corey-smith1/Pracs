"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):

    pass_char_length = sum(1 for i in password)

    if MIN_LENGTH > pass_char_length or pass_char_length > MAX_LENGTH:
        return False


    count_lower = sum(1 for c in password if c.islower())
    count_upper = sum(1 for c in password if c.isupper())
    count_digit = sum(1 for c in password if c.isdigit())
    count_special = pass_char_length - count_digit - count_lower - count_upper

    if (count_lower * count_upper * count_digit) == 1:
        return True

main()