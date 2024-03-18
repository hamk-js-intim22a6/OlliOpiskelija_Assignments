from random import randint

def ask_integer(s):
    """Ask the user for an integer, and keep asking until they give a valid one."""
    while True:
        try:
            return int(input(s))
        except ValueError:
            print("Please enter a valid integer")

n = randint(1, 101)
attempts = 0

while True:
    guess = ask_integer("Enter a number between 1 and 100: ")
    attempts += 1
    if guess < n:
        print("Your guess is low")
    elif guess > n:
        print("Your guess is high")
    else:
        print(f"You guessed it in {attempts} attempts!")
        break
    