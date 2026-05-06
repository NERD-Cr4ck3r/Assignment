import random

def mainguessgame():
    num = []

    def onetohum():
        for i in range(1, 100):
            num.append(i)

    def random_num():
        return random.choice(num)

    onetohum()
    secret_num = random_num()
    Guess_count = 0
    total_count = 5

    def Guess_game():
        nonlocal Guess_count
        print("Welcome to the Number Guess game")
        while total_count > Guess_count:
            try:
                print(f"You have {total_count - Guess_count} left")
                Guess = int(input("Enter number: "))
                Guess_count += 1

                if Guess < 1 or Guess > 99:
                    print("Enter a number between 1 to 99")
                    continue
                elif Guess == secret_num:
                    print("Congratulations! You won!!")
                    break
                elif Guess > secret_num:
                    print("Try Lower number..")
                else:
                    print("Try Higher Number..")

            except ValueError:
                print("Enter an integer Between 1 to 99")
        else:
            print("Oh! You've lost")
            print(f"The secret Number is {secret_num}")

    Guess_game()

