import random

def mainrps():
    possiblities = ['rock', 'paper', 'scissors']

    def computer_choise():
        return random.choice(possiblities)

    print('Welcome to Rock Paper Scissors Game')
    print("ROCK, PAPER, SCISSORS")
    print("To quit Game enter 'q'")

    total_turns = 5
    user_points = 0
    computer_points = 0

    for _ in range(total_turns):
        user_inp = input("\nYour Chance: ").lower()

        if user_inp == 'q':
            break

        if user_inp not in possiblities:
            print("Invalid input!")
            continue

        comp = computer_choise()
        print(f'Computer choice is {comp}')

        if user_inp == comp:
            print("IT'S A TIE!")
        elif (user_inp == 'rock' and comp == 'scissors') or \
             (user_inp == 'paper' and comp == 'rock') or \
             (user_inp == 'scissors' and comp == 'paper'):
            print("You won!!")
            user_points += 1
        else:
            print("Computer won!!")
            computer_points += 1

    print("\nFinal Score:")
    print(f"Your Points: {user_points}")
    print(f"Computer Points: {computer_points}")
