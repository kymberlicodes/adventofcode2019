import math

# Open the file
file = open("input.txt", "r")
# Read the file into a list
mass = file.readlines()
# Initialize the sum
sum = 0

# Define a function that takes in the mass, divides it by 3, rounds down to nearest integer, and subtracts 2
def calculate(mass):
    # Preform calculations
    mass = math.floor(mass / 3) - 2
    return mass

# Loop through each item in mass list, update sum for each item
for i in mass:
    sum = sum + calculate(int(i))

# Print final sum
print(sum)

# Close file
file.close()
