# 58. Length of Last Word
def LengthOfLast():
    s = "hello bihar "
    length = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            if length > 0:
                break
        else:
            length += 1
    print(length)
LengthOfLast()






