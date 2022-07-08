string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
b = 0
for i in string:
    if i in vowels:
        b += 1
print(b)
