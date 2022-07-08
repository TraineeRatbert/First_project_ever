scores = input().split()
correct = 0
wrong = 0
for i in scores:
    if i == 'C':
        correct += 1
    elif i == 'I':
        wrong += 1
        if wrong >= 3:
            print("Game over")
            print(correct)
            break
else:
    print("You won")
    print(correct)
