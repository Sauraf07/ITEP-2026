n = 5
for i in range(n, 0, -1):
    print("1", end="")
    if i > 1: print("+"*(i-2), end=""); print(i)
    else: print()
