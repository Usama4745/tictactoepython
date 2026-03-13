def initialize_game():#initializes the board and game state
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    current_player = "X"
    game_over = False
    winner = None
    return board, current_player, game_over, winner


def display_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(f"  {row[0]} | {row[1]} | {row[2]}")
        if i < 2:
            print(" ---+---+---")
    print("\n")


def make_move(board, row, col, current_player):
    if board[row][col] == " ":
        board[row][col] = current_player
        return True 
    return False 

def make_AI_move(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                return True 
    return False 

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    #check diagonals for wins
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None  


def check_draw(board):
    for row in board:
        if " " in row:
            return False 
    return True 


def switch_player(current_player):
    return "O" if current_player == "X" else "X"


def play_game():
    board, current_player, game_over, winner = initialize_game()
    print("=== TIC TAC TOE ===")
    display_board(board)

    while not game_over:
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("  Enter row (0-2): "))
            col = int(input("  Enter col (0-2): "))
        except ValueError:
            print("Invalid input! Enter a number 0-2.\n")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Out of range! Use 0, 1, or 2.\n")
            continue

        # Make move
        if not make_move(board, row, col, current_player):
            print("Cell already taken! Try again.\n")
            continue

        display_board(board)

        # Check winner
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            game_over = True

        # Check draw
        elif check_draw(board):
            print("It's a draw!")
            game_over = True

        else:
            if current_player == "X":
                current_player = switch_player(current_player)
                make_AI_move(board)
                display_board(board)
                winner = check_winner(board)
                if winner:
                    print(f"Player {winner} wins!")
                    game_over = True
                current_player = switch_player(current_player)



# Run the game
play_game()