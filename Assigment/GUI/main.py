import tkinter as tk

from GUESS_GAME.Guess_game import mainguessgame
from RPS.rps import mainrps
from TTT.ttt import mainttt


def mainpro():
    root = tk.Tk()
    root.title("E-Plaza Game Hub")
    root.geometry("420x450")
    root.config(bg="#1e1e2f")  # dark background

    # ---------- Styles ----------
    BTN_BG = "#3a86ff"
    BTN_HOVER = "#265df2"
    BTN_FG = "white"

    # ---------- Hover Effect ----------
    def on_enter(e):
        e.widget['background'] = BTN_HOVER

    def on_leave(e):
        e.widget['background'] = BTN_BG

    # ---------- Title ----------
    title = tk.Label(
        root,
        text="🎮 E-Plaza Game Hub",
        font=("Arial", 18, "bold"),
        bg="#1e1e2f",
        fg="#ffffff"
    )
    title.pack(pady=30)

    # ---------- Subtitle ----------
    sub = tk.Label(
        root,
        text="Choose Your Game",
        font=("Arial", 12),
        bg="#1e1e2f",
        fg="#bbbbbb"
    )
    sub.pack(pady=5)

    # ---------- Button Creator ----------
    def create_button(text, command):
        btn = tk.Button(
            root,
            text=text,
            command=command,
            width=25,
            height=2,
            bg=BTN_BG,
            fg=BTN_FG,
            font=("Arial", 11, "bold"),
            bd=0,
            activebackground=BTN_HOVER,
            cursor="hand2"
        )
        btn.pack(pady=10)

        # bind hover
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        return btn

    # ---------- Functions ----------
    def open_guess():
        mainguessgame()

    def open_rps():
        mainrps()

    def open_ttt():
        mainttt()

    # ---------- Buttons ----------
    create_button("🎯 Number Guess Game", open_guess)
    create_button("✊ Rock Paper Scissors", open_rps)
    create_button("❌⭕ Tic Tac Toe", open_ttt)
    create_button("🚪 Exit", root.quit)

    root.mainloop()


if __name__ == "__main__":
    mainpro()