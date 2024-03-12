
class Customer:
    def __init__(self, n, a, p):
        self.__name = n
        self.__address = a
        self.__phone = p
#self argument ensures that only attributes of a single item in a class is being changed
    def set_name(self,name):
        self.__name = name

    def set_address(self, add):
          self.__address = add
    
    def set_phone(self, phone):
         self.__phone = phone
        
    def get_name(self):
         return self.__name
    
    def get_address(self):
         return self.__address
    
    def get_phone(self):
         return self.__phone
    
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def set_make (self, make):
         self.__make = make

    def set_model (self, model):
         self.__model = model
    
    def set_year(self, year):
         self.__year = year

    def get_make(self):
         return self.__make
    
    def get_model(self):
         return self.__model
    
    def get_model(self):
         return self.__year
    
class ServiceQuote:
    def __init__ (self, parts, labor):
         self.__parts_charges = parts
         self.__labor_charges = labor
    
    def set_parts_charges (self, parts):
         self.__parts_charges = parts

    def set_labor_charges(self, labor):
         self.__labor_charges = labor
    
    def get_parts_charges(self):
         return self.__parts_charges
    
    def get_labor_charges(self):
         return self.__labor_charges
    
    def get_sales_tax(self):
        taxrate = 0.0825
        sales_tax = (taxrate*self.__labor_charges) + (taxrate*self.__parts_charges)
        return sales_tax
    def get_total_charges(self):
        total = self.__labor_charges + self.__parts_charges + self.get_sales_tax()
        return total

