from threading import Thread,current_thread,Lock
import time
lock = Lock()
def Trasnsection():
    with lock:
        for _ in range(5):
            print(f"{current_thread().name} executing....")
            time.sleep(1)
        print("Lock Realesed...")

t1 = Thread(target=Trasnsection)
t2 = Thread(target=Trasnsection)

t1.name = "thread 1"
t2.name = "thread 2"

t1.start()
t2.start()