# loop over a string, series of numbers, arrays

# create for loop
# for every letter inside of Giraffe Academy do something
for letter in "Giraffe Academy":
    print(letter)

# for each friend in friends array print out each element
friends = ["Jim", "Karen", "Kevin"]
# friend can be anything for whatever in array
for friend in friends:
    print(friends)
print("----------------")
for index in range(10):
    print(index)
print("----------------")
for index in range(3, 10):
    print(index)
print("----------------")
friends = ["John", "Jimmy", "Karla"]
for index in range(len(friends)):
    print(friends[index])
print("----------------")
for index in range(3):
    if index == 0:
        print("first iteration")
    else:
        print("not first")

