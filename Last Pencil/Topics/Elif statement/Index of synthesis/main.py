index = float(input())
if index < 2.0:
    print("Analytic")
elif 2.0 <= index <= 3.0:
    print("Synthetic")
else:
    print("Polysynthetic")
