import CellPhoneClass as cp
def main():
    man = input('Enter the cellphone manufacter: ')
    mod = input('Enter cellphone model: ')
    price = input('Enter cellphone price: ')
    
    cellphone_info = cp.cellphone(man,mod, 999)

    #call the set price
    print(f"Manufacturer: {cellphone_info.get_manufact()}")
    print(f"Model: {cellphone_info.get_model()}")
    print(f"Retail Price: ${cellphone_info.get_retail_price()}") #validate?

main()