#Serhii Maltsev sm5zi

def check(cardNumber):
    """
    This function performs the calculations that are required to determine is the card number valid or not
    :param cardNumber: integer number which represents the number of credit card
    :return: True or False depending on the validity of card
    """
    cardNumberString = str(cardNumber)
    evenNumbers = cardNumberString[1:len(cardNumberString):2]
    oddNumbers = cardNumberString[0:len(cardNumberString):2]
    sumOfEven = 0
    sumOfOdd = 0
    newOdd = ''

    if len(cardNumberString)%2 == 0:
        for i in evenNumbers:
            sumOfEven += int(i)
        for i in oddNumbers:
            newOdd += str(int(i)*2)
        for i in newOdd:
            sumOfOdd += int(i)
    else:
        for i in oddNumbers:
            sumOfEven += int(i)
        for i in evenNumbers:
            newOdd += str(int(i) * 2)
        for i in newOdd:
            sumOfOdd += int(i)

    if (sumOfOdd) == None:
        sumOfOdd = 0
    if (sumOfEven) == None:
        sumOfEven = 0
    if (sumOfEven+sumOfOdd)%10 == 0:
        return True
    else:
        return False
