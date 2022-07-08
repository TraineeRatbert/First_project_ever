my_list = []
while True:
    n = input()
    if n == ".":
        break
    else:
        m = float(n)
        my_list.append(m)
print(min(my_list))
