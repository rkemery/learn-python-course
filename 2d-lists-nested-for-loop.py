# create a list
# make all elements inside the lists also lists
# all elements in number grid are lists
# 4 rows and 3 columns
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid)
print("-------------")
# print row 0 and column 0
print(number_grid[0][0])
# print row 0 and column 1
print(number_grid[0][1])
print("-------------")
# nested for loop
for row in number_grid:
    # each individual column inside array
    for col in row:
        print(col)

