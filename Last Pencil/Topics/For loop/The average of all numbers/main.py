a = int(input())
b = int(input())
counter = 0
total = 0
for x in range(a, b + 1):
    if x % 3 == 0:
        total += x
        counter += 1
        mean = total / counter
print(mean)
