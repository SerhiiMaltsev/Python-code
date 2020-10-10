#Serhii Maltsev sm5zj
import random

#Following block of code makes the input of the number to guess
numberToGuess = int(input("What should the answer be? "))
if numberToGuess == -1:
    numberToGuess = random.randint(1, 101)

numberOfGuesses = int(input("How many guesses? "))

#Following block of code makes the input for
while (numberOfGuesses < 1) and (numberOfGuesses != -1):
    print("Number of guesses should be positive int or should equals to -1. Try again.")
    numberOfGuesses = int(input("How many guesses? "))
if numberOfGuesses == -1:
    numberOfGuesses = random.randint(1, 101)

i = 0
usersGuess = 0
win = False

#Following function performs the process of guess game
def game():
    """
    Simulates the game by asking user the number and compares it to the guessed number
    Input arguments: integer number that is used to guess the answer
    """
    global win, i, usersGuess, numberToGuess, numberOfGuesses
    while (i < numberOfGuesses) and (usersGuess != numberToGuess):
        i += 1
        usersGuess = int(input("Guess a number: "))
        if (usersGuess > numberToGuess) and (i < numberOfGuesses):
            print("The number is lower than that.")
        elif (usersGuess < numberToGuess) and (i < numberOfGuesses):
            print("The number is higher than that.")
        elif (usersGuess == numberToGuess) and (i < numberOfGuesses):
            print("You win!")
            win = True

game()
if (numberOfGuesses == 1) and(usersGuess == numberToGuess):
    print("You win!")
elif win == False:
    print("You lose; the number was " + str(numberToGuess) + ".")
