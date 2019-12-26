# execute the code and give us information back
# function communicates back to us
# return allows this - return information from functions
# when using the return keyword - it breaks us out of the function
# values after returning the statement are out of the function i.e. don't work
def cube(num):
    return num*num*num
# pass function to cube the integer 3
cube(3)
# store value from cube(4) function
result = cube(4)
# calling the function or printing it does not reveal the value of the function
# it needs the return statement in the function to reveal the value
print(cube(3))
print(cube(4))
# print the value from the cube(4) function
print(result)