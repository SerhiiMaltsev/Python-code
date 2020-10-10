import gradebook

syllabus = {
    'exam': 0.5,
    'hw': 0.4,
    'lab': 0.1,
}
print(gradebook.total(syllabus))
gradebook.assignment('exam', 83)
gradebook.assignment('exam', 88)
gradebook.assignment('exam', 91, 2)
print(gradebook.total(syllabus))
gradebook.assignment('hw', 100)
gradebook.assignment('hw', 100)
gradebook.assignment('hw', 70)
gradebook.assignment('hw', 0)
gradebook.assignment('hw', 100, 4)
gradebook.assignment('hw', 50)
gradebook.assignment('lab', 90)
print(gradebook.total(syllabus))
gradebook.assignment('extra', 300)
print(gradebook.total(syllabus))