board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
is_player_1 = True
game_over = False


def print_board():
    print(
        "   1   2   3 \n"
        f"1  {board[0][0]} | {board[0][1]} | {board[0][2]} \n"
        "  -----------\n"
        f"2  {board[1][0]} | {board[1][1]} | {board[1][2]} \n"
        "  -----------\n"
        f"3  {board[2][0]} | {board[2][1]} | {board[2][2]} \n"
    )



def add_mark():
    global is_player_1

    if is_player_1:
        mark = "O"
        player_num = 1
        player_mark = "⭕"
    else:
        mark = "X"
        player_num = 2
        player_mark = "❌"

    print \
        ("To make a move, enter the (row number,column number) of the cell you would like to mark, e.g. 1,1 for top left.")
    choice = input(f"{player_mark}Player {player_num}'s choice: ")
    row = int(choice.split(",")[0])
    col = int(choice.split(",")[1])

    if board[row - 1][col - 1] == " ":
        board[row - 1][col - 1] = mark
        print_board()
        is_player_1 = not is_player_1
    else:
        print("Cell is taken. Please try again.")
        add_mark()


def board_has_space():
    for row in board:
        for cell in row:
            if cell == " ":
                return True
    return False


def check_win():
    for player in range(1,3):
        if \
                (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != " ") \
                or (board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != " ") \
                or (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != " ") \
                or (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != " ") \
                or (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != " ") \
                or (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != " ") \
                or (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != " ") \
                or (board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != " ") :
            print(f"Player {player} wins! Congratulations!\n\n")
            return True

        if not board_has_space():
            print(f"It's a Draw!\n\n")
            return True
    return False

print("Welcome to Tic Tac Toe!")

print(
    "████████╗██╗░█████╗░        ████████╗░█████╗░░█████╗░        ████████╗░█████╗░███████╗\n"
    "╚══██╔══╝██║██╔══██╗        ╚══██╔══╝██╔══██╗██╔══██╗        ╚══██╔══╝██╔══██╗██╔════╝\n"
    "░░░██║░░░██║██║░░╚═╝        ░░░██║░░░███████║██║░░╚═╝        ░░░██║░░░██║░░██║█████╗░░\n"
    "░░░██║░░░██║██║░░██╗        ░░░██║░░░██╔══██║██║░░██╗        ░░░██║░░░██║░░██║██╔══╝░░\n"
    "░░░██║░░░██║╚█████╔╝        ░░░██║░░░██║░░██║╚█████╔╝        ░░░██║░░░╚█████╔╝███████╗\n"
    "░░░╚═╝░░░╚═╝░╚════╝░        ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░        ░░░╚═╝░░░░╚════╝░╚══════╝\n")

print_board()


while not game_over:
    add_mark()
    game_over = check_win()