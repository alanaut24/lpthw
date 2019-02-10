# creates variable types of people and assigns value 10
types_of_people = 10
# Sets variable x to string with an embedded format string. Format strings
# are way to insert (embed) a thing within a string such that the final
# output will include the thing or whatever operation the thing is part of.
x = f"There are {types_of_people} types of people."

# sets variable binary to binary = slightly redundant but necessary
binary = "binary"

# sets variable do_not to don't
do_not = "don't"

# set variable y to string with two embedded format strings
# binary and do_not
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaulation = "Isn't that joke so funny?! {}"

print(joke_evaulation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
