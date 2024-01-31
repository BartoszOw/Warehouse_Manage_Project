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


def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t--------\t----\t----------")

    for i in list(items):
        print(f"{i.get('name')}\t{i.get('quantity')}\t\t{i.get('unit')}\t{i.get('unit_price')}")
    
