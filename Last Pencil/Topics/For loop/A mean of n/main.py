n = int(input())
counter = 0
total = 0
for _ in range(1, n + 1):
    x = int(input())
    total += x
    counter += 1
    mean = float(total / counter)
print(mean)
