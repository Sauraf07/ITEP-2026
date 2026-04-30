def JewelsAndStones(jewels,stones):
    jewels_set=set(jewels)
    count=0
    for s in stones:
        if s in jewels_set:
            count+=1
    return count

    
print(JewelsAndStones("aA","aAAbbbb"))