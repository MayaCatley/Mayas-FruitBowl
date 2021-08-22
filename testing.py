from datetime import date
import re

def get_string(m):
    user_input = input(m)
    return user_input

def validate_phone(str):
    str = re.sub(r"\D", "", str)
    valid = True

    if re.match(r"^(64|04|02)", str):
        print("Thanks")
        if re.match(r"^64", str) and (len(str) < 10 or len(str) > 13):
            valid = False
        elif re.match(r"^04", str) and (len(str) < 8 or len(str) > 9):
            valid = False
        elif re.match(r"^(021|027)", str) and (len(str) < 10 or len(str) > 11):
            valid = False

    else:
        phone = get_string("Please enter a valid phone number: -> ")
        return validate_phone(str)

    print(str, valid)

def pick_phone():
    phone = get_string("What is your phone number: -> ")
    return phone

def main():
    phone = get_string("What is your phone number: -> ")
    validate_phone(phone)







if __name__ == "__main__":
    main()