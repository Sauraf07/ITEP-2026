from threading import Thread,current_thread,Lock
import time
lock = Lock()
def consuming_data():
    with lock:
        print(f"{current_thread().name} got lock")
        print(f"{current_thread().name} consuming data..")
        for _ in range(5):
            print(f"{current_thread().name} consuming data")
            time.sleep(4)
        print(f"{current_thread().name} data consumed  ")

def producing_data():
    with lock:
        print(f"{current_thread().name} got lock")
        print(f"{current_thread().name} producing data..")
        for _ in range(5):
            print(f"{current_thread().name} produced data")
            time.sleep(4)
        print(f"{current_thread().name} data produced  ")

producer = Thread(target=producing_data)
consumer = Thread(target=consuming_data)

producer.name = "Producer "
consumer.name = "Consumer"

producer.start()
producer.join(timeout=5)
consumer.start()
