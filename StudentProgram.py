import StudentClass
#split dob
def main():
    stuid = input('Enter your student ID number: ')
    name = input('Enter first name: ')
    dob = input('Enter date of birth (MM/DD/YYYY): ').strip()
    classification = input('Enter classification(F, S, Jr, Sr): ')

    student = StudentClass.StudentClasses(stuid, name, dob, classification)
    student.calc_age()
    student.calc_registration()

    print()
    print("Student Report")
    print()
    print(f"Student Classification: {student.get_classification()}")
    print(f"Student Age: {student.get_age()}")
    print(f"Registration Period: {student.get_registration()}")
    
    
    
main()