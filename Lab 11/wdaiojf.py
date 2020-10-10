for i in range(0, 3):
    if i != 0:
        print()
    for j in range(0, 6):
        print("0", end="")

print()
print()
for i in range (0, 6):
    if i != 0:
        print()
    for j in range (0, i+1):
        print("0", end="")

print()
print()

for i in range(0, 6):
    print("0"*(i+1))


# Craig Dill (cd9au)
"""
What is the probability of rolling a die five times and each
roll is a six?
"""
from random import randint
def five_die_rolls(p_chances):
    """
    Calculates the probability of rolling five sixes with a die.
    :param p_chances: number of chances to roll five sixes
    :return: string probability message
    """
    print("The chance of rolling five sixes in a row are " + str(1/6**5))
    success = 0
    for chance in range(0, chances):
        count = 0
        x = 0
        # =  Have not yet rolled five times, roll and if it is 6...
        while count < 5 and (x!=5):
            count += 1               # increase the roll count
        if count == 5:             # if that was the fifth roll of a 6
            success += 1             # add to successful 5 straight rolls of 6
    print("Occurence of five sixes is " +str(success) + " of " + str(chances) +\
           " or " + str(success/p_chances))

chances = int(float(input("Please enter number of chances to roll five sixes: ")))
print(five_die_rolls(chances))