from threading import Thread, current_thread


class FirstThread(Thread):
    def run(self):
        for _ in range(5):
            print(f"HEllo {current_thread().name}")


t1 = FirstThread()
t2 = FirstThread()

t1.name = "Thread 1"
t2.name = "Thread 2"

t1.start()
t2.start()
