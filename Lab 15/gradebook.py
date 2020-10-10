#Serhii Maltsev sm5zj
grades = {}
weights = {}

def assignment(type, grade, weight = 1):
    """
    This function adds grade to the dictionary
    :param type: string value of the type of work
    :param grade: int value of grade
    :param weight: in value of credits
    :return: N/A
    """
    global grades, weights
    if ((type in grades.keys()) == False):
        grades[type] = 0
        weights[type] = 0
    grades[type] += grade * weight
    weights[type] += weight

def total(syllabus):
    '''
    This function counts gpa according to the weight of each type of work
    :param syllabus: is the syllabus that is used to count gpa
    :return: gpa value
    '''
    gpa = 0
    for i in syllabus.keys():
        if (i in grades.keys()):
            gpa += (grades[i]/weights[i])*syllabus[i]
    return gpa
