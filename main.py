from warehouse import get_items, add_items, sell_items, show_revenue
from data_transfer import export_items_to_csv, export_sales_to_csv, load_items_from_csv
    
    
load_items_from_csv()
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
    if question == "save":
        export_items_to_csv()
        export_sales_to_csv()
    if question == "load":
        load_items_from_csv()
