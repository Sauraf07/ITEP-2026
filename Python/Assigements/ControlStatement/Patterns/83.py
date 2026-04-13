ch = ord('a')
for i in range(1, 6):
    row = [chr(ch+j) for j in range(i)]; ch += i
    for j, c in enumerate(row):
        print(c if (j==0 or j==len(row)-1 or i==5) else " ", end="")