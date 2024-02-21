import random

class insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.mileage = 0

    def calc_miles(self):
         self.mileage = random.randint(1,11)

    def get_miles(self):
        return self.mileage
       
