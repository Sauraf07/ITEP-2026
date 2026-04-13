row = [1]
for i in range(5):
    print(" "*(5-i), " ".join(map(str, row)))
    row = [1]+[row[j]+row[j+1] for j in range(len(row)-1)]+[1]
