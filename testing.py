from datetime import date
import re

def validate_phone(str):
    str = re.sub(r"\D", "", str)
    valid = True

    if re.match(r"^(64|04|02)", str):
        if re.match(r"^64", str) and (len(str) < 10 or len(str) > 13):
            valid = False
        elif re.match(r"^04", str) and (len(str) < 8 or len(str) > 9):
            valid = False
        elif re.match(r"^(021|027)", str) and (len(str) < 10 or len(str) > 11):
            valid = False
    else:
        valid = False

    print(str, valid)

def main():
    validate_phone("0000")
    validate_phone("04-555-555")
    validate_phone("04-555-5555")
    validate_phone("04 555 5555")
    validate_phone("64 04 555 5555")
    validate_phone("64 21 555 5555")
    validate_phone("021 555 5555")
    validate_phone("021 5555")
    validate_phone("64 021 5555")
    validate_phone("64 021 5555 444")

if __name__ == "__main__":
    main()



