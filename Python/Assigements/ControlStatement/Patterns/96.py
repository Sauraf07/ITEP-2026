n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65+j) if (j==0 or j==i-1 or i==n) else " ", end="")
    print()