# allows for the order history to have a accurate date
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
        elif re.match(r"^(021|022|027)", str) and (len(str) < 10 or len(str) > 11):
            valid = False
    else:
        valid = False

    if valid:
        return str
    else:
        print("This doesn't appear to be a valid phone number")
        return pick_phone()


def validate_name(name):
    if len(name) < 2 or len(name) > 30:
        print("The name must be between 2 and 30 characters.")
        return pick_name()
    else:
        return name


def validate_address(addr):
    if len(addr) < 10 or len(addr) > 60:
        print("The addresss must be between 10 and 60 characters")
        return pick_address()
    else:
        return addr




def get_integer(m, min=0, max=999999):
    getting_user_integer = True
    while getting_user_integer:
        try:
            user_input = int(input(m))
        except ValueError:
            print("Please type a number: -> ")
            continue

        if user_input < min or user_input > max:
            print("Please type a number: -> ")
            continue

        getting_user_integer = False

    return user_input


def get_string(m):
    user_input = input(m).strip()
    return user_input


def get_formatted_string(m):
    user_input = input(m)
    return user_input.upper().strip()



def pick_name():
    name = get_string("What is your name: -> ")
    return validate_name(name)


def pick_phone():
    phone = get_string("What is your phone number: -> ")
    validate_phone(phone)
    return phone

def pick_address():
    address = get_string("What is your address (Street Number, Street Name, Suburb): -> ")
    return validate_address(address)



# function that prints out the pizza menu
def print_menu(L):
    print("    Cost         Type")
    index = 0
    for x in L:
        index += 1
        output = "({}) ${:<7} --- {:>4}".format(index, x[1], x[0])
        print(output)
    return None




# def review_order(L):
    # print("Quantity    Cost     Type")
    # for x in L:
        # output = "{:<6} ---- ${:>4} -- {:<6}".format(x[1], x[2], x[0])
        # print(output)
    # return None





# validation for (Y)es and (N)o questions
def ask_yes_no(m):
    ask_again = get_formatted_string(m)
    if ask_again == "Y":
        return True
    elif ask_again == "N":
        return False
    else:
        print("Enter Y/N")
        return ask_yes_no(m)





def print_current_order(current_order):
    # main portion of the programs cost feature
    cost = 0
    for x in current_order["items"]:
        cost += x[1]

    is_delivery = current_order["type"] == "Delivery"
    if is_delivery:
        cost += 3

    # formating so the code prints nicely
    print("_" * 47)
    print("         CURRENT ORDER")
    print("Name: {}    --   Phone: {}    --   Order Type: {}".format(current_order["name"], current_order["phone"], current_order["type"]))
    print("Total: ${}".format(cost))
    print("   == Pizza ==")

    current_order["cost"] = cost
    pizzas = current_order["items"]
    if len(pizzas) == 0:
        print("You have not selected any pizzas")
    else:
        for i in range(0, len(pizzas)):
            output = "{}: ${} - {} (Toppings: {}) (Options: {})".format(
                i+1,
                pizzas[i][1],
                pizzas[i][0],
                pizzas[i][2] if len(pizzas[i][2]) > 0 else "No changes",
                pizzas[i][3] if len(pizzas[i][3]) > 0 else "None selected"
            )
            print(output)
    if is_delivery:
        print("Delivery: $3.00")





def order_pizza(current_order, pizza_list):
    max_order = 10

    max_input = len(current_order)
    print_menu(pizza_list)
    print_current_order(current_order)

    choice = get_integer(
        "Please pick a pizza from the menu (0 to skip): -> ", 0, max_input)

    if choice == 0:
        return current_order
    elif 0 < choice <= max_input:
        pizza = clone_list(pizza_list[choice-1])
        current_order["items"].append(pizza)

        again = ask_yes_no("Would you like to order another pizza (Y/N): ->")
        if again:
            return order_pizza(current_order, pizza_list)
        else:
            return current_order

    else:
        print("You have to enter a number between 1 and {}".format(len(L)-1))
        return order_pizza(current_order, pizza_list)





def remove_pizza(current_order):
    print_current_order(current_order)

    if len(current_order["items"]) == 0:
        print("There are no more pizzas to remove")
        return current_order
    choice = get_integer("Please pick a pizza you want to remove (0 to exit): -> ")

    if choice == 0:
        return current_order
    elif 0 < choice <= len(current_order["items"]):
        del current_order["items"][choice-1]
        return remove_pizza(current_order)
    else:
        print("You have to enter a number between 0 and {}".format(len(current_order["items"])))
        return remove_pizza(current_order)





def create_new_order(all_orders):
    current_order = {
        "date": date.today().isoformat(),
        "name": "",
        "type": "",
        "items": []
    }
    current_order = pick_order_type(current_order)
    try:
        previous_orders = all_orders[current_order['phone']]
    except KeyError:
        previous_orders = None

    return current_order, previous_orders





def pick_order_type(current_order):
    service = get_formatted_string(
        "Would you like (D)elivery or (P)ickup or (C)hoose Later (D/P/C): -> ")

    if service == "D":
        current_order["name"] = pick_name()
        current_order["phone"] = pick_phone()
        current_order["address"] = pick_address()
        current_order["type"] = "Delivery"
        print("_" * 47)
        return current_order
    elif service == "P":
        current_order["name"] = pick_name()
        current_order["phone"] = pick_phone()
        current_order["address"] = ""
        current_order["type"] = "Pickup"
        print("_" * 47)
        return current_order
    elif service == "C":
        print("You have selected to choose Deliver or Pickup later")
        current_order["name"] = pick_name()
        current_order["phone"] = pick_phone()
        current_order["type"] = "Not yet selected"
        print("_" * 47)
        return current_order
    else:
        print("Unrecognised entry")
        return pick_order_type(current_order)


def confirm_order(current_order):
    print_current_order(current_order)

    if len(current_order["items"]) == 0:
        return False

    if current_order["type"] == "Not yet selected":
        service = get_formatted_string(
            "Please select either (D)elivery or (P)ickup (D/P): -> ")
        if service == "D":
            current_order["address"] = pick_address()
            current_order["type"] = "Delivery"
            print("You have selected Delivery")
            print("_" * 47)
        elif service == "P":
            current_order["type"] = "Pickup"
            print("You have selected Pickup")
            print("_" * 47)

    confirm = ask_yes_no("Would you like to confirm your order, enter Y for yes and N for no: -> ")
    if confirm:
        print("Thank you for your order, it will be ready soon")
        print("_" * 47)
        print("_" * 47)
        return True

    return False





def find_pizza_by_name(name, pizza_list):
    pizza = [x for x in pizza_list if x[0] == name][0]

    return clone_list(pizza)


def find_topping_by_name(name, toppings):
    return [x for x in toppings if x[0] == name][0]


def find_option_by_name(name, options):
    return [x for x in options if x[0] == name][0]


def clone_list(array):
    return array[:]





def show_previous_orders(current_order, orders, pizza_list):
    print_current_order(current_order)

    print("_" * 47)
    print("         PREVIOUS ORDERS")
    print("_" * 47)

    if orders is None:
        print("There are no previous orders")
        return

    index = 0
    for o in orders:
        index += 1
        print("({}) {}: ${}  (Name: {})".format(index, o["date"], o["cost"], o["name"]))
        for p in o["items"]:
            pizza_type = find_pizza_by_name(p[0], pizza_list)
            toppings = p[2] if len(p[2]) > 0 else pizza_type[2]
            print("{:<4} {}: {} (Toppings: {}) (Options: {})".format(" ", p[0], p[1], toppings, p[3]))
        print("_" * 47)

    reorder = get_integer(
        "Enter the order number to add to your current order or 0 to exit: -> "
    )
    if reorder < 0 and reorder >= len(orders):
        print("Invalid input")
        show_previous_orders(current_order, orders, pizza_list)
    elif reorder > 0:
        order = orders[reorder-1]
        for p in order["items"]:
            menu_pizza = find_pizza_by_name(p[0], pizza_list)
            current_order["items"].append([menu_pizza[0], menu_pizza[1], p[2], p[3]])

        show_previous_orders(current_order, orders, pizza_list)
    return





def print_toppings(pizza, toppings, options):
    print("_" * 47)
    print("      TOPPINGS")
    print("_" * 47)
    index = 0
    for x in toppings:
        index += 1
        selected = "X" if x[0] in pizza[2] else " "
        print("{}. ({}) ${:<5}: {}".format(index, selected, x[1], x[0]))

    print("_" * 47)
    print("      OPTIONS")
    print("_" * 47)
    for x in options:
        index += 1
        selected = "X" if x[0] in pizza[3] else " "
        print("{}. ({}) ${:<5}: {}".format(index, selected, x[1], x[0]))





def update_cost_for_toppings(pizza, menu_pizza, toppings, options):
    missing_toppings = list(set(menu_pizza[2]) - set(pizza[2]))

    new_toppings = list(set(pizza[2]) - set(menu_pizza[2]))

    subtract = 0
    for s in missing_toppings:
        topping = find_topping_by_name(s, toppings)
        subtract += topping[1]

    add = 0
    for a in new_toppings:
        topping = find_topping_by_name(a, toppings)
        add += topping[1]

    options_cost = 0
    for o in pizza[3]:
        opt = find_option_by_name(o, options)
        options_cost += opt[1]

    pizza[1] = (menu_pizza[1] - subtract) + add + options_cost

    print(add, subtract)

    return pizza





def customise_pizza(pizza, toppings, options, pizza_list):
    print_toppings(pizza, toppings, options)

    choice = get_integer("Please pick a topping or option to toggle it (0 to exit): -> ")

    pizza_toppings = clone_list(pizza[2])
    pizza_options = clone_list(pizza[3])

    if choice == 0:
        return pizza
    menu_pizza = find_pizza_by_name(pizza[0], pizza_list)
    if 0 < choice <= len(toppings):
        idx = choice - 1
        try:
            index = pizza_toppings.index(toppings[idx][0])
            del pizza_toppings[index]
        except ValueError:
            pizza_toppings.append(toppings[idx][0])

        pizza[2] = pizza_toppings
        pizza = update_cost_for_toppings(pizza, menu_pizza, toppings, options)
    elif choice <= len(toppings) + len(options):
        idx = (choice - len(toppings)) - 1
        try:
            index = pizza_options.index(options[idx][0])
            del pizza_options[index]
        except ValueError:
            pizza_options.append(options[idx][0])
        pizza[3] = pizza_options
        pizza = update_cost_for_toppings(pizza, menu_pizza, toppings, options)
    else:
        print("You have to enter a number between 0 and {}".format(len(toppings + options)))

    return customise_pizza(pizza, toppings, options, pizza_list)





def customise_order(current_order, toppings, options, pizza_list):
    print_current_order(current_order)

    if len(current_order["items"]) == 0:
        print("There are no pizzas to customise")
        return current_order

    choice = get_integer("Please pick a pizza you want to customise (0 to exit): -> ")

    if choice == 0:
        return current_order

    if 0 < choice <= len(current_order["items"]):
        current_order["items"][choice-1] = customise_pizza(current_order["items"][choice-1], toppings, options, pizza_list)
    else:
        print("You have to enter a number between 0 and {}".format(len(current_order["items"])))

    return customise_order(current_order, toppings, options, pizza_list)





def create_customer_list():
    return [
        ["Cheese", 0, 18.50],
        ["Hawaian", 0, 18.50],
        ["Pepperoni ", 0, 18.50],
        ["Meat Lover's", 0, 25.50],
        ["Veggie", 0, 25.50]
    ]


def main():
    all_orders = {
        "444": [{
            "date": "2020-01-01",
            "name": "Maya Catley",
            "phone": "022 311 5133",
            "address": "",
            "cost": 44.50,
            "type": "Pickup",
            "items": [
                ["Cheese", 18.50, ["Cheese", "Feta"], []],
                ["Veggie", 24.00, [
                    "Cheese",
                    "Feta",
                    "Mushrooms",
                    "Tomato",
                    "Olives",
                    "Artichoke"
                ], []]
            ]
        }],
    }

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

    toppings_list = [
        ["Cheese", 1.50],
        ["Ham", 1.50],
        ["Pineapple", 1.50],
        ["Pepperoni", 2.00],
        ["Salami", 3.00],
        ["Meatballs", 2.50],
        ["Anchovies", 2.00],
        ["Mushrooms", 1.50],
        ["Olives", 2.00],
        ["Tomato", 1.00],
        ["Capsicum", 1.00],
        ["Artichoke", 2.00],
        ["Feta", 2.00],
    ]

    options_list = [
        ["Gluten Free", 3.00],
        ["Thin Crust", 2.00],
    ]

    pizza_list = [
        ["Cheese", 16.50, ["Cheese"], []],
        ["Pepperoni", 18.50, ["Cheese", "Pepperoni"], []],
        ["Hawaian", 20.00, ["Cheese", "Ham", "Pineapple"], []],
        ["Veggie", 24.00, ["Cheese", "Feta", "Mushrooms", "Tomato", "Capsicum", "Artichoke"], []],
        ["Meat Lover's", 25.50, ["Cheese", "Pepperoni", "Ham", "Salami", "Meatballs"], []],
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
                if previous_orders is None:
                    all_orders[current_order["phone"]] = [current_order]
                else:
                    all_orders[current_order["phone"]].append(current_order)

                confirm = ask_yes_no(
                   "Would you like to make another order, enter Y for yes and N for no: -> ")
                if confirm:
                    current_order, previous_orders = create_new_order(all_orders)
                    print(previous_orders)
                else:
                    run_program = False

        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")

        print("_" * 47)
        print("Thank you, please select from the following options menu")
        print("_" * 47)
if __name__ == "__main__":
    main()