'''
23. Notification System
Abstract:
Notification
Derived:
EmailNotification
SMSNotification
PushNotification
'''
from abc import *
class Notification(ABC):
    @abstractmethod
    def sound(self):
        pass
class Email(Notification):
    def sound(self):
        print("Ring")

class SMS(Notification):
    def sound(self):
        print("Bell")

class Push(Notification):
    def sound(self):
        print("sound")

p = Push()
p.sound()
s = SMS()
s.sound()