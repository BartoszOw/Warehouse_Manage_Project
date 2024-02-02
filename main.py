from warehouse import get_items, add_items, sell_items, show_revenue


while True:
    question = input("What would u like to do? ")

    if question == "exit":
        print("Exiting... Bye!")
        break
    if question == "show":
        get_items()
    if question == "add":
        add_items()
    if question == "sell":
        sell_items()
    if question == "show_revenue":
        show_revenue()