"""
Ravindra Arjune
Lab 3, Python review
"""

print("---------> Example 1: control flow <----------- ")
labs = int(input("Enter labs' grade: "))
exams = int(input("Enter exams' grade: "))

finalgrade = (labs + exams) / 2
gpa = ''


if (100>= finalgrade>=90):
    gpa = 'A'
elif (90>finalgrade>=80):
    gpa = 'B'
elif (80>finalgrade>=70):
    gpa = 'C'
elif (70>finalgrade>=60):
    gpa = 'D'
elif (60>finalgrade>=0):
    gpa = 'F'
else:
    gpa = 'UNDEFINED'

print(f"Your final grade in the class is {finalgrade} = {gpa}")

