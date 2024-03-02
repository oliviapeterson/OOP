class Car:
    def __init__(self, y,m):
        self.__year_model = y
        self.__make = m
        self.__speed = 0

    def calc_accelerate(self):
        self.__speed += 5 
    
    def calc_brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed
    