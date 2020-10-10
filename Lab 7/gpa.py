#Serhii Maltsev sm5zj@virginia.edu
gpaValue = 0
creditsNumber = 0

def add_course(grade, number_of_credits=3):
    global gpaValue, creditsNumber
    x = grade * number_of_credits
    y = gpaValue * creditsNumber
    sumOfCredits = number_of_credits + creditsNumber
    gpaInFunction = (x+y)/sumOfCredits
    gpaValue = gpaInFunction
    creditsNumber = sumOfCredits

def gpa():
    return gpaValue

def credit_total():
    return creditsNumber
