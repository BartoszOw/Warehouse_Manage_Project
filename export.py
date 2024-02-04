from warehouse import items, sold_items
import csv

def export_items_to_csv():
    with open('magazyn.csv','w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'quantity', 'unit', 'unit_price'])
        writer.writeheader()
        for i in list(items):
            writer.writerow({'name': i['name'],'quantity': i['quantity'],'unit': i['unit'],'unit_price': i['unit_price']})
        
    print("Successfully exported data to magazyn.csv")


def export_sales_to_csv():
    with open('sale_magazyn.csv','w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'quantity', 'unit', 'unit_price'])
        writer.writeheader()
        for i in list(sold_items):
            writer.writerow({'name': i['name'],'quantity': i['quantity'],'unit': i['unit'],'unit_price': i['unit_price']})
        
