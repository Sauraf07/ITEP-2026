from threading import Thread
import time
def square(l):
    Result = []
    print("Calculating Time..")
    time.sleep(5)
    for element in l:
        Result.append(element**2)
    print(f"Square :{Result}")

def cube(l):
    Result = []
    print("Calculating Time..")
    time.sleep(5)
    for element in l:
        Result.append(element**3)
    print(f"Cube :{Result}")
    
l = [1,2,3,4,5,6]
t1 = Thread(target=square,args=(l,))
t2 = Thread(target=cube,args=(l,))
t1.start()
t2.start()
