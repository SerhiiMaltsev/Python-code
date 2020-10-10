#Serhii Maltsev sm5zj
import urllib.request

def instructors (department):
    """
    This function is used to create a list of professors of a particular department
    :param department: str parameter that defines the department for the professors search
    :return: returns the list of professors
    """
    stream = urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/louslist/"+department)
    text = stream.readlines()

    arrayOfClasses = []
    arrayOfProfessors = []

    for line in text:
        arrayOfClasses.append(line.decode("UTF-8").strip().split("|"))

    for i in arrayOfClasses:
        if ((i[4] in arrayOfProfessors) != True):
            arrayOfProfessors.append(i[4])

    finalArrayOfProfessors = []
    for i in arrayOfProfessors:
        x = i.find("+")
        if (x >= 0):
            i = i[0:x]
            finalArrayOfProfessors.append(i)
        else:
            finalArrayOfProfessors.append(i)

    arrayWithoutRepetitions = []
    for i in finalArrayOfProfessors:
        if (i in arrayWithoutRepetitions) == False:
            arrayWithoutRepetitions.append(i)

    finalArrayOfProfessors = arrayWithoutRepetitions
    finalArrayOfProfessors.sort()
    return finalArrayOfProfessors

def class_search (dept_name, has_seats_available = True, level = None, not_before = None, not_after = None):
    """
    This function is used to search all classes that satisfy the parameters
    :param dept_name: str name of department where search is processed
    :param has_seats_available: bool that is used to determine if the seats for the class are available
    :param level: str level of class
    :param not_before: int the earliest time of the start of the class
    :param not_after: int the latest time of the end of the class
    :return: the list of classes that satisfy the requirements 
    """
    stream = urllib.request.urlopen("http://cs1110.cs.virginia.edu/files/louslist/"+dept_name)
    text = stream.readlines()

    arrayOfClasses = []

    for line in text:
        arrayOfClasses.append(line.decode("UTF-8").strip().split("|"))

    arrayOfClasses1 = []
    for i in arrayOfClasses:
        if has_seats_available:
            if int(i[15]) < int(i[16]):
                arrayOfClasses1.append(i)
        else:
            arrayOfClasses1 = arrayOfClasses

    arrayOfClasses2 = []
    for i in arrayOfClasses1:
        if level != None:
            if i[1][0] == str(level)[0]:
                arrayOfClasses2.append(i)
        else:
            arrayOfClasses2 = arrayOfClasses1

    arrayOfClasses3 = []
    for i in arrayOfClasses2:
        if not_before:
            if int(i[12]) >= not_before:
                arrayOfClasses3.append(i)
        else:
            arrayOfClasses3 = arrayOfClasses2

    arrayOfClasses4 = []
    for i in arrayOfClasses3:
        if not_after:
            if int(i[12]) <= not_after:
                arrayOfClasses4.append(i)
        else:
            arrayOfClasses4 = arrayOfClasses3

    return arrayOfClasses4
