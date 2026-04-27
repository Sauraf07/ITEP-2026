text = 'aabbcde'
freq = {}
for ch in text:
    if ch not in freq:
        freq[ch]=0
    freq[ch] += 1
for ch in text:
    if freq[ch] == 1:
        print(ch)
        break