current_char = 97
for i in range(1, 6):
    print("".join([chr(current_char + j) if j % 2 == 0 else " " for j in range(i)]))
    current_char += i