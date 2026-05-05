class Circle:
    def set_area(self,area):
        self.area = area
    def Area(self):
        print(f"Area of a Circle : {22/7*(self.area*self.area)}")

    def Circumference(self):
        print(f"Circumference of a circle : {2*22/7*self.area}")

c1 = Circle()
c1.set_area(5)
c1.Area()
c1.Circumference()
