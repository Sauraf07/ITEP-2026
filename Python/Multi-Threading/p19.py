from threading import Thread,current_thread,Lock
import time
class Task:
    def __init__(self):
        self.lock = Lock()

    def m1(self):
        with self.lock:
            print(f"{current_thread().name} EXECUTING..")
            
