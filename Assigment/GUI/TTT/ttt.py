import tkinter as tk

def mainttt():
    win = tk.Toplevel()
    win.title("Tic Tac Toe")
    win.geometry("300x350")

    board = [""] * 9
    current_player = "X"

    title = tk.Label(win, text="Tic Tac Toe", font=("Arial", 16))
    title.pack(pady=10)

    status = tk.Label(win, text="Player X's Turn", font=("Arial", 12))
    status.pack(pady=5)

    frame = tk.Frame(win)
    frame.pack()

    buttons = []

    def check_winner(player):
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
                return True
        return False

    def on_click(index):
        nonlocal current_player

        if board[index] != "":
            return

        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner(current_player):
            status.config(text=f"🎉 Player {current_player} Wins!")
            disable_buttons()
            return

        if "" not in board:
            status.config(text="🤝 It's a Draw!")
            return

        current_player = "O" if current_player == "X" else "X"
        status.config(text=f"Player {current_player}'s Turn")

    def disable_buttons():
        for btn in buttons:
            btn.config(state="disabled")

    def reset_game():
        nonlocal board, current_player
        board = [""] * 9
        current_player = "X"
        status.config(text="Player X's Turn")
        for btn in buttons:
            btn.config(text="", state="normal")

    # create buttons (3x3 grid)
    for i in range(9):
        btn = tk.Button(frame, text="", width=5, height=2,
                        font=("Arial", 18),
                        command=lambda i=i: on_click(i))
        btn.grid(row=i//3, column=i%3, padx=5, pady=5)
        buttons.append(btn)

    reset_btn = tk.Button(win, text="Reset Game", command=reset_game)
    reset_btn.pack(pady=10)