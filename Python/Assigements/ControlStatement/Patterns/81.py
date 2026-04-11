for i in range(1, 6):
    if i == 5:
        print(str(i) * i)
    else:
        print(f"{i} " + " " * (i - 1) + f"{i}")