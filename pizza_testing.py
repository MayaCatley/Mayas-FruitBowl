def get_string(m):
    user_input = input(m).strip()
    return user_input


def pick_name():
    name = get_string("What is your name: -> ")
    return validate_letters_name, validate_name(name)


def validate_name(name):
    if len(name) < 2 or len(name) > 30:
        print("The name must be between 2 and 30 characters.")
        return pick_name()
    else:
        return name


def validate_letters_name(name):
    while True:
        if name.isalpha():
            return name
        else:
            print("Please use only letters, try again")
            return pick_name()
