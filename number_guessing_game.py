import random

def guess_number(guess=None):
    """Number Guessing Game."""
    num = random.randint(1,100)
    guess = None

    while guess != num:
        guess = input("Guess a number: ")
        guess = int(guess)
        if guess == num:
            print("Congratulation you won.")
            break
        elif guess > num:
            print("Your number is High.")
        elif guess < num:
            print("You entered low number.")
guess_number()
