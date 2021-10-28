heights = input('enter the heights: ').split()

sum_of_heights = 0
for height in heights:
    sum_of_heights += int(height)

students = 0
for student in heights:
    students += 1

average_height = sum_of_heights / students
print(f'the average height is {average_height}.')
