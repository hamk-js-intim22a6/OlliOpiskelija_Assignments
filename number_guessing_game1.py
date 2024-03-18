from random import randint

n = randint(1, 101)
attempts = 0

while True:
    try:
        guess = int(input("Enter an integer from 1 to 100: "))
    except ValueError:
        print("Please enter an integer between 1 and 100")
        continue
    attempts += 1
    if guess < n:
        print("Your guess is low")
    elif guess > n:
        print("Your guess is high")
    else:
        print(f"You guessed it in {attempts} attempts!")
        break
    