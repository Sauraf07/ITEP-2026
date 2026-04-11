current = 1
for i in range(1, 5):
    print(''.join([str(current + j) for j in range(i)]))
    current += i