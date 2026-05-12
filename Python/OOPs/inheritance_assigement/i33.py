'''
33. Smart Home Devices
Methods:
turn_on()
turn_off()
Implement:
SmartFan
SmartLight
SmartAC
'''
from abc import *
class HomeDevices(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class SmartFan(HomeDevices):
    def turn_off(self):
        print("Smart Fan Off")

    def turn_on(self):
       print("Smart fan On")

class SmartLight(HomeDevices):
    def turn_off(self):
        print("Smart light Off")

    def turn_on(self):
       print("Smart light On")

class SamrtAc(HomeDevices):
    def turn_off(self):
        print("Smart AC Off")

    def turn_on(self):
       print("Smart AC On")

sl = SmartLight()
sl.turn_off()
sl.turn_on()

