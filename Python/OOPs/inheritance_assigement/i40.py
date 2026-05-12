'''
40. AI Chatbot System
Methods:
reply()
Implement:
SupportBot
SalesBot
'''
from abc import *
class ChatBot(ABC):
    @abstractmethod
    def reply(self):
        pass

class SupperBot(ChatBot):
    def reply(self):
        print("SuperBot is replying")

class SalesBot(ChatBot):
    def reply(self):
        print("Sales bot is replying")

b1 = SalesBot()
b1.reply()
b2 = SupperBot()
b2.reply()