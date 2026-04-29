def palindrome():
    word = input("Enter word : ")
    rev = ""
    for ch in word:
        rev = ch + rev
    if word == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

# palindrome()


