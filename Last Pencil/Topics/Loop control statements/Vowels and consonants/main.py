vowels = ["a", "e", "i", "o", "u"]
word = input()
my_list = list(word)
for letter in my_list:
    if letter.isalpha():
        if letter in vowels:
            print("vowel")
        else:
            print("consonant")
    else:
        break
