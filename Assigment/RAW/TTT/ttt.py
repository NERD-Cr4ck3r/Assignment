def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def mainttt():
    board = ["1","2","3","4","5","6","7","8","9"]
    current_player = "X"

    print("🎮 Tic-Tac-Toe Game")
    print("Choose positions from 1 to 9:")
    print_board(board)

    for turn in range(9):
        choice = input(f"Player {current_player}, enter position: ")

        if not choice.isdigit() or int(choice) not in range(1,10):
            print("Invalid input, try again.")
            continue

        index = int(choice) - 1

        if board[index] in ["X", "O"]:
            print("Spot already taken!")
            continue

        board[index] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            return

        # switch player
        current_player = "O" if current_player == "X" else "X"

    print("🤝 It's a draw!")
