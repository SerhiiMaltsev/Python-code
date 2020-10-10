import regex

text = '''
CS1110-001/smile ! hi there
"hi there" but not " hi there" or "hi there " or "I said "hi" just now"
3,4, 3.0, 4.5 and -3.14159265 1110 but not 3.4.5, 1 or 1   2 or 3 - 4
Thomas Jefferson and Edmund Jennings Randolph and J. Pierpont Finch and T. Jefferson
but not T Jefferson or Thomas J. or Flannery O'Connor
'''

def full_match(regex, text):
    '''Gives a list of all complete matches'''
    ans = []
    for match in regex.finditer(text):
        ans.append(match.group(0))
    print(ans)
    return ans


ns = full_match(regex.nospace, text)
print('nospace:',
    'CS1110-001/smile' in ns,
    '!' in ns,
    'hi there' not in ns,
    '' not in ns)



q = full_match(regex.quotation, text)
print('quotation:',
    '"hi there"' in q,
    '" hi there"' not in q,
    '"hi there "' not in q,
    '"I said "hi" just now"' not in q)

tn = full_match(regex.twonum, text)

print('twonum:',
    '3,4' in tn,
    '3.0, 4.5' in tn,
    '-3.14159265 1110' in tn,
    '3.4.5, 1' not in tn,
    '1   2' not in tn,
    '3 - 4' not in tn)

for match in regex.twonum.finditer(text):
    if match.group(0) == '3,4':
        print('  match1:', '3' in match.groups(), '4' in match.groups())
    if match.group(0) == '-3.14159265 1110':
        print('  match2:', '-3.14159265' in match.groups(), '1110' in match.groups())