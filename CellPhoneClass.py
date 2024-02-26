
class cellphone:
    def __init__(self, m, n, p):
        self.__manufact = m
        self.__model = n
        self.__retail_price = p
#self argument ensures that only attributes of a single item in a class is being changed
    def set_manufact(self, man): #aka a mutable method; it is being changed
         self.__manufact = man

    def set_model(self, mod): #get functions access
        self.__model = mod
    
    def set_retail_price(self, price):
        self.__retail_price = price

    def get_manufact(self):
        return self.__manufact
    
    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__retail_price
        