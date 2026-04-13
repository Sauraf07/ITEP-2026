n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(i if (j==0 or j==i-1 or i==1) else " ", end="")
    print()