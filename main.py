def multiplayer():

    game_win = False

    while(game_win == False):
        game_win = True

#Test this comment


def display_table():
    for i in range(len(tic_tac_toe_board)):
        for j in range(len(tic_tac_toe_board[i])):
            print(tic_tac_toe_board[i][j], end="")
            if j < 2:
                print("|", end="")
        print("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")

    tic_tac_toe_board = [["  ", " X ", " O "], [" O ", "  ", "  "], [" X ", "  ", " X "]]

    display_table()
   # player1_input = input("Player 1! Enter coordinates to place your piece down: ")

   # multiplayer()


