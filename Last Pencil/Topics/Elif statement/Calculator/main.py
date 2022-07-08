num_1 = float(input())
num_2 = float(input())
operand = input()
if num_2 == 0 and operand in ("/", "mod", "div"):
    print("Division by 0!")
elif operand == "+":
    print(num_1 + num_2)
elif operand == "-":
    print(num_1 - num_2)
elif operand == "/":
    print(num_1 / num_2)
elif operand == "*":
    print(num_1 * num_2)
elif operand == "mod":
    print(num_1 % num_2)
elif operand == "pow":
    print(num_1 ** num_2)
elif operand == "div":
    print(num_1 // num_2)
