import tkinter as tk
import random

def mainguessgame():
    win = tk.Toplevel()
    win.title("Number Guess Game")
    win.geometry("300x300")

    secret_num = random.randint(1, 99)
    attempts = 5

    label = tk.Label(win, text="Guess a number (1-99)")
    label.pack(pady=10)

    entry = tk.Entry(win)
    entry.pack()

    result = tk.Label(win, text="")
    result.pack(pady=10)

    def check():
        nonlocal attempts

        try:
            guess = int(entry.get())
        except:
            result.config(text="Enter a valid number")
            return

        attempts -= 1

        if guess == secret_num:
            result.config(text="🎉 You Won!")
        elif attempts == 0:
            result.config(text=f"😢 You Lost! Number was {secret_num}")
        elif guess > secret_num:
            result.config(text=f"Try Lower! Attempts left: {attempts}")
        else:
            result.config(text=f"Try Higher! Attempts left: {attempts}")

    btn = tk.Button(win, text="Submit", command=check)
    btn.pack(pady=10)