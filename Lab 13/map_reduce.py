#Serhii Maltsev sm5zj

def mymap(function, list):
    """
    This function uses function for every element of the list
    :param function: is a function that is used for every element of the list
    :param list: is the list that will be used as a parameter of the function
    :return: returns the changed list
    """
    changed_list = []
    for i in range(0, len(list)):
        changed_list.append(function(list[i]))
    return changed_list

def myreduce(function, list):
    """
    This function uses function for each pair of elements of array
    :param function: is a function that will be used for the elements of array
    :param list: is a list that will be used for the execution of function
    :return: returns the value of the function execution for the last pair
    """
    x = list[0]
    for i in range(1, len(list)):
        x = function(x, list[i])
    return x
