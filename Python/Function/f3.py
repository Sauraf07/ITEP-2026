def f1(a):
    print(f"Before conct : a {id(a)}")
    a = a + (5,6)
    print(f"Inside f1: {a} adderss of a {id(a)}")

x = (1,2,3)
print(f"Adderss of c {id(x)}")
print(f"Before calling f1 : {x}")
f1(x)
print(f"After calling f1 {x}")