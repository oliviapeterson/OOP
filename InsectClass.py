import random

class insect:
    def __init__(self, w,l,n):
        self.wings = w
        self.legs = l
        self.mileage = 0
        self.name = n
#self argument ensures that only attributes of a single item in a class is being changed
    def calc_miles(self): #aka a mutable method; it is being changed
         self.mileage = random.randint(1,11) 

    def get_miles(self): #get functions access
        return self.mileage
    
    def get_name(self):
        return self.name
       
