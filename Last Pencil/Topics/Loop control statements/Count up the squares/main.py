start_num = int(input())
total = 0 + start_num
target_total = 0 + (start_num * start_num)
while start_num != 0:
    n = int(input())
    total += n
    target_total += (n * n)
    if total == 0:
        print(target_total)
        break
else:
    print(0)
