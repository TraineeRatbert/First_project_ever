guest_list = []
while True:
    n = input()
    guest_list.append(n)
    if n == ".":
        guest_list.pop()
        break
print(guest_list)
print(len(guest_list))
