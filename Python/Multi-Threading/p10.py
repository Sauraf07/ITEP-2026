from threading import Thread,current_thread
import time
def sayHello(message):
    for _ in range(5):
        print(f"{message}..{current_thread().name}")
        time.sleep(1)

t1 = Thread(target=sayHello,args=("Hello",))
t2 = Thread(target=sayHello,args=("Hi",))

t1.name = "Thread 1"
t2.name = "Thread 2"
t1.start()
t2.start()