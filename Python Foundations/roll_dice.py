import random

roll = random.randint(1,6)
print("The computer rolled a " + str(roll))

guess = int(input('Guess the dice roll...\n'))

if guess == roll:
    print("Correct, The computer rolled a " + str(roll))
else:
    print("You guessed wrong, they rolled a " + str(roll))