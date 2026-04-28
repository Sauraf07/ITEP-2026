def f1(a):
    a.append(5)

x = [1,2,3,4]
print(f"Before calling f1 {x}")
f1(x)
print(f"After calling f1 { x}")