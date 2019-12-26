# if statements tell python to make decisions
# execute certain code when certain conditions are true
# allow our programs to respond to input that is given
# create boolean variable
is_male = False
is_tall = True

# if declaration
# can put as much code as you want
# if person is either male or if they are tall then do something
# when one or both of the values are true
if is_male or is_tall:
    # condition when true
    print("You are a tall male.")
    # else = otherwise
# check to see if male and not tall
# not function negatives boolean value inside
elif is_male and not(is_tall):
    print("You are a short male.")
# check to see if not male and tall
elif not(is_male) and is_tall:
    print("You are not a male, but are tall.")
else:
    # when both booleans are false
    print("You are not a male and not tall.")