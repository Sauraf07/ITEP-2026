class Rectangle:
    def set_length(self,length):
        self.length = length
    def set_Width(self,width):
        self.width = width
    def Area(self):
        print(f"Area of a circle {2*self.length*self.width}")

r1 = Rectangle()
r1.set_length(10)
r1.set_Width(6)
r1.Area()