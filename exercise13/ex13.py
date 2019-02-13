# this is an import
# this is how we add modules to our script
# argv is an argument variable
from sys import argv
# read the WYSS section for how to run this

# this lines unpacks argv
script, food, orange, grapefruit = argv

print("This script is called:", script)
print("Your first variable is:", food)
print("Your second variable is:", orange)
print("Your third variable is:", grapefruit)

input()

print(f"You like to eat: {food}")
