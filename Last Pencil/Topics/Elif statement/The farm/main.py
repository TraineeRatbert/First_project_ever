a = 23  # Chicken price
b = 678  # Goat price
c = 1296  # Pig price
d = 3848  # Cow price
e = 6769  # Sheep price
capital = int(input())
if capital < a:
    print("None")
elif a <= capital < a * 2:
    print("1 chicken")
elif a * 2 < capital < b:
    print(str(capital // a) + " chickens")
elif b <= capital < c:
    print("1 goat")
elif c <= capital < c * 2:
    print("1 pig")
elif c * 2 <= capital < d:
    print("2 pigs")
elif d <= capital < e:
    print("1 cow")
elif capital >= e:
    print(str(capital // e) + " sheep")
