import random

print("=== NUMBER GUESSING GAME ===")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it!")

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1
    except:
        print("Enter a valid number.")
        continue

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"\nCorrect! The number was {number}.")
        print(f"You got it in {attempts} tries.")
        break
