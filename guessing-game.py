# if statements
# while loops
# variables
# specify secret word
# user can interact with program
# try to guess secret word
# user can keep guessing until secret word is correct

secret_word  = "giraffe"
# set guess to empty string values
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# prompt user to input secret word
# if they don't guess it correctly
# prompt to enter again
# while loop
# as long as guess does not equal secret word
# and they are not out of guesses
# keep looping through
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
# if out of guesses then user ran out of guesses
# otherwise, they are not and they guessed correctly
if out_of_guesses:
    print("You lose.")
else:
    print("You win!")