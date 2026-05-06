# Akhil Chintanippula 24204-EC-023

# imports
from Num_guess.random_num import mainguessgame
from RPS.rps import mainrps
from TTT.ttt import mainttt


def mainpro():
    name = input("Enter your name: ")
    print(f"\nHey {name}, welcome to e-plaza!\n")

    while True:
        print("""
Choose a game:
1. Number Guess Game
2. Rock Paper Scissors
3. Tic-Tac-Toe
4. Exit
""")

        try:
            game_no = int(input(">> "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if game_no == 1:
            mainguessgame()
        elif game_no == 2:
            mainrps()
        elif game_no == 3:
            mainttt()
        elif game_no == 4:
            print("Thanks for visiting e-plaza!")
            break
        else:
            print("Invalid selection. Try again.\n")


# run program
if __name__ == "__main__":
    mainpro()