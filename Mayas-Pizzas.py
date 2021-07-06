def get_integer(m):
    try:
        user_input = int(input(m))

        if user_input < 0:
            print("No negative numbers.")
            return get_integer(m)

        return user_input
    except ValueError:
        print("Please type a number: -> ")
        return get_integer(m)


def get_string(m):
    user_input = input(m)
    return user_input


def get_formatted_string(m):
    user_input = input(m)
    return user_input.upper().strip()


def pick_name():
    name = get_string("What is your name: -> ")
    return name

def pick_phone():
    phone = get_integer("What is your phone number: -> ")
    return phone

def pick_address():
    address = get_string("What is your address (Street Number, Street Name, Suburb): -> ")
    return address


def print_menu(L):
    print("Cost         Type")
    for x in L:
        output = "${:<7} --- {:>4}".format(x[1], x[0])
        print(output)
    return None


def print_order(L, order_type, name):
    print(order_type, name)
    print("Cost         Type      Quantity")
    for x in L:
        if x[1] > 0:
            output = "${:<7} --- {:>4} -- {:<4}".format(x[2], x[0], x[1])
            print(output)
    return None


def ask_yes_no(m):
    ask_again = get_formatted_string(m)
    if ask_again == "Y":
        return True
    elif ask_again == "N":
        return False
    else:
        print("Enter Y/N")
        return ask_yes_no()



def order_pizza(L, C):
    for i in range(0, len(L)):
        output = "{}: ${} - {} {}".format(i, L[i][2], L[i][0], L[i][1])
        print(output)
    choice = get_integer("Please pick a pizza from the menu: -> ")

    if -1 < choice < len(L):
        quantity = get_integer("How many {} would you like: -> ".format(L[choice]))
        L[choice][1] += quantity
        print("You now have {}".format(L[choice]))

        C += L[choice][2] * quantity
        print("Your current total is ${}".format(C))

        again = ask_yes_no("Would you like to order another pizza (Y/N): ->")
        if again:
            return order_pizza(L, C)
        else:
            return L
        again = get_formatted_string("Would you like to order another pizza (Y/N): -> ")
        if get_string == "Y":
            return order_pizza(L, C)
        elif again == "N":
            return L
        else:
            print("Enter yes or no")
            return order_pizza(L, C)

    else:
        print("You have to enter a number between 0 and 1")
        return order_pizza(L, C)


def remove_pizza(L, C):
    for i in range(0, len(L)):
        output = "{}: ${} - {} {}".format(i, L[i][2], L[i][0], L[i][1])
        print(output)
    choice = get_integer("Please pick a pizza you want to remove from: -> ")

    if -1 < choice < len(L):
        quantity = get_integer("How many {} would you like to remove: -> ".format(L[choice]))
        L[choice][1] -= quantity
        print("You now have {}".format(L[choice][1]))

        C =  (L[choice][2] * quantity) - C
        print("Your current total is ${}".format(C))


    else:
        print("You have to enter a number between 0 and 4")
        return remove_pizza(L, C)


def confirm_order(L):
    print("Quantity    Cost     Type")
    for x in create_customer_list[1]:
        output = "{:<6} ---- ${:>4} -- {:<6}".format(x[1], x[2], x[0])
        print(output)
    confirm = ask_yes_no("Would you like to confirm your order, enter Y for yes and N for no: -> ")
    if confirm:
        print("Thank you for your order, it will be ready soon")
        return main()
    else:
        return False


def review_order(L):
    print("Quantity    Cost     Type")
    for x in L:
        output = "{:<6} ---- ${:>4} -- {:<6}".format(x[1], x[2], x[0])
        print(output)
    return None


def pick_order_type():
    service = get_formatted_string("Would you like Delivery or Pickup or Quit (D/P/Q): -> ")

    if service == "D":
        name = pick_name()
        phone = pick_phone()
        address = pick_address()
        print("_" * 47)
        return "Delivery"
    elif service == "P":
        name = pick_name()
        phone = pick_phone()
        print("_" * 47)
        return "Pickup"
    elif service == "Q":
        return None
    else:
        print("Unrecognised entry")
        return pick_order_type()



def create_customer_list():
    return [
        ["Cheese", 0, 18.50],
        ["Hawaian", 0, 18.50],
        ["Pepperoni ", 0, 18.50],
        ["Meat Lover's", 0, 25.50],
        ["Veggie", 0, 25.50]
    ]


def main():
    cost = 0

    menu_list = [
        ["P", "Pizza Menu"],
        ["PO", "Print Current Order"],
        ["O", "Order Pizzas"],
        ["R", "Remove Pizzas"],
        ["T", "Change order type (Delivery/Pickup)"],
        ["C", "Customise Pizza"],
        ["CO", "Confirm Order"],
        ["Q", "Quit"]
    ]

    pizza_list = [
        ["Cheese", 18.50],
        ["Hawaian", 18.50],
        ["Pepperoni ", 18.50],
        ["Meat Lover's", 25.50],
        ["Veggie", 25.50]
    ]

    customer_list = create_customer_list()

    confirmed_orders = []

    print("_"*47)
    print("Welcome to Mymyz Pizzeria")
    print("_" * 47)

    order_type = pick_order_type()


    run_program = True
    while run_program:
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
            print("_" * 47)
        user_choice = get_string("Please select an option: -> ")
        print("_" * 47)
        user_choice = user_choice.upper()
        user_choice = user_choice.strip()
        if user_choice == "P":
            print_menu(pizza_list)
        elif user_choice == "PO":
            print_order(customer_list, order_type, name)
        elif user_choice == "O":
            order_pizza(customer_list, cost)
        elif user_choice == "N":
            new_pizza(customer_list)
        elif user_choice == "R":
            remove_pizza(customer_list, cost)
        elif user_choice == "T":
            new_order_type = pick_order_type()
            if new_order_type != None:
                order_type = new_order_type
        elif user_choice == "C":
            confirmed = confirm_order(customer_list)
            if confirmed:
                confirmed_orders.append([customer_list, order_type, name])
                customer_list = create_customer_list()
                cost = 0
                order_type = pick_order_type()
                name = pick_name()


        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")
        print("_" * 47)
        print("Thank you for shopping with Mymyz Pizzeria")
        print("_" * 47)



if __name__ == "__main__":
    main()