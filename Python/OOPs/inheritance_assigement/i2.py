'''2. Vehicle System

Create parent class Vehicle.

Child classes:

Car
Bike
Bus

Add methods:

start()
stop()
'''

class Vehical:
    def start(self):
        print("Engine started..")

    def stop(self):
        print("Engine stop")

class Car(Vehical):
    def start(self):
        return super().start()

    def stop(self):
        return super().stop()
    
class Bike(Vehical):
    def start(self):
        return super().start()

    def stop(self):
        return super().stop()
    
class Bus(Vehical):
    def start(self):
        return super().start()

    def stop(self):
        return super().stop()
    
c = Car()
c.start()
c.stop()
