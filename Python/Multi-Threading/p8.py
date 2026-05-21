'''
  T1 ---> 5 time printing GM...
  T2 ---> 5 time printing GN...
'''
from threading import Thread
import time
class FirstThread(Thread):
    def run(self):
        for _ in range(5):
            print("GM.....")
            time.sleep(1)
        
class SecondThread(Thread):
    def run(self):
        for _ in range(5):
            print("GN...")
            time.sleep(0.5)

t1 = FirstThread()
t2 = SecondThread()
t1.run()
t2.run()