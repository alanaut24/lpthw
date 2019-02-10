# set variable formatter to string with embedded formats
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

# No quotes when calling variables
print(formatter.format(formatter, formatter, formatter, formatter))

# Formatting for the array
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
