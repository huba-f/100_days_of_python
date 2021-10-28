student_scores = {
    'harry': 92,
    'joe': 85,
    'huba': 45,
    'elon': 79,
}
student_grades = student_scores
for student in student_grades:
    if student_scores[student] >= 91 and student_scores[student] <= 100:
        student_grades[student] = 'Outstanding'
    elif student_scores[student] >= 81 and student_scores[student] <= 90:
        student_grades[student] = 'Exceeds expectations'
    elif student_scores[student] >= 71 and student_scores[student] <= 80:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'failure'
print(student_grades)