class Mobile:
    def set_brand(self,brand):
        self.brand = brand
    def set_model(self,model):
        self.model = model
    def set_price(self,price):
        self.price = price
    
    def is_affortable(self):
        print(f"Brand {self.brand}")
        print(f"Model {self.model}")
        print(f"Price {self.price}")
        if self.price <20000:
            print(f"Affortable")
        print("Not Affortable")
m1 = Mobile()
m1.set_brand("Iphone")
m1.set_model("Iphone 14 pro")
m1.set_price(52222)
m1.is_affortable()