c = int(input())  # column left to right
r = int(input())  # row bottom to top
c_left = 1
c_right = 8
r_bottom = 1
r_top = 8
max_moves = 8
if c in (c_left, c_right):  # leftmost and rightmost column
    x = -3
    if r in (r_top, r_bottom):  # corner
        y = -2
        possible_moves = (max_moves + x + y)
        print(possible_moves)
    else:
        y = 0
        possible_moves = (max_moves + x + y)
        print(possible_moves)
elif c_left < c < c_right:
    x = 0
    if r in (r_top, r_bottom):
        y = -3
        possible_moves = (max_moves + x + y)
        print(possible_moves)
    else:
        y = 0
        possible_moves = (max_moves + x + y)
        print(possible_moves)
else:
    x = 0
    y = 0
    possible_moves = (max_moves + x + y)
    print(possible_moves)
