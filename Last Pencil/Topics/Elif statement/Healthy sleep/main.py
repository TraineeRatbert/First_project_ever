a = int(input())
b = int(input())
h = int(input())
if h < a:
    print("Deficiency")
elif a <= h <= b:
    print("Normal")
else:
    print("Excess")
