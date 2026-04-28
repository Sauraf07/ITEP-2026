def f1(a):
    print(f"Inside f1 :{a}")
    a = a + "world"
    print(f"After concvt : {a}")

x = "Hello"
f1(x)
print(f"After calling f1 : {x}")