class Student:
    def set_name(self,name):
        self.name = name

    def set_mathMarks(self,mathMarks):
        self.mathMarks = mathMarks
    
    def set_scienceMarks(self,scienceMarks):
        self.scienceMarks = scienceMarks
    
    def Average(self):
        print(f"Name : {self.name}")
        print(f"Math Marks {self.mathMarks}")
        print(f"Science marks  : {self.scienceMarks}")
        print(f"Average : {(self.mathMarks+self.scienceMarks)/2}")

s1 = Student()
s1.set_name("Saurav")
s1.set_mathMarks(56)
s1.set_scienceMarks(35)
s1.Average()