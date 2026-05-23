from threading import Thread,current_thread,Lock
import time
lock = Lock()
class Task(Thread):
    def __init__(self):
        self.lock = Lock()

    def consuming_data(self):
        with lock:
            print(f"{current_thread().name} got lock")
            print(f"{current_thread().name} consuming data..")
            for _ in range(5):
                print(f"{current_thread().name} consuming data")
                time.sleep(4)
            print(f"{current_thread().name} data consumed  ") 

    def producing_data(self):
        with lock:
            print(f"{current_thread().name} got lock")
            print(f"{current_thread().name} producing data..")
            for _ in range(5):
                print(f"{current_thread().name} producing data")
                time.sleep(4)
            print(f"{current_thread().name} data produced  ")

task = Task()


t1 = Thread(target=task.consuming_data)
t2 = Thread(target=task.producing_data)

t1.name = "Consumer"
t2.name = "Producer"

t2.start()
t1.start()

