
def get_integer(m):
    user_input = int(input(m))
    return user_input

def get_string(m):
    user_input = input(m)
    return user_input

def review_fruit(l):
    for x in l:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)
    return None


def main():
    fruit_list = [
        ["apples", 2],
        ["pears", 0],
        ["quinces", 3],
        ["lemons", 7]
]

    menu_list =[
        ["R" , "Reveiw Fruit"],
        ["Q" , "Quit"]
    ]
    run_program = True
    while run_program:
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: -> ")
        if user_choice == "R":
            review_fruit(fruit_list)
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")
        print("Thank you, the program has ended")

if __name__ == "__main__":
    main()

