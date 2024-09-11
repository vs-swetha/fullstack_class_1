def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print()

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Move must be between 1 and 9.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print_board(board)
    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        move = get_move()
        row, col = divmod(move, 3)

        if board[row][col] != ' ':
            print("Cell already taken. Try again.")
            continue

        board[row][col] = player
        print_board(board)

        if check_win(board, player):
            print(f"Player {player} wins!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        turn += 1

if __name__ == "__main__":
    play_game()
