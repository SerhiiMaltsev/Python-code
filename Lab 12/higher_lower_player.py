#Serhii Maltsev sm5zj

#following code is used to make initial input
print("Think of a number between 1 and 100 and I'll guess it.")
number_of_guesses = int(input("How many guesses do I get? "))

#following code is used to define all variables that we will use in this program
guess = 50
i = 0
win = False
top_bond = 100
low_bond = 1

#following code is doing once cycle of code to get the initial values for variables
our_answer = input("Is the number higher, lower, or the same as " + str(guess) + "? ")
if our_answer == "higher":
    low_bond = low_bond + guess
if our_answer == "lower":
    top_bond = top_bond - guess -1
if our_answer == "same":
    print("I won!")
    win = True

guess = (top_bond + low_bond) // 2

old = guess
#following code is a loop that is used to simmulate the game
while (i < number_of_guesses-1) and (win != True) and (our_answer != "error"):
    our_answer = input("Is the number higher, lower, or the same as " + str(guess) + "? ")
    if (abs(old - guess)) == 1 and our_answer == "higher":
        print("Wait; how can it be both higher than " + str(guess) + " and lower than " + str(old) + "?")
        our_answer = "error"
    if (abs(old - guess)) == 1 and our_answer == "lower":
        print("Wait; how can it be both higher than " + str(old) + " and lower than " + str(guess) + "?")
        our_answer = ("error")
    if our_answer == "higher":
        low_bond = guess + 1
    if our_answer == "lower":
        top_bond = guess - 1
    if our_answer == "same":
        print("I won!")
        win = True
    i += 1
    old = guess
    guess = (top_bond+low_bond)//2

#following code is used to make output of our program
if win == False and (our_answer != "error"):
    answer = int(input("I lost; what was the answer? "))
    if (answer < low_bond):
            print("That can't be; you said it was " + our_answer + " than " + str(low_bond-1) + "!")
    if (answer > top_bond):
            print("That can't be; you said it was " + our_answer + " than " + str(low_bond+1) + "!")
    else:
        print("Well played!")
