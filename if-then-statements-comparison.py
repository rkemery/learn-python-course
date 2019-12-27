# comparison operators
# == checks to see if two values are equal
# != not equals
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# create function for maximum number
# take 3 parameters as input and print out max number
# can also compare strings if "dog" == "dog"
# can compare different data types: numbers, strings, booleans
def max_num(num1, num2, num3):
    # compare numbers
    # will end up with true or false value
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    # if num1 or num2 is not the largest we can assume num3 is the biggest
    else:
        return num3
# print max number
print(max_num(3, 4, 5))