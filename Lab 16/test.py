import lous_list

print(lous_list.instructors('STS'))

print('-'*40)

for f in lous_list.class_search('CS', level=3000, not_before=1100, not_after=1100):
    print(f)

print('-'*40)

print(len(lous_list.class_search('CS', False, 3000, not_after=1300)))