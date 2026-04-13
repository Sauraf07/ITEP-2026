n = 5
for i in range(n-1, -1, -1):
    for j in range(n):
        print("*" if j==i or j==2*(n-1)-i else " ", end=" ")
    print()
