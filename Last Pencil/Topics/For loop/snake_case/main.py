text = input()
if text.islower():
    print(text)
else:
    if text[0].isupper:
        text = text.replace(text[0], text[0].lower())
    for i in text:
        if i.isupper():
            text = text.replace(i, "_"+i.lower())
    print(text)
