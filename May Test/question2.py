'''Question 2 — Multilevel Inheritance
Create the following class hierarchy:
Person → Teacher → PythonTrainer
Requirements:
Person
variable: name
method: show_person()
Teacher
variable: subject
method: show_teacher()
PythonTrainer
variable: experience
method: show_trainer()
Create an object of PythonTrainer and display all details using inherited methods.'''
class Person:
    def __init__(self,name):
        self.__name = name

    def show_person(self):
        print(f"Name : {self.__name}")  

class Teacher(Person):
    def __init__(self,name,subject):
        self.__subject = subject
        super().__init__(name)

    def show_teacher(self):
        print(f"Subject : {self.__subject}")
        return super().show_person()

class PythonTrainer(Teacher):
    def __init__(self,name,subject,experience):
        self.__experience = experience
        super().__init__(name,subject)

    def show_trainer(self):
        print(f"Experience : {self.__experience} years")
        return super().show_teacher()
    
trainer = PythonTrainer("Saurav","Python",5)
trainer.show_trainer()
