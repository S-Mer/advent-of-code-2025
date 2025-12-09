import re
import math

# Read line by line
# If not the last line, then just keep them as the values 
with open("test_case.txt", "r") as file:
    input_file = file.read()

# len(input_file)
# len(input_file.split("\n"))

# print(input_file.split("\n"))

# for i in range(0,4):
#     print(i)

# len(input_file.split("\n"))
# input_file.split("\n")

# Every line should be identical length. Initialize the length of the first line to compare to during our asserts.
expected_len = len(input_file.split("\n")[0].split())

# Assert all whitespace-split lines are the same length, assert that the last line i just addition or multiplication
for i in range(0, len(input_file.split("\n"))):

    print(f"On line {i}")
    assert len(input_file.split("\n")[i].split()) == expected_len, "Line is not of expected length"

    if i < len(input_file.split("\n"))-1:
        print("Checking line")
        assert re.match("^(\\s*\\d+\\s*)+$", input_file.split("\n")[i]), "Doesn't match the string format"
    else: # if last line
        print("Checking last line")
        assert re.match("^(\\s*[\\*\\+]{1}\\s*)+$", input_file.split("\n")[i]), "Last line doesn't match format"
print("Success!")

# If the lengths all match, then we can just iterate from 1 to the length, and for each we get our sum or product value. Then move on.

answer_list = []

# input_file.split("\n")[expected_len-1].split()
# [expected_len]
print(input_file.split("\n")[expected_len-1].split()[0])
for element in range(0, expected_len):
    
    # Find the operation
    operation = input_file.split("\n")[len(input_file.split("\n"))-1].split()[element]
    print(f"On element num {element}. Identified operation: {operation}")

    operands = []

    for line in range(0, len(input_file.split("\n"))-1):
        operands.append(int(input_file.split("\n")[line].split()[element]))
        print(f"Adding operand {int(input_file.split("\n")[line].split()[element])} from line {line}")

    print(operands)
    # Perform the operation
    if operation == "*":
        answer_list.append(math.prod(operands))
    else: #operation == "+"
        answer_list.append(sum(operands))

operands
# How can we extract the last character of an int?
# inefficient, but can cast to str, take last character, revert to int
int(str(operands[2])[len(str(operands[2]))-1])

# Reformat the operands
def reformat_operands(operand_list):
    for operand in operand_list:
        
        

# print(answer_list)
print(sum(answer_list))

###########################################################
##### Part two: now column-wise, right to left digits #####
###########################################################

# What do we need to change? We need to assess both the length and order of each element in the operand list, then modify to fit this new math before performing the operation. I think this should only change lines within the if-else operation block

answer_list = []

# input_file.split("\n")[expected_len-1].split()
# [expected_len]
print(input_file.split("\n")[expected_len-1].split()[0])
for element in range(0, expected_len):
    
    # Find the operation
    operation = input_file.split("\n")[len(input_file.split("\n"))-1].split()[element]
    print(f"On element num {element}. Identified operation: {operation}")

    operands = []

    for line in range(0, len(input_file.split("\n"))-1):
        operands.append(int(input_file.split("\n")[line].split()[element]))
        print(f"Adding operand {int(input_file.split("\n")[line].split()[element])} from line {line}")

    # Perform the operation
    if operation == "*":
        answer_list.append(math.prod(operands))
    else: #operation == "+"
        answer_list.append(sum(operands))

# print(answer_list)
print(sum(answer_list))