'''
  T1 ---> 5 time printing GM...
  T2 ---> 5 time printing GN...
'''
from threading import Thread
class FirstThread(Thread):
    def run(self):
        for _ in range(5):
            print("GM...")

class SecondThread(Thread):
    def run(self):
        for _ in  range(5):
            print("Hi...")

t1 = FirstThread()
t2 = SecondThread()

t1.start()
t2.start()