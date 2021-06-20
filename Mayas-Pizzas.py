
def get_integer(m):
    user_input = int(input(m))
    return user_input

def get_string(m):
    user_input = input(m)
    return user_input

def print_list(L):
    for x in L:
        output = "{}: {} {}".format(i, L[0], L[1])
        print(output)
    return None


def print_menu(L):
    for x in L:
        output = "{} {}".format(x[0], x[1])
        print(output)
    return None


def order_pizza(L):
    for i in range(0, len(L)):
        output = "{}: {} {}".format(i, L[0], L[1])
        print(output)
    order_choice = get_integer("Please pick a pizza from the menu: -> ")
    if -1 < order_choice < len(L):
        print("{} has been chosen".format(order_choice))

    else:
        print("You have to enter a number between 0, 1, 2 or 3")
        return add_fruit(L)



def main():
    print("_"*47)
    print("Welcome to Mymyz Pizzeria")
    print("_" * 47)

    menu_list = [
        ["P", "Print Menu"],
        ["O", "Add to Order"],
        ["Q", "Quit"]
    ]

    run_program = True
    while run_program:
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
            print("_" * 47)
        user_choice = get_string("Please select an option: -> ")
        pizza_list = [
            ["Cheese", 2],
            ["Hawaian", 0],
        ]
        print("_" * 47)
        user_choice = user_choice.upper()
        user_choice = user_choice.strip()
        if user_choice == "P":
            print_menu(pizza_list)
        elif user_choice == "O":
            order_pizza(pizza_list)
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")
        print("_" * 47)
        print("Thank you for shopping with Mymyz Pizzeria")
        print("_" * 47)



if __name__ == "__main__":
    main()