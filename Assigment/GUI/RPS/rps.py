import tkinter as tk
import random

def mainrps():
    win = tk.Toplevel()
    win.title("Rock Paper Scissors")
    win.geometry("350x350")

    possiblities = ['rock', 'paper', 'scissors']
    total_turns = 5
    turns_left = total_turns

    user_points = 0
    computer_points = 0

    title = tk.Label(win, text="Rock Paper Scissors", font=("Arial", 14))
    title.pack(pady=10)

    info = tk.Label(win, text=f"Turns left: {turns_left}")
    info.pack()

    result = tk.Label(win, text="", font=("Arial", 12))
    result.pack(pady=10)

    score = tk.Label(win, text="You: 0 | Computer: 0")
    score.pack(pady=10)

    def play(user_choice):
        nonlocal turns_left, user_points, computer_points

        if turns_left == 0:
            result.config(text="Game Over!")
            return

        comp = random.choice(possiblities)
        turns_left -= 1

        if user_choice == comp:
            outcome = "It's a Tie!"
        elif (user_choice == 'rock' and comp == 'scissors') or \
             (user_choice == 'paper' and comp == 'rock') or \
             (user_choice == 'scissors' and comp == 'paper'):
            outcome = "You Won!"
            user_points += 1
        else:
            outcome = "Computer Won!"
            computer_points += 1

        result.config(text=f"You: {user_choice} | Computer: {comp}\n{outcome}")
        score.config(text=f"You: {user_points} | Computer: {computer_points}")
        info.config(text=f"Turns left: {turns_left}")

        if turns_left == 0:
            if user_points > computer_points:
                result.config(text="🎉 Final Winner: YOU!")
            elif user_points < computer_points:
                result.config(text="💻 Final Winner: COMPUTER!")
            else:
                result.config(text="🤝 It's a DRAW!")

    # Buttons
    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=20)

    rock_btn = tk.Button(btn_frame, text="Rock", width=10, command=lambda: play('rock'))
    rock_btn.grid(row=0, column=0, padx=5)

    paper_btn = tk.Button(btn_frame, text="Paper", width=10, command=lambda: play('paper'))
    paper_btn.grid(row=0, column=1, padx=5)

    scissor_btn = tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play('scissors'))
    scissor_btn.grid(row=0, column=2, padx=5)
