x= 100
def f1():
    global x
    x = x +10
    print(f"Inside f1 {x}")

def f2():
    print(f"Inside f2 : {x}")

f1()
f2()