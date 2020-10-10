#Serhii Maltsev sm5zj
import urllib.request, re

def name_to_URL(name):
    '''
    This function is used to transform the name of the employee to the name for the link
    :param name: str name of the employee
    :return: returns str name of the employee in the form of link
    '''
    if ',' in name:
        last_name = ''
        comma_location = name.find(',')
        for i in range(0, comma_location):
            last_name += name[i]
        name = name.replace(last_name, '')
        name = name.replace(',', '')
        name = name.replace('.', '')
        name += ' ' + last_name
        name = name[1:len(name)]
        name = name.replace(' ', '-')
        name = name.lower()
    else:
        name = name.replace('.', '')
        name = name.replace(' ', '-')
        name = name.lower()
    return name

def full_match(regex, text):
    '''
    This function is used to create the array of matches for the regular expression
    :param regex: regular expression
    :param text: text that is used to search for matches
    :return: returns an array of all matches
    '''
    ans = []
    for match in regex.finditer(text):
        ans.append(match.group(0))
    return ans

def money_finder (info):
    '''
    This function is used to find the salary of the employee
    :param info: str info form the website
    :return: returns salary of the employee
    '''
    search_money = re.compile(r"total gross pay: \$\d+[,]\d+")
    salary = full_match(search_money, info)
    salary = salary[0]
    index_of_sign = salary.find("$")
    salary = salary[index_of_sign:len(salary)]
    salary = salary.replace('$', '')
    salary = salary.replace(',', '')
    salary = salary + ".0"
    return salary

def job_finder (info):
    '''
    This function returns job title of the employee
    :param info: str info form the website
    :return: returns the job title of the employee
    '''
    search_job = re.compile(r"id=\"personjob\">[^<]+")
    title = full_match(search_job, info)
    title = title[0]
    title = title.replace('Job title: ', '')
    title = title.replace('&amp;/or', '&/or')
    title = title.replace('&#39;', '\'')
    title = title.replace('id=\"personjob\">', '')
    return title

def rank_finder(info):
    '''
    This function returns the rank of the employee
    :param info: str info form the website
    :return: returns the rank of the employee
    '''
    search_rank = re.compile(r"rank</td><td>[\d\,]+")
    rank = full_match(search_rank, info)
    if rank == []:
        rank = 0
    else:
        rank = rank[0]
        rank = rank.replace('rank</td><td>', '')
        rank = rank.replace(',', '')
    return rank

def report (name):
    '''
    This is main function which is used to execute all other functions
    :param name: the name of the employee
    :return: information about employee
    '''
    name = name_to_URL(name)
    link = 'https://cs1110.cs.virginia.edu/files/uva2018/' + name
    try:
        stream = urllib.request.urlopen(link)
        info = stream.read()
        info = str(info)
        money = money_finder(info)
        job = job_finder(info)
        rank = rank_finder(info)
    except:
        job = None
        money = 0
        rank = 0
    return job, money, rank
