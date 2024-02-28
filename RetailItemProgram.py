import RetailItemClass as ri
def main():
   item_one = ri.RetailItem('Jacket', 12, 59.95)
   item_two = ri.RetailItem('Designer Jeans', 40, 34.95)
   item_three = ri.RetailItem('Shirt', 20, 24.95)
   print(f"Item 1: {item_one.get_description()} {item_one.get_units()}, {item_one.get_price()}")
   print(f"Item 2: {item_two.get_description()} {item_two.get_units()}, {item_two.get_price()}")
   print(f"Item 3: {item_three.get_description()} {item_three.get_units()}, {item_three.get_price()}")
main()