from warehouse import items, sold_items
import csv



def export_items_to_csv():
    with open('dane/magazyn.csv','w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'quantity', 'unit', 'unit_price'])
        writer.writeheader()
        for i in list(items):
            writer.writerow({'name': i['name'],'quantity': i['quantity'],'unit': i['unit'],'unit_price': i['unit_price']})
        
    print("Successfully exported data to magazyn.csv")


def export_sales_to_csv():
    with open('dane/sale_magazyn.csv','w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'quantity', 'unit', 'unit_price'])
        writer.writeheader()
        for i in list(sold_items):
            writer.writerow({'name': i['name'],'quantity': i['quantity'],'unit': i['unit'],'unit_price': i['unit_price']})
        

def load_items_from_csv(path= 'dane/magazyn.csv'):
    items.clear()
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append({
                'name': row['name'], 
                'quantity': row['quantity'], 
                'unit': row['unit'], 
                'unit_price': row['unit_price']
                })
    print("Successfully loaded data from magazyn.csv")