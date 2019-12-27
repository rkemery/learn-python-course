# dictionary allows us to store information in key value pairs
# can access information by key value
# convert Jan to January, Mar to March
# good use case for a dictionary

# create dictionary
# dictionary entries must be unique
# cannot have duplicate entries
# can also enter keys as numbers
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
# print out dictionary entries
print(monthConversions["Jan"])
print(monthConversions["Feb"])
print(monthConversions.get("Mar"))
# get invalid entry / default value == Jan
print(monthConversions.get("Luv", "Not a valid key"))