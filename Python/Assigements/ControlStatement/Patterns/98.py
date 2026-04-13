ch = ord('A')
for i in range(1, 6):
    for j in range(2*i - 1):
        print(chr(ch), end=""); ch += 1
    print()