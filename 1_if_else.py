# Variables, comments, output
a = 3
# b = a
b = 1.7
c = "abc"
d = False  # True
# student_grade = 90
# Single line comment
"""
First comment line
Second comment line
Third comment line
"""
print(a, b, c, d, 1.9, "fdgdfg", True, sep=",", end=" ")
print(type(a), type(b), type(c), type(d))

# Strings
student_full_name = "Avi Cohen"
print(student_full_name[0])  # A
print(student_full_name[0:3], student_full_name[:3])  # Avi Avi
print(student_full_name[4:])  # Cohen
print(student_full_name[1:8:2])  # v oe
print(len(student_full_name))  # 9
print(student_full_name[::-1])  # nehoC ivA

user_age = 18

if user_age > 18:
    if user_age < 60:
        print("You are over 18 and younger than 60")
    else:
        print("You are over 18 and older than 60")
elif user_age < 18:
    print("You are under 18")
else:
    print("You are 18 years old!")



# Input
# username = input("Enter your username:")
# print("Your username is:", username)
# print(type(username))


# If statements
user_salary = int(input("Enter your salary"))

if 0 <= user_salary <= 12000:
    print("Your salary with 20 percent of bonus is:", user_salary * 1.2)
elif user_salary < 0:
    print("Your salary can't be negative")
else:
    print("Your salary is bigger than 12000")




if 0 <= user_salary:
    if user_salary <= 12000:
        print("Your salary with 20 percent of bonus is:", user_salary * 1.2)
    else:
        print("Your salary is bigger than 12000")
else:
    print("Your salary can't be negative")
