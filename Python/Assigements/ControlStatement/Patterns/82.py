for i in range(1, 6):
    print("".join([chr(65 + j) if (i == 1 or j == i - 1) else " " for j in range(i)]))