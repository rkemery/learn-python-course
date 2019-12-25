lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "John"]
# put friends list in alphabetical order
friends.sort()
# put lucky_numbers in ascending order
lucky_numbers.sort()
# appends another list to a list - add 2 lists together
friends.extend(lucky_numbers)
print(friends)
# append item to end of the list
friends.append("Creed")
print(friends)
# insert value Kelly at index position 1 in friends list
friends.insert(1, "Kelly")
print(friends)
# remove Jim from list
friends.remove("Jim")
print(friends)
# removes last item in list
friends.pop()
print(friends)
# get index value where string exists
print(friends.index("Kevin"))
print(friends.index("Oscar"))
# count how many times John exists in friends list
print(friends.count("John"))
# copies current state of friends list
friends2 = friends.copy()
print(friends2)
# clear list
friends.clear()
print(friends)