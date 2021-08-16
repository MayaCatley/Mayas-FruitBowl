# allows for the order history to have a accurate date
# https://www.programiz.com/python-programming/datetime/current-datetime (the website i used for reference)
from datetime import date

# this allows for numbers to be searched for (specifically phone numbers)
import re

# ensures that the user is entering a valid phone number
# https://www.sololearn.com/Discuss/2588446/solved-python-phone-number-validator (the website i used for reference)
def validate_phone(str):
    """Make sure the users phone number is valid

    :param str: string
    :return: pick_phone
    """
    valid = True
    # this tests to match the starting numbers with the rest of the number
    if not re.match(r"^(64|04|02)", str):
        valid = False
    # if the number starts with 64 the total amount of letter have to be 10-13
    elif re.match(r"^64", str) and (len(str) < 10 or len(str) > 13):
        valid = False
    # if the number starts with 04 the total amount of letter have to be 8 or 9
    elif re.match(r"^04", str) and (len(str) < 8 or len(str) > 9):
        valid = False
    # if the number starts with 021, 022, 027 the total amount of letter have to be 10 or 11
    elif re.match(r"^(021|022|027)", str) and (len(str) < 10 or len(str) > 11):
        valid = False

    return valid


# this function makes sure that the user is entering a name that is between 2-30 characters
def validate_name(name):
    """Make sure the users name is between 2-30 characters long

    :param name: string
    :return: name
    """
    if len(name) < 2 or len(name) > 30:
        print("The name must be between 2 and 30 characters.")
        return pick_name()
    else:
        return name


# this function makes sure that the user is entering an address that is between 10-60 letters
def validate_address(addr):
    """Make sure the users address is valid

    :param addr: string
    :return: addr
    """
    if len(addr) < 10 or len(addr) > 60:
        print("The address must be between 10 and 60 characters")
        return pick_address()
    else:
        return addr


# this function makes sure that the user is entering is entering a number,
# and that the number is within the min and max boundaries
def get_integer(m, min=0, max=999999):
    """Make sure the users number is valid

    :param m: integer
    :param min: 0
    :param max: 999999
    :return: user_input
    """
    getting_user_integer = True
    while getting_user_integer:
        try:
            user_input = int(input(m))
        except ValueError:
            print("Please type a number: -> ")
            continue
        if user_input < min or user_input > max:
            print("You must enter a number between {} and {}".format(min, max))
            continue
        getting_user_integer = False
    return user_input


# these functions makes sure that regardless of the format used by the user, lowercase and capital letters are allowed
def get_string(m):
    """Format user input to same case

    :param m: string
    :return: user_input
    """
    user_input = input(m).strip()
    return user_input


def get_formatted_string(m):
    """Format user input to same case

    :param m: string
    :return: user_input.upper().strip()
    """
    user_input = input(m)
    return user_input.upper().strip()


# these functions gather information such as the users name, phone number and address, and makes sure they are validated
def pick_name():
    """Ask for the users name

    :return: validate_name(name)
    """
    name = get_string("What is your name: -> ")
    return validate_name(name)


def pick_phone():
    """Ask for the users phone number

    :return: phone
    """
    phone = get_string("What is your phone number: -> ")

    # this removes anything that is not a number
    phone = re.sub(r"\D", "", phone)

    if not validate_phone(phone):
        # if number doesn't appear valid, print message
        print("This doesn't appear to be a valid phone number")
        #try again
        return pick_phone();

    return phone

def pick_address():
    """Ask for the users address

    :return: validate_address(address)
    """
    address = get_string("What is your address (Street Number, Street Name, Suburb): -> ")
    return validate_address(address)


# function that prints out the pizza menu
def print_menu(L):
    """Print out the pizza menu

    :param L: list
    :return: None
    """
    print("    Cost         Type")
    index = 0
    for x in L:
        index += 1
        output = "({}) ${:<7} --- {:>4}".format(index, x[1], x[0])
        print(output)
    return None


# validation for (Y)es and (N)o questions
def ask_yes_no(m):
    """Ask user yes or no

    :param m: string
    :return: ask_yes_no(m)
    """
    ask_again = get_formatted_string(m)
    if ask_again == "Y":
        return True
    elif ask_again == "N":
        return False
    # if the user enters another value, they are asked to try again
    else:
        print("Enter Y/N")
        return ask_yes_no(m)


# function that prints out the users current order
def print_current_order(current_order):
    """Print the users current order

    :param current_order: list
    :return: None
    """
    # main portion of the programs cost feature
    cost = 0
    for x in current_order["items"]:
        cost += x[1]

    # if the user is getting their order delivered, $3 is added to their total
    is_delivery = current_order["type"] == "Delivery"
    if is_delivery:
        cost += 3
    # formatting so the code prints nicely and looks like a receipt
    print("_" * 47)
    print("         CURRENT ORDER")
    print("Name: {}    --   Phone: {}    --   Order Type: {}".format(current_order["name"], current_order["phone"], current_order["type"]))
    print("Total: ${}".format(cost))
    print("   == Pizza ==")

    # this means the cost is just from the current order, and not all previous orders
    current_order["cost"] = cost
    # this means the "pizzas" are the amount of pizzas in the current order
    pizzas = current_order["items"]

    # if the user tries to view their order, but they haven't ordered a pizza, the program will inform them
    if len(pizzas) == 0:
        print("You have not selected any pizzas")
    # this prints out the users pizzas as well as any toppings, options and changes
    else:
        for i in range(0, len(pizzas)):
            output = "{}: ${} - {} (Toppings: {}) (Options: {})".format(
                # this means that 0 won't be an index number, as i used 0 to quit throughout my program
                i+1,
                # pizza[0] is the name of the pizza, pizza[1] is the current price,
                # pizza[2] is the toppings, and pizza[3] is the options
                pizzas[i][1], # cost
                pizzas[i][0], # pizza name
                # "no changes" and "none selected' are printed
                # instead of toppings and pizzas if the user hasn't changed anything
                pizzas[i][2] if len(pizzas[i][2]) > 0 else "No changes",  # toppings
                pizzas[i][3] if len(pizzas[i][3]) > 0 else "None selected"  # options
            )
            print(output)
    # this informs the user of the delivery cost
    if is_delivery:
        print("Delivery: $3.00")


# this is the function for ordering a pizza
def order_pizza(current_order, pizza_list):
    """Ask the user to order a pizza

    :param current_order: list
    :param pizza_list: list
    :return: current_order
    """
    # max input is the max number the pizza list goes up to
    max_input = len(pizza_list)
    # print menu function
    print_menu(pizza_list)
    # the users current order information
    print_current_order(current_order)

    # this requests user input for what pizza they want to order
    choice = get_integer(
        "Please pick a pizza from the menu (0 to skip): -> ", 0, max_input)

    # if the user chooses to pick 0 the program exits out of order pizza
    if choice == 0:
        return current_order

    # if the user selects a number from the menu, the pizza chosen is added onto their order
    if 0 < choice <= max_input:
        pizza = clone_list(pizza_list[choice-1])
        current_order["items"].append(pizza)

        # the user is asked if they want another pizza
        again = ask_yes_no("Would you like to order another pizza (Y/N): ->")
        # the user can't order another pizza if they already have purchased 10
        if again:
            if len(current_order["items"]) >= MAX_ORDER_SIZE: # max order size is 10 pizzas per order
                print("You have selected our maximum order size of {} pizzas. "
                      "Please remove a pizza before adding a new one".format(
                    MAX_ORDER_SIZE))
                return current_order
            # return the user to the pizza menu to order again
            else:
                return order_pizza(current_order, pizza_list)
        # return the user back to the main menu
        else:
            return current_order
    # if the user enters an invalid entry, this helpful error message will be printed
    print("You have to enter a number between 1 and {}".format(max_input))
    return order_pizza(current_order, pizza_list)


# this function allows the user to remove pizzas from their order
def remove_pizza(current_order):
    """Ask user to remove a pizza from their order

    :param current_order: list
    :return: remove_pizza(current_order)
    """
    # prints the users current order
    print_current_order(current_order)

    # if the user hasn't ordered any pizza, a helpful error message will inform them of that
    if len(current_order["items"]) == 0:
        print("There are no more pizzas to remove")
        return current_order
    # this asks the user what pizza they want to remove
    choice = get_integer("Please pick a pizza you want to remove (0 to exit): -> ")

    # if the choose 0 (exit) they are taken back to the main menu
    if choice == 0:
        return current_order
    # if they enter a valid number, that pizza is removed from their order
    elif 0 < choice <= len(current_order["items"]):
        del current_order["items"][choice-1]
        return remove_pizza(current_order)
    # if the user enters an invalid entry, this helpful error message will be printed
    else:
        print("You have to enter a number between 1 and {}".format(len(current_order["items"])))
        return remove_pizza(current_order)


# this function is for creating a new order
def create_new_order(all_orders):
    """Create a new order

    :param all_orders: list
    :return: current_order, previous_orders
    """
# this is the information each order requires
    current_order = {
        "date": date.today().isoformat(),  # finds current date and then is formatted to be "yyyy-mm-dd"
        "name": "",
        "type": "",
        "items": [] # empty order to start
    }
    current_order = pick_order_type(current_order)
    # this categorises all the previous orders by phone number
    # this means if the phone numbers are the same, the user can re-order previous pizzas
    try:
        previous_orders = all_orders[current_order['phone']]
    except KeyError:
        previous_orders = None

    return current_order, previous_orders


# this function is so the user can pick Delivery, Pickup or Choose Later
def pick_order_type(current_order):
    """Ask user to pick Delivery, Pickup or Choose Later

    :param current_order: list
    :return: current_order
    """
    # asks the user what option they want to pick
    service = get_formatted_string(
        "Would you like (D)elivery or (P)ickup or (C)hoose Later (D/P/C): -> ")

    # if they pick delivery, the following information is required,
    # and the order type is made to be "Delivery"
    if service == "D":
        current_order["name"] = pick_name()
        current_order["phone"] = pick_phone()
        current_order["address"] = pick_address()
        current_order["type"] = "Delivery"
        print("_" * 47)
        return current_order
    # if they pick pick up, the following information is required,
    # and the order type is made to be "Pickup"
    elif service == "P":
        current_order["name"] = pick_name()
        current_order["phone"] = pick_phone()
        current_order["address"] = ""
        current_order["type"] = "Pickup"
        print("_" * 47)
        return current_order
    # if they pick Choose Later, the following information is required,
    # and the order type is made to be "Not yet selected"
    elif service == "C":
        print("You have selected to choose Deliver or Pickup later")
        current_order["name"] = pick_name()
        current_order["phone"] = pick_phone()
        current_order["type"] = "Not yet selected"
        print("_" * 47)
        return current_order
    # if they enter anything else, a helpful error message is printed
    else:
        print("Unrecognised entry")
        return pick_order_type(current_order)


# this function allows the user to confirm their order
def confirm_order(current_order):
    """Ask user to confirm order

    :param current_order: list
    :return: boolean
    """
    print_current_order(current_order)

    # if they have ordered no pizzas, they cannot confirm their order
    if len(current_order["items"]) == 0:
        return False

    # if they try to checkout but haven't selected delivery or pickup because the user previous picked Choose Later
    # they are asked to select one or the other
    if current_order["type"] == "Not yet selected":
        service = get_formatted_string(
            "Please select either (D)elivery or (P)ickup (D/P): -> ")
        # if they pick Delivery ask for address and change order type to "Delivery"
        if service == "D":
            current_order["address"] = pick_address()
            current_order["type"] = "Delivery"
            print("You have selected Delivery")
            print("_" * 47)
        # if they pick Pick Up change order type to "Pickup"
        elif service == "P":
            current_order["type"] = "Pickup"
            print("You have selected Pickup")
            print("_" * 47)
    # if all other information is there, the user if asked if they want to confirm
    confirm = ask_yes_no("Would you like to confirm your order, enter Y for yes and N for no: -> ")
    # if they do want to confirm, the current order is finished
    if confirm:
        print("Thank you for your order, it will be ready soon")
        print("_" * 47)
        print("_" * 47)
        return True
    # if not, the confirmed function won't finish
    return False


# https://stackoverflow.com/questions/9542738/python-find-in-list (the website i used for reference)
# this allows the program to find different pizzas from the list
def find_pizza_by_name(name, pizza_list):
    """Find the name of a pizza

    :param name: string
    :param pizza_list: list
    :return: clone_list(pizza)
    """
    pizza = [x for x in pizza_list if x[0] == name][0]
    return clone_list(pizza)


# this allows the program to find different toppings from the list
def find_topping_by_name(name, toppings):
    """Find the name of a topping

    :param name: string
    :param toppings: list
    :return: [x for x in toppings if x[0] == name][0]
    """
    return [x for x in toppings if x[0] == name][0]


# this allows the program to find different options from the list
def find_option_by_name(name, options):
    """Find the name of an option

    :param name: string
    :param options: list
    :return: [x for x in options if x[0] == name][0]
    """
    return [x for x in options if x[0] == name][0]


# this allows for the program to insert things into the list at a certain index
def clone_list(array):
    """Insert information into list

    :param array: list
    :return: array
    """
    return array[:]


# this function allows the user to see previous orders under the same phone number
def show_previous_orders(current_order, orders, pizza_list):
    """Show user previous orders

    :param current_order: list
    :param orders: list
    :param pizza_list: list
    :return: show_previous_orders(current_order, orders, pizza_list)
    """
    print_current_order(current_order)
    # formatting
    print("_" * 47)
    print("         PREVIOUS ORDERS")
    print("_" * 47)

    # if there are no previous orders with the same phone number, a helpful error message is printed
    if orders is None:
        print("There are no previous orders")
        return

    # the index means the user can select the number of a pizza so they can re-order
    index = 0
    for o in orders:
        index += 1
        # this prints out the list of previously ordered pizzas
        print("({}) {}: ${}  (Name: {})".format(index, o["date"], o["cost"], o["name"]))
        for p in o["items"]:
            # this finds if there were any toppings or options included in the order
            pizza_type = find_pizza_by_name(p[0], pizza_list)
            toppings = p[2] if len(p[2]) > 0 else pizza_type[2]
            print("{:<4} {}: {} (Toppings: {}) (Options: {})".format(" ", p[0], p[1], toppings, p[3]))
        print("_" * 47)

    # this asks the user if they want to order one of the pizzas or if they want to exit
    reorder = get_integer(
        "Enter the order number to add to your current order or 0 to exit: -> "
    )
    # they are returned to the main menu
    if reorder == 0:
        return current_order

    # if they enter a valid number that pizza is added to their order
    if 0 < reorder <= len(orders):
        order = orders[reorder - 1]
        # if the total number of pizzas ordered exceeds 10, they are informed that their order is maxed
        if (len(current_order["items"]) + len(order["items"])) > MAX_ORDER_SIZE:
            print("We have a maximum order size of {} items. Please remove some pizzas first".format(MAX_ORDER_SIZE))
            return current_order
        # the pizza they selected in added to items
        else:
            for p in order["items"]:
                menu_pizza = find_pizza_by_name(p[0], pizza_list)
                current_order["items"].append([menu_pizza[0], menu_pizza[1], p[2], p[3]])

        # if problem, the previous orders function is printed again
        return show_previous_orders(current_order, orders, pizza_list)
    else:

        # if they enter in a number less than or more than the options, they are asked to try again
        print("Invalid input")
        return show_previous_orders(current_order, orders, pizza_list)


# this function falls under the customise option, and is how the toppings and options are printed
# pizza[0] is the name of the pizza, pizza[1] is the current price,
# pizza[2] is the toppings, and pizza[3] is the options
def print_toppings(pizza, toppings, options):
    """Print topping and options list

    :param pizza: list
    :param toppings: list
    :param options: list
    :return: None
    """
    # formatting and how the topping choices are printed out
    print("_" * 47)
    print("      TOPPINGS")
    print("_" * 47)
    index = 0
    # prints all the pizza toppings in the toppings list
    # and checks the pizza to decide if that topping has been selected or not
    # https://overiq.com/python-101/strings-in-python/ (the website i used for the crosses)
    for x in toppings:
        index += 1
        selected = "X" if x[0] in pizza[2] else " "  # is checking if the topping name is in the toppings list
        print("{}. ({}) ${:<5}: {}".format(index, selected, x[1], x[0]))

    # formatting and how the option choices are printed out
    print("_" * 47)
    print("      OPTIONS")
    print("_" * 47)
    # prints all the pizza options in the options list
    # and checks the pizza to decide if that option has been selected or not
    for x in options:
        index += 1
        selected = "X" if x[0] in pizza[3] else " "  # empty string using double quote
        print("{}. ({}) ${:<5}: {}".format(index, selected, x[1], x[0]))


# this function is for updating the costs for any toppings or options selected
def update_cost_for_toppings(pizza, menu_pizza, toppings, options):
    """Update the cost of the toppings and options

    :param pizza: list
    :param menu_pizza: list
    :param toppings: list
    :param options: list
    :return: pizza
    """
    # pizza is the current selected pizza from your order,
    # menu_pizza is the same pizza from the original menu / pizza list,
    # toppings are all the toppings available, and options are all the options available

    # both missing toppings and new toppings are compared to the previous pizza
    # missing toppings are the toppings that have been removed
    missing_toppings = list(set(menu_pizza[2]) - set(pizza[2]))
    # new toppings are the toppings that have been added
    new_toppings = list(set(pizza[2]) - set(menu_pizza[2]))

    # find how much money to subtract from the current pizza price
    subtract = 0
    for s in missing_toppings:
        topping = find_topping_by_name(s, toppings)
        subtract += topping[1]

    # the new toppings are added to the current pizza price
    add = 0
    for a in new_toppings:
        topping = find_topping_by_name(a, toppings)
        add += topping[1]

    # the new options are added to the current pizza price
    options_cost = 0
    for o in pizza[3]:
        opt = find_option_by_name(o, options)
        options_cost += opt[1]

    # price is calculated by taking the menu_pizza price, subtracting the missing toppings price,
    # and adding the new toppings cost + options_cost
    pizza[1] = (menu_pizza[1] - subtract) + add + options_cost

    return pizza


# this function is for customising a pizza once the user picks a pizza to customise
def customise_pizza(pizza, toppings, options, pizza_list):
    """Customise a chosen pizza

    :param pizza: list
    :param toppings: list
    :param options: list
    :param pizza_list: list
    :return: customise_pizza(pizza, toppings, options, pizza_list)
    """
    print_toppings(pizza, toppings, options)
    # pizza is the pizza in current order selected in the customise_order method, toppings are the toppings available,
    # options are the options available, pizza_list is the list of pizzas available to order

    choice = get_integer("Please pick a topping or option to toggle it (0 to exit): -> ")

    # the menu_pizza / previous orders were being changed when customising the toppings/options
    # so the new list is cloned
    # this means the users changes are updated each time and will be modified everywhere
    pizza_toppings = clone_list(pizza[2])
    pizza_options = clone_list(pizza[3])

    # if the user selects quit, they are returned to the main menu
    if choice == 0:
        return pizza
    # searches for the pizza name off the pizza_list
    menu_pizza = find_pizza_by_name(pizza[0], pizza_list)
    # change the toppings based on the number selected
    if 0 < choice <= len(toppings):
        # idx stands for the index in the respective lists
        idx = choice - 1

        # the try and except try to remove the selected topping from the list
        try:
            index = pizza_toppings.index(toppings[idx][0])
            del pizza_toppings[index]
        # if the topping isn't selected, it is added and vise versa
        except ValueError:
            pizza_toppings.append(toppings[idx][0])
        # whenever pizza[2] is called it refers to pizza toppings
        pizza[2] = pizza_toppings
        # update the new cost for toppings
        pizza = update_cost_for_toppings(pizza, menu_pizza, toppings, options)

    # change the options based on the number selected
    # needs to be toppings + options, as the options are listed bellow the toppings when printed
    elif choice <= len(toppings) + len(options):
        idx = (choice - len(toppings)) - 1
        # the try and except try to remove the selected options from the list
        try:
            index = pizza_options.index(options[idx][0])
            del pizza_options[index]
        #  if the topping isn't selected, it is added and vise versa
        except ValueError:
            pizza_options.append(options[idx][0])
        # whenever pizza[3] is called it refers to pizza options
        pizza[3] = pizza_options
        # update the new cost for toppings
        pizza = update_cost_for_toppings(pizza, menu_pizza, toppings, options)
    # helpful error message if the user enters a number greater or less than the toppings+options
    else:
        print("You have to enter a number between 0 and {}".format(len(toppings + options)))
    # returned to the customise pizza menu until the user selects 0 to quit
    return customise_pizza(pizza, toppings, options, pizza_list)


# this function is for customising a pizza
def customise_order(current_order, toppings, options, pizza_list):
    """Choose a pizza to customise

    :param current_order: list
    :param toppings: list
    :param options: list
    :param pizza_list: list
    :return: customise_order(current_order, toppings, options, pizza_list)
    """
    print_current_order(current_order)

    # if the user hasn't ordered a pizza yet, the program will inform them that they need to order a pizza first
    if len(current_order["items"]) == 0:
        print("There are no pizzas to customise")
        # the user is returned to the main menu
        return current_order

    # message asking the user to choose a pizza to customise (only is printed if there is a pizza to choose from)
    choice = get_integer("Please pick a pizza you want to customise (0 to exit): -> ")

    # if the user selects quit, they are returned to the main menu
    if choice == 0:
        return current_order

    # if the user selects one of the pizzas in the order (current_order["items"])
    # that item is updated with the result from the customize_pizza method
    if 0 < choice <= len(current_order["items"]):
        current_order["items"][choice-1] = customise_pizza(current_order["items"][choice-1], toppings, options, pizza_list)
    # helpful error message if the user enters a number greater or less than the items (pizzas)
    else:
        print("You have to enter a number between 0 and {}".format(len(current_order["items"])))

    # the current_order is returned to the main menu
    return customise_order(current_order, toppings, options, pizza_list)


# limits the amount of pizzas the user can order to 10
MAX_ORDER_SIZE = 10


def main():
    """Main function for ordering pizzas

    :rtype: object
    """
    # all order history is stored here
    all_orders = {}

    # main menu list
    menu_list = [
        ["P", "Pizza Menu"],
        ["T", "Change order type (Delivery/Pickup)"],
        ["O", "Order Pizzas"],
        ["R", "Remove Pizzas"],
        ["C", "Customise Pizza"],
        ["CH", "Checkout"],
        ["CO", "Print Current Order"],
        ["PO", "Previous Orders"],
        ["Q", "Quit"]
    ]

    # list of all possible toppings
    toppings_list = [
        ["Marinara Sauce", 1.00],
        ["White Sauce", 3.00],
        ["Arugula", 1.50],
        ["Anchovies", 2.50],
        ["Basil", 1.00],
        ["Capsicum", 1.00],
        ["Cheddar", 1.50],
        ["Chicken", 2.50],
        ["Feta", 2.00],
        ["Ham", 1.50],
        ["Mozzarella", 1.00],
        ["Mushrooms", 1.50],
        ["Olives", 2.00],
        ["Pineapple", 1.50],
        ["Pesto", 2.00],
        ["Pepperoni", 2.00],
        ["Salami", 1.00],
        ["Tomato", 1.00],
    ]

    # list of all possible options
    options_list = [
        ["Gluten Free", 3.00],
        ["Thin Crust", 2.00],
        ["Stuffed Crust", 2.00]
    ]

    # list of all the pizzas the user can choose from
    pizza_list = [
        ["Cheese Pizza", 18.50, ["Marinara Sauce", "Mozzarella"], []],
        ["Pepperoni Pizza", 18.50, ["Marinara Sauce", "Mozzarella", "Pepperoni"], []],
        ["Hawaiian Pizza", 18.50, ["Marinara Sauce", "Mozzarella", "Ham", "Pineapple"], []],
        ["Veggie Pizza", 18.50,
         ["Marinara Sauce", "Mozzarella", "Feta", "Mushrooms", "Tomato", "Capsicum", "Basil"], []],
        ["Meat Lover's Pizza", 18.50, ["Marinara Sauce", "Mozzarella", "Pepperoni", "Ham", "Salami"], []],
        ["Margherita Pizza", 18.50, ["Marinara Sauce", "Mozzarella", "Basil", "Tomato"], []],
        ["BBQ Chicken Pizza", 18.50, ["Marinara Sauce", "Mozzarella", "Chicken", ], []],
        ["Wood-Fired Margherita Pizza", 25.50, ["Marinara Sauce", "Mozzarella", "Capsicum", "Pepperoni"], []],
        ["Three-Cheese White Sauce Pizza", 25.50, ["White Sauce", "Mozzarella", "Cheddar", "Feta"], []],
        ["Gourmet Pesto Pizza", 25.50, ["White Sauce", "Mozzarella", "Pesto", "Arugula"], []]
    ]

    confirmed_orders = []
    print("_" * 47)
    print("Welcome to Mymyz Pizzeria")
    print("_" * 47)

    current_order, previous_orders = create_new_order(all_orders)
    run_program = True
    while run_program:
        for x in menu_list:
            output = "{:>2}: {}".format(x[0], x[1])
            print(output)
        print("_" * 47)
        user_choice = get_formatted_string("Please select an option: -> ")
        print("_" * 47)
        if user_choice == "P":
            print_menu(pizza_list)
        elif user_choice == "O":
            order_pizza(current_order, pizza_list)
        elif user_choice == "CO":
            print_current_order(current_order)
        elif user_choice == "PO":
            show_previous_orders(current_order, previous_orders, pizza_list)
        elif user_choice == "R":
            remove_pizza(current_order)
        elif user_choice == "T":
            current_order = pick_order_type(current_order)
        elif user_choice == "C":
            current_order = customise_order(current_order, toppings_list, options_list, pizza_list)
        elif user_choice == "CH":
            confirmed = confirm_order(current_order)
            if confirmed:
                # this is to categorise as an old previous user, or make a new user (both through phone number)
                if previous_orders is None:
                    all_orders[current_order["phone"]] = [current_order]
                else:
                    all_orders[current_order["phone"]].append(current_order)
                # asks the user if they want to make a new order
                confirm = ask_yes_no(
                   "Would you like to make another order, enter Y for yes and N for no: -> ")
                # if they want to, a new order is started and added to all_orders
                if confirm:
                    current_order, previous_orders = create_new_order(all_orders)
                # if they don't want to, the program ends
                else:
                    run_program = False
                    print(all_orders)
                    print("_" * 47)
                    print("Thank you for using Mymyz Pizzeria's program")
                    print("_" * 47)
                    exit()
        elif user_choice == "Q":
            run_program = False
            print(all_orders)
            print("_" * 47)
            print("Thank you for using Mymyz Pizzeria's program")
            print("_" * 47)
            exit()
        else:
            print("Unrecognised entry")

        print("_" * 47)
        print("Thank you, please select from the following options menu")
        print("_" * 47)

if __name__ == "__main__":
    main()