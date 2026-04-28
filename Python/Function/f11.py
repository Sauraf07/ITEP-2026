def f1():
    global x
    x = 100
    print(f"Inside f1 : {x}")

def f2():
    print(f"inside f2 :{x}")

f1()
f2()