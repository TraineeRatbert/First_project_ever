list_names = []
numbers = []
while True:
    cafe = input()
    if cafe == "MEOW":
        x = max(numbers)
        y = numbers.index((max(numbers)))
        print(list_names[y])
        break
    else:
        cafe = cafe.split()
        name = cafe[0]
        quantity = cafe[1]
        list_names.append(name)
        numbers.append(quantity)
        numbers = [int(i) for i in numbers]
