'''
32. Database Interface
Methods:
connect()
disconnect()
Implement:
MySQL
MongoDB
PostgreSQL
'''
from abc import *
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class MySql(Database):
    def connect(self):
        print("Database connected")
    
    def disconnect(self):
        print("Database Disconnected")

class MangoDB(Database):
    def connect(self):
        print("Database connected")
    
    def disconnect(self):
        print("Database Disconnected")

class PostgreSQL(Database):
    def connect(self):
        print("Database connected")
    
    def disconnect(self):
        print("Database Disconnected")

s = MySql()
s.connect()
m = MangoDB()
m.connect()
p = PostgreSQL()
p.connect()