display_grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
Xs, Os, player1, player2 = ["X", "X", "X"], ["O", "O", "O"], input("Enter name for player 1: "), input(
    "Enter name for player 2: ")


def display():
    for i in range(0, 9, 3):
        print(*display_grid[i:i + 3], sep="    ")


a = True


for i in range(10):
    display()
    if a:
        turn = input(f"Enter number, {player1}: ")
        for item in display_grid:
            if turn == item:
                display_grid[int(turn) - 1] = "X"
                a = False
    else:
        turn = input(f"Enter number, {player2}: ")
        for item in display_grid:
            if turn == item:
                display_grid[int(turn) - 1] = "O"
                a = True
    if display_grid[0:3] == Xs or display_grid[3:6] == Xs or display_grid[7:10] == Xs:
        display()
        print(player1, "has won")
        break
    elif display_grid[0:3] == Os or display_grid[3:6] == Os or display_grid[7:10] == Os:
        display()
        print(player2, "has won")
        break
    elif display_grid[0::3] == Xs or display_grid[1::3] == Xs or display_grid[2::3] == Xs:
        display()
        print(player1, "has won")
        break
    elif display_grid[0::3] == Os or display_grid[1::3] == Os or display_grid[2::3] == Os:
        display()
        print(player2, "has won")
        break
    elif display_grid[0::4] == Xs or display_grid[2:7:2] == Xs:
        display()
        print(player1, "has won")
        break
    elif display_grid[0::4] == Os or display_grid[2:7:2] == Os:
        display()
        print(player2, "has won")
        break
    elif i == 9:
        print("It's a draw!!")
        break
