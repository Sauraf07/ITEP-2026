'''
Find Most Frequent Vowel and Consonant
'''
def MostFrequentVowelAndConsonant():
    s = "successes"
    vowels = 'aeiou'
    vowel_freq = {}
    consonant_freq = {}
    
    for char in s:
        if char in vowels:
            vowel_freq[char] = vowel_freq.get(char, 0) + 1
        else:
            consonant_freq[char] = consonant_freq.get(char, 0) + 1
            
    max_vowel_freq = max(vowel_freq.values()) if vowel_freq else 0
    max_consonant_freq = max(consonant_freq.values()) if consonant_freq else 0
    
    result = max_vowel_freq + max_consonant_freq
    print(result)

MostFrequentVowelAndConsonant()