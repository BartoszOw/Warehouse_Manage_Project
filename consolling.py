from warehouse import get_items, add_items, sell_items

def what_to_do():
    question = input("What would u like to do? ")

    if question == "exit":
        print("Exiting... Bye!")
    if question == "show":
        return get_items()
    if question == "add":
        return add_items()
    if question == "sell":
        return sell_items()