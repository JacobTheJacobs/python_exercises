# list comprehension python
# salaries_list = [12300, 25000, 30500, 10000]
# salary_bonus = 1.15
# minimum_valid_salary = 12500
# salaries_with_bonus = []
#
# for salary in salaries_list:
#     if salary > minimum_valid_salary:
#         salaries_with_bonus.append(round(salary * salary_bonus))
#
# print(salaries_with_bonus)
#
# salaries_with_bonus = [round(salary * salary_bonus) for salary in salaries_list if salary > minimum_valid_salary]
# print(salaries_with_bonus)

grades_list = [53, 67, 88, 91, 100, 13, 69]
pass_grade = 56
grade_factor = 1.05
highest_grade = 100
pass_grades_with_factor = []

for grade in grades_list:
    if pass_grade <= grade <= highest_grade:
        pass_grades_with_factor.append(
            round(grade * grade_factor) if grade * grade_factor <= highest_grade else highest_grade)

print(pass_grades_with_factor)

pass_grades_with_factor = [round(grade * grade_factor) if grade * grade_factor <= highest_grade else highest_grade for
                           grade in
                           grades_list if pass_grade <= grade <= highest_grade]
print(pass_grades_with_factor)
