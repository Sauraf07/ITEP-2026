'''
18. Vehicle Insurance System
Vehicle
InsuredVehicle
Car
Calculate insurance amount.
'''
class Vehical:
    def insurence(self):
        pass
class InsuredVehical(Vehical):
    def insurence(self):
        print("Vehical is insuresnd")
class Car(InsuredVehical):
    def insurence(self):
        return super().insurence()
    
c = Car()
c.insurence()