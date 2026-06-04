from src.dao.employee_dao import EmployeeDao
from src.model.employee import Employee
while True:
    print("Press 1 for Insertion ")
    print("Press 2 for fatchall")
    print("Press 3 to Update")
    print("Press 4 to Delete")
    print("Press 5 to fetch by Id")
    print("Press 0 to exit")
    choice = input("Enter your choice: ")

    if choice == 1:
        name = input("Enter your name: ")
        salary = float(input("Enter your salary: "))
        age = int(input("Enter your age: "))
        skill = (input("Enter your skill: "))
        department = (input("Enter your department: "))
        employee = Employee(name,salary,age,skill,department)
        if EmployeeDao.save_employee(employee):
            print("Employee saved")
        else:
            print("!SomeThing went wrong")
    elif choice == 2:
        EmployeeDao.get_employee(employee)
        

