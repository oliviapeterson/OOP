import joesautoclass as j

def main():
    #Customer
    name = input('Enter your name: ')
    add = input('Enter your address: ')
    phone = input('Enter cellphone number: ')
    #Car
    make = input('Enter the car make: ')
    model = input('Enter car model: ')
    year = input('Enter car year: ')
    #Servicequote
    quote = j.ServiceQuote(500,250)

    quote.get_sales_tax

    #execution
    print()
    print()
    print(f'Customer info: {name}: {add}, {phone}')
    print('Make: ', make)
    print(f'Model/Year: {model}/{year}')
    print('Service quote: ')
    print(f'Parts charge.....${quote.get_parts_charges()}')
    print(f'Service charge...${quote.get_labor_charges()}')
    print(f'Sales Tax........${quote.get_sales_tax()}')
    print('-----------------------')
    print(f'Total Charges:   ${quote.get_total_charges():,.2f}')


main()