import csv

class Product:
    def __init__(self, name, quantity, unit, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.unit_price = unit_price
       
    def __str__(self):
        return F"Product: {self.name}, Unit: {self.unit}, Unit Price: {self.unit_price}, Quantity: {self.quantity}"
    
    def total_price(self):
        return self.unit_price * self.quantity

    def increase_quantity(self, amount):
        self.quantity += amount

    def decrease_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print("Error: Not enough quantity available.")

def load_products_from_csv(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = Product(row['name'], row['unit'], row['unit_price'], row['quantity'])
            products.append(product)
    return products
# Poczatkowa lista towaru
items = []

# Wyswietlanie towaru

def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t--------\t----\t----------")

    for i in list(items):
        print(f"{i.get('name')}\t{i.get('quantity')}\t\t{i.get('unit')}\t{i.get('unit_price')}")

# Dodawanie Towaru
        
def add_items():

    print("Adding to warehouse...")

    name = input("Item Name: ")
    quantity = input("Item quantity: ")
    unit_name = input("Item unit of measure: Eg, l, kg : pcs: ")
    unit_price = input("Item price in PLN: ")

    items.append(
    {
        'name': name,
        'quantity': int(quantity),
        'unit': unit_name,
        'unit_price': float(unit_price)
    })
    print("Successfully added to warehouse. Current Status:")
    get_items()
    
# Sprzedaż towaru

sold_items = []


def sell_items():
    
    name = input("Item Name: ")
    quantity = int(input("Quantity to sell: "))

    for i in list(items):
        if i['name'] == name:
            i['quantity'] = int(i['quantity'])
            i['quantity'] -= quantity
            if i['quantity'] <= 0:
                items.remove(i)
            print(f"Successfully sold {quantity}{i['unit']} of {i['name']}")
            sold_items.append({
                'name': name,
                'quantity': quantity,
                'unit': i['unit'],
                'unit_price': i['unit_price']
            })
    get_items()
    print(sold_items)


# Pobieranie kosztów
    
def get_costs():

    costs_of_quantity = [int(i['quantity']) * float(i['unit_price']) for i in list(items) ]
    return sum(costs_of_quantity)

def get_income():

    income_of_quantity = [int(i['quantity']) * float(i['unit_price']) for i in list(sold_items) ]
    return sum(income_of_quantity)

# Pokazywanie kosztów

def show_revenue():
    print("Revenue breakdown (PLN)")
    print(f"Income: {str(get_income())}")
    print(f"Costs: {str(get_costs())}")
    print("----------")
    x = get_income() - get_costs()
    print(f"Revenue {x} PLN")