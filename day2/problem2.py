# Open the file
file = open("input.txt", "r")
# Read the file into a list
intCode = file.read().split(',')
# Get the length of the list
lengthOfIntCode = len(intCode)

# Loop through the list
for i in intCode:
    if int(i) == 1:
        i = int(i + 1) + int(i + 2)
        print(intCode)
    elif int(i) == 2:
        print("done")
    elif int(i) == 99:
        print("done")
    else:
        print("done")

# If the first entry (opcode) is a 99, halt the code
# If you encounter an unkown opcode, it means something went wrong
# If the opcode is 1, it adds together numbers read from two positiions and stores the result in the third position
# The three integers following the opcode are the locations

# print(lengthOfIntCode)

# Close file
file.close()