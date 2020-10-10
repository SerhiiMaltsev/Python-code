import gpa

gpa.add_course(4.0, 3)
print(gpa.gpa(), gpa.credit_total())

gpa.add_course(3.3)
print(gpa.gpa(), gpa.credit_total())

gpa.add_course(2.3, 4)
print(gpa.gpa(), gpa.credit_total())
