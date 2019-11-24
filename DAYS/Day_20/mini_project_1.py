player_1 = {
    "name": "Player 1",
    "colored_mark": "\x1b[1;33;40m" + "X" + "\x1b[0m",
    "mark": "X"
}
player_2 = {
    "name": "Player 2",
    "colored_mark": "\x1b[1;34;40m" + "O" + "\x1b[0m",
    "mark": "O"
}


def initialize():
    global a, b, c, d, e, f, g, h, i, player, turn, winner
    a = "0"
    b = "1"
    c = "2"
    d = "3"
    e = "4"
    f = "5"
    g = "6"
    h = "7"
    i = "8"
    player = player_1
    turn = 1
    winner = False


def print_board():
    board = f'''
     |     |
  {a}  |  {b}  |  {c}
-----|-----|-----
  {d}  |  {e}  |  {f}
-----|-----|-----
  {g}  |  {h}  |  {i}
     |     |
'''
    print(board)


def player_turn():
    global turn
    global player
    if turn % 2 == 0:
        player = player_2
        turn += 1
    else:
        player = player_1
        turn += 1


def choice():
    right_choice = False
    global player, a, b, c, d, e, f, g, h, i
    while right_choice == False:
        choice = int(input(f"{player['name']}: "))
        if choice == 0:
            if a == player_1["colored_mark"] or a == player_2["colored_mark"]:
                print("This cell is taken, dude. Choose again.")
            else:
                a = player["colored_mark"]
                right_choice = True
        elif choice == 1:
            if b == "X" or b == "O":
                print("This cell is taken, dude. Choose again.")
            else:
                b = player["colored_mark"]
                right_choice = True
        elif choice == 2:
            if c == "X" or c == "O":
                print("This cell is taken, dude. Choose again.")
            else:
                c = player["colored_mark"]
                right_choice = True
        elif choice == 3:
            if d == "X" or d == "O":
                print("This cell is taken, dude. Choose again.")
            else:
                d = player["colored_mark"]
                right_choice = True
        elif choice == 4:
            if e == "X" or e == "O":
                print("This cell is taken, dude. Choose again.")
            else:
                e = player["colored_mark"]
                right_choice = True
        elif choice == 5:
            if f == "X" or f == "O":
                print("This cell is taken, dude. Choose again.")
            else:
                f = player["colored_mark"]
                right_choice = True
        elif choice == 6:
            if g == "X" or g == "O":
                print("This cell is taken, dude. Choose again.")
            else:
                g = player["colored_mark"]
                right_choice = True
        elif choice == 7:
            if h == "X" or h == "O":
                print("This cell is taken, dude. Choose again.")
            else:
                h = player["colored_mark"]
                right_choice = True
        elif choice == 8:
            if i == "X" or i == "O":
                print("This cell is taken, dude. Choose again.")
            else:
                i = player["colored_mark"]
                right_choice = True


def check_win():
    global winner, a, b, c, d, e, f, g, h, i
    if a == b == c:
        a = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        b = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        c = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        print_board()
        print(f"{player['name']} wins!")
        winner = True
    elif d == e == f:
        d = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        e = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        f = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        print_board()
        print(f"{player['name']} wins!")
        winner = True
    elif g == h == i:
        g = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        h = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        i = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        print_board()
        print(f"{player['name']} wins!")
        winner = True
    elif a == d == g:
        a = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        d = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        g = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        print_board()
        print(f"{player['name']} wins!")
        winner = True
    elif b == e == h:
        b = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        e = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        h = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        print_board()
        print(f"{player['name']} wins!")
        winner = True
    elif c == f == i:
        c = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        f = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        i = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        print_board()
        print(f"{player['name']} wins!")
        winner = True
    elif a == e == i:
        a = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        e = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        i = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        print_board()
        print(f"{player['name']} wins!")
        winner = True
    elif c == e == g:
        c = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        e = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        g = "\x1b[6;30;42m" + player["mark"] + "\x1b[0m"
        print_board()
        print(f"{player['name']} wins!")
        winner = True


def play():
    initialize()
    print_board()
    for i in range(9):
        player_turn()
        choice()
        print_board()
        check_win()
        if winner == True:
            break
    else:
        print("It's a tie.")
    if input("Play again? Y/N: ").capitalize() == "Y":
        play()


play()
