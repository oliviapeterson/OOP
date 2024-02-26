import Insects as i
#import the name of the FILE, not the class

mosquito = i.insect(2,4, 'Mosquito') #w, l, n are now set to these items
housefly = i.insect(2,4, 'Housefly')

mosquito.calc_miles()
housefly.calc_miles()

print(f"The {mosquito.get_name()} can travel up to {mosquito.get_miles()} miles")
print(f"The {housefly.get_name()} can travel up to {housefly.get_miles()} miles")
# The main function.

           

# Call the main function.

