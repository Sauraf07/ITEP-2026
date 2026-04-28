def f1(a,b = []):
    b.append(1)
    print(f"Inside f1 a {a} b {b}")

f1(10)
f1(10)
f1(10)