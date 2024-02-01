
# Poczatkowa lista towaru

items = [{
    'name': 'Bułka',
    'quantity': 5000,
    'unit': 'kg',
    'unit_price': 2.5
}, 
{
    'name': 'Chleb',
    'quantity': 1111,
    'unit': 'kg',
    'unit_price': 1
},
{
    'name': 'Mleko',
    'quantity': 150,
    'unit': 'l',
    'unit_price': 4
},
{
    'name': 'Kawa',
    'quantity': 68,
    'unit': 'kg',
    'unit_price': 10
}]

# Sprzedane towary(lista)

sold_items = []



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
        'quantity': quantity,
        'unit': unit_name,
        'unit_price': unit_price
    })
    print("Successfully added to warehouse. Current Status:")
    get_items()
    
# Sprzedaż towaru

def sell_items():
    
    name = input("Item Name: ")
    quantity = input("Quantity to sell: ")

    for i in list(items):
        if i['name'] == name:
            i['quantity'] -= int(quantity)
            if i['quantity'] == 0:
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
