from threading import Thread,current_thread
import time
class FirstThread(Thread):
    def run(self):
      for _ in range(5):
        print(f"{current_thread().name} executing")
        time.sleep(3)

class SecondThread(Thread):
   def run(self):
      for _ in range(5):
        print(f"{current_thread().name} executing")
        time.sleep(1.4)


class ThirdThread(Thread):
   def run(self):
      for _ in range(5):
        print(f"{current_thread().name} executing")
        time.sleep(0.7)


t1 = FirstThread()
t2 = SecondThread()
t3 = ThirdThread()

t1.name = "Thread 1"
t2.name = "Thread 2"
t3.name = "Thread 3"

t1.start()
t1.join()
t2.start()
t3.start()

for _ in range(5):
    print(f"{current_thread().name} is executing")
    time.sleep(5)