from threading import Thread, current_thread, Lock
import time

c = 0
lock = Lock()


def increment():
    global c
    with lock:
        for _ in range(10000):
            c += 1


t1 = Thread(target=increment)
t2 = Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(c)