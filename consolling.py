from warehouse import get_items

def what_to_do():
    question = input("What would u like to do? ")

    if question == "exit":
        print("Exiting... Bye!")
    if question == "show":
        return get_items()