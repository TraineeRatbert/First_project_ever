from random import randint

cut_nr = 0


def bot_turn():
    global pencil_nr
    global cut_nr
    if pencil_nr == 1:
        cut_nr = 1
    elif pencil_nr % 4 == 0 and pencil_nr != 0:
        cut_nr = 3
    elif pencil_nr % 4 == 3 and pencil_nr != 0:
        cut_nr = 2
    elif pencil_nr % 4 == 2 and pencil_nr != 0:
        cut_nr = 1
    elif pencil_nr != 0:
        cut_nr = randint(1, 3)
    pencil_nr -= cut_nr
    print(cut_nr)
    return pencil_nr, cut_nr


def human_turn():
    global pencil_nr
    global cut_nr
    while True:
        cut_nr = input()
        if not cut_nr.isnumeric():
            print("Possible values: '1', '2' or '3'")
            continue
        cut_nr = int(cut_nr)
        if not 1 <= cut_nr <= 3:
            print("Possible values: '1', '2' or '3'")
            continue
        if cut_nr > pencil_nr:
            print("Too many pencils were taken")
            continue
        else:
            break
    pencil_nr -= cut_nr
    return pencil_nr, cut_nr


print("How many pencils would you like to use:")
while True:
    pencil_nr = input()
    if not pencil_nr.isnumeric():
        print("The number of pencils should be numeric")
        continue
    if int(pencil_nr) == 0:
        print("The number of pencils should be positive")
        continue
    if int(pencil_nr) == 0:
        print("The number of pencils should be numeric")
        continue
    pencil_nr = int(pencil_nr)
    break

print("Who will be the first (John, Jack):")
while True:
    player_one = input()
    if not str(player_one) in ["John", "Jack"]:
        print("Choose between John and Jack")
        continue
    if player_one == "John":
        player_two = "Jack"
    else:
        player_two = "John"
    break
cur_player = player_one
while pencil_nr > 0:
    print('|' * pencil_nr)
    if cur_player == "John":
        print("John's turn:")
        human_turn()
        cur_player = "Jack"
    elif cur_player == "Jack":
        print("Jack's turn:")
        bot_turn()
        cur_player = "John"
while pencil_nr == 0:
    if cur_player == "John":
        print("John won!")
        break
    else:
        print("Jack won!")
        break
