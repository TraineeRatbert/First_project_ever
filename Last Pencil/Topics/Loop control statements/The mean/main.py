counter = 0
total = 0
while True:
    n = input()
    if n != ".":
        m = int(n)
        total += m
        counter += 1
    else:
        print(total / counter)
        break
