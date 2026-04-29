'''
Jwel and Stones
'''
def JewelsAndStones():
    jewels = "aA"
    stones = "aAbbbb"
    count = 0
    for i in range(len(stones)):
        if stones[i] in jewels:
            count += 1
    print(count)
JewelsAndStones()

