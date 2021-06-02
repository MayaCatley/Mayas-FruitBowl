
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

def add_fruit(L):
    for i in range(0, len(L)):
        output = "{}: {} {}".format(i, L[i][0], L[i][1])
        print(output)
    choice = get_integer("Please pick a fruit you want to add too")

    quantity = get_integer("How many {} would you like to add".format(L[choice]))
    L[choice][1] += quantity
    print("You now have {}".format(L[choice]))

def main():
    fruit_list = [
        ["apples", 2],
        ["pears", 0],
        ["quinces", 3],
        ["lemons", 7]
]

    menu_list =[
        ["R" , "Reveiw Fruit"],
        ["A" , "Add Fruit"],
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
        elif user_choice == "A":
            add_fruit(fruit_list)
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")
        print("Thank you, the program has ended")

if __name__ == "__main__":
    main()

