a = float(input())  # actual points
p = float(input())  # possible points
if a / p < 0.6:
    print("F")
elif 0.6 <= a / p < 0.7:
    print("D")
elif 0.7 <= a / p < 0.8:
    print("C")
elif 0.8 <= a / p < 0.9:
    print("B")
else:
    print("A")
