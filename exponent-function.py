# exponent function
# allows us to take a certain number and raise to a power

# 2 raised to the 3rd power
print(2**3)
print("---------------")
# for loop to create exponent function
def raise_to_power(base_num, pow_num):
    # result of the math is stored in variable
    result = 1
    # range through a collection of numbers
    # range pow_num means if 3 is pow_num then loop through 3 times
    # loop through for loop as many times as pow_num
    for index in range(pow_num):
        result = result * base_num
    return result

# 3 to the 2nd power
print(raise_to_power(2, 3))