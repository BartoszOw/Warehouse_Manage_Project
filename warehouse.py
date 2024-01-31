items = [{
    'name': 'Bułka',
    'quantity': 5,
    'unit': 'kg',
    'unit_price': 2.5
}, 
{
    'name': 'Chleb',
    'quantity': 10,
    'unit': 'kg',
    'unit_price': 1
},
{
    'name': 'Mleko',
    'quantity': 2,
    'unit': 'l',
    'unit_price': 4
},
{
    'name': 'Kawa',
    'quantity': 1,
    'unit': 'kg',
    'unit_price': 10
}]


def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t--------\t----\t----------")
    for i in len(items):
        print(items[i])
