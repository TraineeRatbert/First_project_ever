ceiling = "---------"
sidebar = "|"
top_bar = " _ _ _ "  # playing places have indices 1, 3, 5
mid_bar = " _ _ _ "  # playing places have indices 1, 3, 5
low_bar = " _ _ _ "  # playing places have indices 1, 3, 5
result = 0  # no result at game start yet
x_win_counter = 0  # checking for one of 8 possible x win combinations
o_win_counter = 0  # checking for one of 8 possible o win combinations
game_impossible = 0  # impossible game flag, if 1 game is impossible give "Impossible" result
unfinished = 0  # unfinished game flag - neither side won empty places in grid
messages = ["You should enter numbers!", "Coordinates should be from 1 to 3!", "This cell is occupied! Choose another one!"]
game_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # empty grid at start
move_counter = 1  # counter of moves to determine which sign to place on board


def print_results():
    global alef
    global bet
    global gimel
    alef = list(top_bar)
    bet = list(mid_bar)
    gimel = list(low_bar)
    alef[1] = game_list[0]
    alef[3] = game_list[1]
    alef[5] = game_list[2]
    bet[1] = game_list[3]
    bet[3] = game_list[4]
    bet[5] = game_list[5]
    gimel[1] = game_list[6]
    gimel[3] = game_list[7]
    gimel[5] = game_list[8]
    print(ceiling)
    print(sidebar + "".join(alef) + sidebar)
    print(sidebar + "".join(bet) + sidebar)
    print(sidebar + "".join(gimel) + sidebar)
    print(ceiling)
    if result != 0:
        print(result)


def get_new_coords():
    global row
    global column
    while True:
        coords = input("Enter coordinates ").split()
        if len(coords) < 2:
            print(messages[0])
            continue
        elif coords[0].isdigit() is False or coords[1].isdigit() is False:
            print(messages[0])
            continue
        else:
            row = int(coords[0])
            column = int(coords[1])
            if row not in range(1, 4) or column not in range(1, 4):
                print(messages[1])
                continue
            else:
                check_occupancy()
                break


def check_occupancy():
    if row == 1:
        if column == 1 and alef[1] != " ":
            print(messages[2])
            get_new_coords()
        elif column == 2 and alef[3] != " ":
            print(messages[2])
            get_new_coords()
        elif column == 3 and alef[5] != " ":
            print(messages[2])
            get_new_coords()
        else:
            replace()
    elif row == 2:
        if column == 1 and bet[1] != " ":
            print(messages[2])
            get_new_coords()
        elif column == 2 and bet[3] != " ":
            print(messages[2])
            get_new_coords()
        elif column == 3 and bet[5] != " ":
            print(messages[2])
            get_new_coords()
        else:
            replace()
    elif row == 3:
        if column == 1 and gimel[1] != " ":
            print(messages[2])
            get_new_coords()
        elif column == 2 and gimel[3] != " ":
            print(messages[2])
            get_new_coords()
        elif column == 3 and gimel[5] != " ":
            print(messages[2])
            get_new_coords()
        else:
            replace()


def replace():
    global game_list
    global move_counter
    if move_counter == 1 or move_counter % 2 != 0:
        game_sign = "X"
    else:
        game_sign = "O"
    move_counter += 1
    if row == 1:
        if column == 1:
            game_list[0] = game_sign
        elif column == 2:
            game_list[1] = game_sign
        else:
            game_list[2] = game_sign
    elif row == 2:
        if column == 1:
            game_list[3] = game_sign
        elif column == 2:
            game_list[4] = game_sign
        else:
            game_list[5] = game_sign
    elif row == 3:
        if column == 1:
            game_list[6] = game_sign
        elif column == 2:
            game_list[7] = game_sign
        else:
            game_list[8] = game_sign


def check_x_wins():
    global x_win_counter
    if game_list[0] == "X" and game_list[1] == "X" and game_list[2] == "X":
        x_win_counter += 1
    if game_list[3] == "X" and game_list[4] == "X" and game_list[5] == "X":
        x_win_counter += 1
    if game_list[6] == "X" and game_list[7] == "X" and game_list[8] == "X":
        x_win_counter += 1
    if game_list[0] == "X" and game_list[3] == "X" and game_list[6] == "X":
        x_win_counter += 1
    if game_list[1] == "X" and game_list[4] == "X" and game_list[7] == "X":
        x_win_counter += 1
    if game_list[2] == "X" and game_list[5] == "X" and game_list[8] == "X":
        x_win_counter += 1
    if game_list[0] == "X" and game_list[4] == "X" and game_list[8] == "X":
        x_win_counter += 1
    if game_list[2] == "X" and game_list[4] == "X" and game_list[6] == "X":
        x_win_counter += 1


def check_o_wins():
    global o_win_counter
    if game_list[0] == "O" and game_list[1] == "O" and game_list[2] == "O":
        o_win_counter += 1
    if game_list[3] == "O" and game_list[4] == "O" and game_list[5] == "O":
        o_win_counter += 1
    if game_list[6] == "O" and game_list[7] == "O" and game_list[8] == "O":
        o_win_counter += 1
    if game_list[0] == "O" and game_list[3] == "O" and game_list[6] == "O":
        o_win_counter += 1
    if game_list[1] == "O" and game_list[4] == "O" and game_list[7] == "O":
        o_win_counter += 1
    if game_list[2] == "O" and game_list[5] == "O" and game_list[8] == "O":
        o_win_counter += 1
    if game_list[0] == "O" and game_list[4] == "O" and game_list[8] == "O":
        o_win_counter += 1
    if game_list[2] == "O" and game_list[4] == "O" and game_list[6] == "O":
        o_win_counter += 1


def check_draw():
    global result
    while True:
        if x_win_counter == 0 and o_win_counter == 0 and game_list.count(" ") == 0:
            result = "Draw"
            break
        else:
            break


def find_winner():
    global result
    if x_win_counter == 1:
        result = "X wins"
    elif o_win_counter == 1:
        result = "O wins"
    else:
        result = 0


print_results()
while result == 0:
    get_new_coords()
    check_x_wins()
    check_o_wins()
    check_draw()
    if result != "Draw":
        find_winner()
        print_results()
    else:
        print_results()
