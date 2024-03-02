from datetime import date

class StudentClasses:
    def __init__(self, i, n, dob, c):
        self.stuid = i
        self.name = n
        self.dob = dob
        self.classification = c
        self.__age = 0
        self.__register = ''
    def calc_age(self):
        current_year = date.today().year
        dob_year = int(self.dob.split("/")[-1])
        self.__age = (current_year - dob_year)

    def calc_registration(self):
        if self.classification == 'F':
            self.__register = '4/1 - 4/3'
        elif self.classification == 'S':
            self.__register = '4/4 - 4/6'
        elif self.classification == 'Jr':
            self.__register = '4/7-4/9'
        elif self.classification == 'Sr':
            self.__register = '4/10 - 4/12'
        else:
            print("Invalid classification.")
    
    def get_age(self):
        return self.__age
    
    def get_classification(self):
        return self.classification
    
    def get_registration(self):
        return self.__register
    

