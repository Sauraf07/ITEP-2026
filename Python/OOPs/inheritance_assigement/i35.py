'''
35. Messaging Application
Methods:
send_message()
Implement:
WhatsApp
Telegram
Signal
'''
from abc import *
class Application(ABC):
    @abstractmethod
    def send_message(self):
        pass
class WhatsApp(Application):
    def send_message(self):
        print("Message send by WhatsApp")

class Telegram(Application):
    def send_message(self):
        print("Message send by Telegram")
        
class Signal(Application):
    def send_message(self):
        print("Message send by signal")
m1 = WhatsApp()
m1.send_message()
m2 = Telegram()
m2.send_message()
m3 = Signal()
m3.send_message()
        