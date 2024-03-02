import CarClass

def main(): 
    year = input("Enter the car year: ")
    model = input("Enter the car model: ")
    my_car = CarClass.Car(year, model)
  
    i = 0
    while i <= 4:
        my_car.calc_accelerate()
        print("Accelerating...")
        print(f"Current Speed: {my_car.get_speed()}")

        i += 1

main()