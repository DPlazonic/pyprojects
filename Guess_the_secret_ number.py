import random

secret_number = random.randint(0,6)
guessed = False
while guessed == False:
    guess_number = int(input("Guess the number (0-6):"))

    if secret_number == guess_number:
        print("Correct! Congratulations! ")
        guessed = True
    elif guess_number > (secret_number):
        print("Lower, try again")
        guessed = False
    elif guess_number < (secret_number):
        print("Higher, try again")
        guessed = False


