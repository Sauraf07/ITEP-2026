'''
By using Function 
and by extending Thread Class
'''
from threading import Thread
class FirstThread(Thread):
    def run(self):
        print("Run Executed")

t1 = FirstThread()
t2 = FirstThread()
t1.start()
t2.start()