n = 5
for i in range(n):
    for j in range(n):
        print(chr(65+j) if (i==0 or i==n-1 or j==0 or j==n-1) else "_", end="")
    print()