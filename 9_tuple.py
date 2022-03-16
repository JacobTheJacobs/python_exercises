# Tuples
numbers_tuple = (12, 23, 34, 45, 56, 67)
print(numbers_tuple[1])
print(numbers_tuple[1:5])

print(23 in numbers_tuple)
print(len(numbers_tuple))

grades_tuple = ([12, 23, 34], [45, 56, 67])
grades_tuple[0][1] = 99
print(grades_tuple[0])
