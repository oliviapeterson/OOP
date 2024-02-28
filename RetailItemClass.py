class RetailItem:
    def __init__(self, d, u, p):
        self.description = d
        self.units = u
        self.price = p
    def get_description(self): #get functions access
        return self.description
    def get_units(self):
        return self.units
    def get_price(self):
        return self.price
    