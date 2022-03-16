# lists.pdf - Exercise 1
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# bottom_range_value = 1
# top_range_value = 99
#
# Getting a number to multiply every matrix element by
# while True:
#     multiply_by = int(input(
#         f"Enter a number to multiply every element of the given matrix by (between {bottom_range_value} and {top_range_value}):"))
#
#     # If the integer we will multiply the matrix elements by is at the given range
#     if bottom_range_value <= multiply_by <= top_range_value:
#         break
#
#     print(f"Wrong value. The value must be between {bottom_range_value} and {top_range_value}")
#
# # Displaying new matrix (every new element is equal to an old matrix element multiplied by the given number)
# for row in matrix:  # Displaying matrix rows
#     print("|", end="\t")
#     for column in row:  # Displaying matrix columns
#         print(column * multiply_by, end="\t")
#     print("|")

# lists.pdf - Exercise 2
matrix = []

# Getting an amount of rows a new matrix would have
while True:
    matrix_rows = int(input("Enter the matrix rows amount (a positive number):"))
    if matrix_rows > 0:
        break

    print("An amount of rows can be a positive number only")

# Getting an amount of columns a new matrix would have
while True:
    matrix_columns = int(input("Enter the matrix columns amount (a positive number):"))
    if matrix_columns > 0:
        break

    print("An amount of columns can be a positive number only")

# Building a new matrix by creating a new row and filling the created row with new values
for i in range(0, matrix_rows):
    row = []
    # Filling the next matrix row
    for j in range(0, matrix_columns):
        row.append(int(input(f"Enter another element for row {i + 1}:")))

    matrix.append(row)

# Displaying the new matrix here in the specific format
print("The matrix is:")
for row in matrix:
    for column in row:
        print(column, end=" ")
    print()
