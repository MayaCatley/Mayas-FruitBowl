def get_formatted_string(m):
    user_input = input(m)
    return user_input.upper().strip()

def ask_yes_no(m):
    ask_again = get_formatted_string(m)
    if ask_again == "Y":
        return True
    elif ask_again == "N":
        return False
    else:
        print("Enter Y/N")
        return ask_yes_no(m)

if __name__=="__main__":
    x = ask_yes_no("Please confirm(Y/N) -> ")
    print(x)




