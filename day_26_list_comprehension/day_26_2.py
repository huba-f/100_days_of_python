import pandas


student_dict = {
    'student': ['Huba', 'Kalapacs', 'kutya'],
    'score': [12, 23, 45]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)
