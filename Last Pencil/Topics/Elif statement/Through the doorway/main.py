a = float(input())
b = float(input())
c = float(input())
x = float(input())
y = float(input())
door = x * y
box_1 = a * b
box_2 = b * c
box_3 = a * c
if door >= box_1 or door >= box_2 or door >= box_3:
    print("The box can be carried")
else:
    print("The box cannot be carried")
