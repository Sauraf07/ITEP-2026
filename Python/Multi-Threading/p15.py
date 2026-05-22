from threading import Thread,current_thread,Lock
import time
class Task:
    def __init__(self):
        self.lock = Lock()

    def transection(self):
        with self.lock:
            for _ in range(5):
                print(f"{current_thread().name} Executing  ")
                time.sleep(1)

task = Task()
t1 = Thread(target=task.transection)
t2 = Thread(target=task.transection)

t1.start()
t2.start()