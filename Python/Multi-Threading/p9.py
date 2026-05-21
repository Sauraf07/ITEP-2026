from threading import Thread,current_thread
import time
def sayhello():
    for _ in range(5):
        print(f"Hello...{current_thread().name}")
        time.sleep(1)

t1 =Thread(target=sayhello)
t2 = Thread(target=sayhello)

t1.name = "Thread 1"
t2.name = "Thread 2"
t1.start()
t2.start()