# giraffe language
# all vowels become g
# dog becomes dgg
# cat becomes cgt
def translate(phrase):
    translation = ""
    # loop through every letter inside phrase
    # if vowel change to g
    # otherwise don't do anything
    for letter in phrase:
        # check to see if letter is vowel
        # if letter inside string then it's a vowel
        if letter.lower() in "aeiou":
                if letter.isupper():
                    translation = translation + "G"
                else:
                    # if letter is vowel then convert to g
                    translation = translation + "g"
        # otherwise
        else:
            # don't add a g
            translation = translation + letter
    return translation

# print out translation of whatever the user enters in
print(translate(input("Enter a phrase: ")))