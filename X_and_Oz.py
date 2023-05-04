# Part 1: The Display
def part_1():
    Xs = ["X", "X", "X"]
    Os = ["O", "O", "O"]
    display_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    reverse_display_list = sorted(display_list, reverse=True)
    for i in range(0, len(display_list), 3):
        print(display_list[i:i + 3])

    # the verticals
    if display_list[0::3] or reverse_display_list[0::3] == Xs:
        print("The Xs win it!!")
    elif display_list[0::3] or reverse_display_list[0::3] == Os:
        print("The os win it!!")
    elif display_list[2::3] or reverse_display_list[2::3] == Xs:
        print("The Xs win it!!")
    elif display_list[2::3] or reverse_display_list[2::3] == Os:
        print("The os win it!!")
    elif display_list[1::3] or reverse_display_list[1::3] == Xs:
        print("The Xs win it!!")
    elif display_list[1::3] or reverse_display_list[1::3] == Os:
        print("The os win it!!")

    # the horizontals
    elif display_list[0:3] or reverse_display_list[0:3] == Xs:
        print("The Xs win it!!")
    elif display_list[0:3] or reverse_display_list[0:3] == Os:
        print("The os win it!!")
    elif display_list[3:6] or reverse_display_list[3:6] == Xs:
        print("The Xs win it!!")
    elif display_list[3:6] or reverse_display_list[3:6] == Os:
        print("The os win it!!")
    elif display_list[6:9] or reverse_display_list[6:9] == Xs:
        print("The Xs win it!!")
    elif display_list[6:9] or reverse_display_list[6:9] == Os:
        print("The os win it!!")

    # the diagonals
    elif display_list[2:7:2] or reverse_display_list[2:7:2] == Xs:
        print("The Xs win it!!")
    elif display_list[2:7:2] or reverse_display_list[2:7:2] == Os:
        print("The os win it!!")
    elif display_list[0::4] or reverse_display_list[0::4] == Xs:
        print("The Xs win it!!")
    elif display_list[0::4] or reverse_display_list[0::4] == Os:
        print("The os win it!!")
    else:
        print("It's a draw!!")


