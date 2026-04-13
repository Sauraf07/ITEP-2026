vowel = input("Enter a character : ")
match vowel:
    case 'a'|'e'|'i'|'o'|'u':
        print("Vowel")
    case _:print("Consonant ")