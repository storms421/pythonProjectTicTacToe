# No friend mode
import random


def single_player(ttt_board):
    # Flag false for loop
    is_win = False
    # Increments each round taken (Total 9 rounds max)
    round_counter = 0

    display_table()

    # While TTT board isn't filled or players haven't won, loop
    while not is_win:
        # Get user input and take the first two inputs and store into row and col
        row, col = valid_input(ttt_board, "Player 1, you are 'X'! Enter coordinates to place your piece down "
                                          "(row col): ")
        ttt_board[row][col] = "X"
        display_table()
        round_counter += 1
        if game_win(ttt_board, round_counter, "Player Wins!"):
            break

        # Get Computer's input
        print("Computer's Turn")
        row, col = computer_input(ttt_board)
        ttt_board[row][col] = "O"
        display_table()
        round_counter += 1
        is_win = game_win(ttt_board, round_counter, "Computer Wins!")


# Function used to determine the computer's movement
def computer_input(ttt_board):
    valid_computer = False

    # If possible, make sure player 1 can't control the board
    if ttt_board[1][1] == " ":
        return 1, 1

    # If offense player tries diagonal strategy, cut off path by playing offensively (makes player play defense)
    if ttt_board[1][1] == "O" and ttt_board[0][0] == "X" and ttt_board[2][2] == "X" and ttt_board[1][0] == " ":
        return 1, 0
    if ttt_board[1][1] == "O" and ttt_board[2][0] == "X" and ttt_board[0][2] == "X" and ttt_board[1][2] == " ":
        return 1, 2

    # If offense player goes to middle, cut off one diagonal area by default (Sticks them with one area to work with)
    if ttt_board[1][1] == "X" and ttt_board[0][2] == " ":
        return 0, 2

    # This beats the player's attempt at a strategy to get the upper hand on the computer
    if ttt_board[1][1] == "X" and ttt_board[0][2] == "O" and ttt_board[2][0] == "X" and ttt_board[0][0] == " ":
        return 0, 0

    # Offense Mode
    for i in range(3):
        # Check rows
        if ttt_board[i][0] == "O" and ttt_board[i][1] == "O" and ttt_board[i][2] == " ":
            return i, 2
        if ttt_board[i][0] == "O" and ttt_board[i][1] == " " and ttt_board[i][2] == "O":
            return i, 1
        if ttt_board[i][0] == " " and ttt_board[i][1] == "O" and ttt_board[i][2] == "O":
            return i, 0
        # Check columns
        if ttt_board[0][i] == " " and ttt_board[1][i] == "O" and ttt_board[2][i] == "O":
            return 0, i
        if ttt_board[0][i] == "O" and ttt_board[1][i] == " " and ttt_board[2][i] == "O":
            return 1, i
        if ttt_board[0][i] == "O" and ttt_board[1][i] == "O" and ttt_board[2][i] == " ":
            return 2, i

    # Check diagonal (top down)
    if ttt_board[0][0] == " " and ttt_board[1][1] == "O" and ttt_board[2][2] == "O":
        return 0, 0
    if ttt_board[0][0] == "O" and ttt_board[1][1] == " " and ttt_board[2][2] == "O":
        return 1, 1
    if ttt_board[0][0] == "O" and ttt_board[1][1] == "O" and ttt_board[2][2] == " ":
        return 2, 2

    # Check diagonal (down top)
    if ttt_board[2][0] == " " and ttt_board[1][1] == "O" and ttt_board[0][2] == "O":
        return 2, 0
    if ttt_board[2][0] == "O" and ttt_board[1][1] == " " and ttt_board[0][2] == "O":
        return 1, 1
    if ttt_board[2][0] == "O" and ttt_board[1][1] == "O" and ttt_board[0][2] == " ":
        return 0, 2

    # Defense Mode
    for i in range(3):
        # Check rows
        if ttt_board[i][0] == "X" and ttt_board[i][1] == "X" and ttt_board[i][2] == " ":
            return i, 2
        if ttt_board[i][0] == "X" and ttt_board[i][1] == " " and ttt_board[i][2] == "X":
            return i, 1
        if ttt_board[i][0] == " " and ttt_board[i][1] == "X" and ttt_board[i][2] == "X":
            return i, 0
        # Check columns
        if ttt_board[0][i] == " " and ttt_board[1][i] == "X" and ttt_board[2][i] == "X":
            return 0, i
        if ttt_board[0][i] == "X" and ttt_board[1][i] == " " and ttt_board[2][i] == "X":
            return 1, i
        if ttt_board[0][i] == "X" and ttt_board[1][i] == "X" and ttt_board[2][i] == " ":
            return 2, i

    # Check diagonal (top down)
    if ttt_board[0][0] == " " and ttt_board[1][1] == "X" and ttt_board[2][2] == "X":
        return 0, 0
    if ttt_board[0][0] == "X" and ttt_board[1][1] == " " and ttt_board[2][2] == "X":
        return 1, 1
    if ttt_board[0][0] == "X" and ttt_board[1][1] == "X" and ttt_board[2][2] == " ":
        return 2, 2

    # Check diagonal (down top)
    if ttt_board[2][0] == " " and ttt_board[1][1] == "X" and ttt_board[0][2] == "X":
        return 2, 0
    if ttt_board[2][0] == "X" and ttt_board[1][1] == " " and ttt_board[0][2] == "X":
        return 1, 1
    if ttt_board[2][0] == "X" and ttt_board[1][1] == "X" and ttt_board[0][2] == " ":
        return 0, 2

    while not valid_computer:
        temp_row = random.randint(0, 2)
        temp_col = random.randint(0, 2)
        if ttt_board[temp_row][temp_col] != "X" and ttt_board[temp_row][temp_col] != "O":
            return temp_row, temp_col


# Friend mode
def multiplayer(ttt_board):
    # Flag false for loop
    is_win = False
    round_counter = 0

    display_table()

    # While TTT board isn't filled or players haven't won, loop
    while not is_win:
        # Get user input and take the first two inputs and store into row and col
        row, col = valid_input(ttt_board, "Player 1 you are 'X'! Enter coordinates to place your piece down: ")
        ttt_board[row][col] = "X"
        display_table()
        round_counter += 1
        if game_win(ttt_board, round_counter, "Player 1 Wins"):
            break

        row, col = valid_input(ttt_board, "Player 2 you are 'O'! Enter coordinates to place your piece down: ")
        ttt_board[row][col] = "O"
        display_table()
        round_counter += 1
        is_win = game_win(ttt_board, round_counter, "Player 2 Wins!")


# Makes sure the players put in a valid input
def valid_input(ttt_board, input_string):
    valid = False

    while not valid:
        # Checks if an integer is inputted
        try:
            temp_row, temp_col = map(int, input(input_string).split())

            # Checks if coordinate inputs are in range
            if 0 <= temp_row < 3 and 0 <= temp_col < 3:
                # Checks if coordinate location isn't taken
                if ttt_board[temp_row][temp_col] != "X" and ttt_board[temp_row][temp_col] != "O":
                    return temp_row, temp_col
                else:
                    print("\nYou can't write over that spot silly goose! Try again!\n")
            else:
                print("\nInvalid coordinates. Needs to be in between [0-2]\n")
        except ValueError:
            print("\nInvalid input. That's not an integer >:(\n")


# Determines who wins
def game_win(ttt_board, count, winner_string):
    # If the row or columns match vertically or horizontally, there is a winner
    for i in range(3):
        if ttt_board[0][i] == "X" and ttt_board[1][i] == "X" and ttt_board[2][i] == "X":
            print(f"\n{winner_string}\n")
            return True
        elif ttt_board[i][0] == "X" and ttt_board[i][1] == "X" and ttt_board[i][2] == "X":
            print(f"\n{winner_string}\n")
            return True
        elif ttt_board[0][i] == "O" and ttt_board[1][i] == "O" and ttt_board[2][i] == "O":
            print(f"\n{winner_string}\n")
            return True
        elif ttt_board[i][0] == "O" and ttt_board[i][1] == "O" and ttt_board[i][2] == "O":
            print(f"\n{winner_string}\n")
            return True

    # If the row or columns match diagonally, there is a winner
    if ttt_board[0][0] == "X" and ttt_board[1][1] == "X" and ttt_board[2][2] == "X":
        print(f"\n{winner_string}\n")
        return True
    elif ttt_board[2][0] == "X" and ttt_board[1][1] == "X" and ttt_board[0][2] == "X":
        print(f"\n{winner_string}\n")
        return True
    elif ttt_board[0][0] == "O" and ttt_board[1][1] == "O" and ttt_board[2][2] == "O":
        print(f"\n{winner_string}\n")
        return True
    elif ttt_board[2][0] == "O" and ttt_board[1][1] == "O" and ttt_board[0][2] == "O":
        print(f"\n{winner_string}\n")
        return True

    # If counter exceeds 9 rounds, return Cat's Game
    if count < 9:
        return False
    else:
        print("\nCat's Game\n")
        return True


# Displays the current tic-tac-toe board
def display_table():
    print("    0 1 2")
    for i in range(len(tic_tac_toe_board)):
        print(i, "  ", end="")
        for j in range(len(tic_tac_toe_board[i])):
            print(tic_tac_toe_board[i][j], end="")
            if j < 2:
                print("|", end="")
        print("")


if __name__ == '__main__':
    while True:
        print("Welcome to Tic-Tac-Toe!")

        # 2D TTT board initialized
        tic_tac_toe_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        # Checks if only an integer is inputted
        try:
            menu = input("How will you be playing? \n(1) Single Player \n(2) Multiplayer \n(3) Exit\n")
            menu = int(menu)
            # Checks if input is an option
            if menu == 1:
                # Call function for single player game (One friend mode)
                single_player(tic_tac_toe_board)
            elif menu == 2:
                # Call function for multiplayer game (NO friends mode)
                multiplayer(tic_tac_toe_board)
            elif menu == 3:
                # Rage Quit
                break
            else:
                print("\nOut of range. Enter 1, 2, or 3\n")
        except ValueError:
            print("\nInvalid input. That's not an integer >:(\n")


# Information for me to reference:
# .split() is used to split up strings. It, by default, splits based on whitespace.
#          In this code, the split method is used to split up the string input from
#          the user by whitespace.
# map() is used to apply a specified function to all items in an iterable. In this
#          code, the map function is used to convert each string into an integer
