'''
  T1 ---> 5 time printing GM...
  T2 ---> 5 time printing GN...
'''
from threading import Thread
import time
class FirstThrad(Thread):
    def run(self):
        for _ in range(5):
            print("GM..")
            time.sleep(1.2)

class SecondThread(Thread):
    def run(self):
        print("GN... ")
        time.sleep(1.5)

t1 = FirstThrad()
t2 = SecondThread()

t1.start()
t2.start()