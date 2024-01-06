# Friend mode
def multiplayer(ttt_board):

    # Flag false for loop
    is_win = False
    round_counter = 0

    # While TTT board isn't filled or players haven't won, loop
    while not is_win:
        # Get user input and take the first two inputs and store into row and col
        row, col = map(int, input("Player 1 you are 'X'! Enter coordinates to place your piece down: ").split())
        ttt_board[row][col] = "X"
        display_table()
        round_counter += 1
        if game_win(ttt_board, round_counter):
            break

        row, col = map(int, input("Player 2 you are 'O'! Enter coordinates to place your piece down: ").split())
        ttt_board[row][col] = "O"
        display_table()
        round_counter += 1
        is_win = game_win(ttt_board, round_counter)


def game_win(ttt_board, count):
    # If the row or columns match vertically or horizontally, there is a winner
    for i in range(3):
        if ttt_board[0][i] == "X" and ttt_board[1][i] == "X" and ttt_board[2][i] == "X":
            print("\nPlayer 1 Wins!")
            return True
        elif ttt_board[i][0] == "X" and ttt_board[i][1] == "X" and ttt_board[i][2] == "X":
            print("\nPlayer 1 Wins!")
            return True
        elif ttt_board[0][i] == "O" and ttt_board[1][i] == "O" and ttt_board[2][i] == "O":
            print("\nPlayer 2 Wins!")
            return True
        elif ttt_board[i][0] == "O" and ttt_board[i][1] == "O" and ttt_board[i][2] == "O":
            print("\nPlayer 2 Wins!")
            return True

    # If the row or columns match diagonally, there is a winner
    if ttt_board[0][0] == "X" and ttt_board[1][1] == "X" and ttt_board[2][2] == "X":
        print("\nPlayer 1 Wins!")
        return True
    elif ttt_board[2][0] == "X" and ttt_board[1][1] == "X" and ttt_board[0][2] == "X":
        print("\nPlayer 1 Wins!")
        return True
    elif ttt_board[0][0] == "O" and ttt_board[1][1] == "O" and ttt_board[2][2] == "O":
        print("\nPlayer 2 Wins!")
        return True
    elif ttt_board[2][0] == "O" and ttt_board[1][1] == "O" and ttt_board[0][2] == "O":
        print("\nPlayer 2 Wins!")
        return True

    # If counter exceeds 9 slots, return Cat's Game
    if count < 9:
        return False
    else:
        print("\nCat's Game")
        return True


# Displays the current tic-tac-toe board
def display_table():
    print("    0 1 2")
    for i in range(len(tic_tac_toe_board)):
        print(i, "  ",  end="")
        for j in range(len(tic_tac_toe_board[i])):
            print(tic_tac_toe_board[i][j], end="")
            if j < 2:
                print("|", end="")
        print("")


if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")

    # 2D TTT board initialized
    tic_tac_toe_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Call function for multiplayer game (cpu version to come cause you have NO friends)
    multiplayer(tic_tac_toe_board)





# Information for me to reference:
# .split() is used to split up strings. It, by default, splits based on whitespace.
#          In this code, the split method is used to split up the string input from
#          the user by whitespace.
# map() is used to apply a specified function to all items in an iterable. In this
#          code, the map function is used to convert each string into an integer
