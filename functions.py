# a function is a collection of code that performs a specific task
# def - defines a function creation
# tab indent implies commands are in the function
def say_hi():
    print("Hello User")
# call function
print("Top" + " --------")
say_hi()
print("Bottom" + " --------")
# parameter is a piece of information that you give to a function
# require name and age to be present for input when calling then print the name and age
# convert age to a string value to print it
def say_hi_2(name, age):
    print("Hello " + name + ", you are " + str(age))
say_hi_2("Rick", 35)
say_hi_2("Jacqueline", 32)