# ID's with repeated patterns between the first and second half of the string are erroneous. However, there are only a few product ID ranges to search. Answer is the sum of all invalid ID's

# Idea: Initialize empty list of invalid IDs. Search "for x in ranges" for strings where the 0, len(x)/2 is the same as the len(x)/2+1, len(x) and append to list.

# Find ID ranges from file by parsing on , and -

# Step one: read in the text file

import re

with open("input.txt", "r") as file:
    input_file = file.read()

input_file

input_file = input_file.strip() # Remove newline char

assert re.match("^(\\d+-\\d+,?)+$", input_file)

invalid_ids = []
# For every comma-split segment, extract the numbers from the hyphen-split sections, search for the repeat sequences
id_segments = input_file.split(",")
for id_range in id_segments:
    id_nums = id_range.split("-")

    print(f"On ID Range: {id_nums}")
    start_num = int(id_nums[0])
    end_num = int(id_nums[1])

    for num in range(start_num,end_num+1):
        str_num = str(num)
        if len(str_num)%2 == 0:
            first_half = str_num[0:len(str_num)//2]
            second_half = str_num[len(str_num)//2:len(str_num)]
            if first_half == second_half:
                invalid_ids.append(num)

invalid_ids
sum(invalid_ids)


## PART TWO: patterns can now be repeated any number of times. A new (perhaps inefficient) pass would be to iterate through all 2+ length segments of the number as a string (up to half its length) to verify that it's not a repeated pattern. Let's try

invalid_ids = set()
# For every comma-split segment, extract the numbers from the hyphen-split sections, search for the repeat sequences
id_segments = input_file.split(",")
for id_range in id_segments:
    id_nums = id_range.split("-")

    print(f"On ID Range: {id_nums}")
    start_num = int(id_nums[0])
    end_num = int(id_nums[1])

    for num in range(start_num,end_num+1):
        str_num = str(num)
        for i in range(1, len(str_num)//2+1):
            
            # Smallest sequence would be the first two characters
            pattern = str_num[0:i]
            # print(f"First subset: {pattern}. Repetition would be {len(str_num) // len(pattern)}")
            if str_num == (pattern * (len(str_num) // len(pattern))): 
                invalid_ids.add(num)

invalid_ids
sum(invalid_ids)

id_segments

invalid_ids = []
start_num = int(2214325)
end_num = int(2229214)

for num in range(start_num,end_num+1):
    str_num = str(num)
    for i in range(2, len(str_num)//2+1):
        
        # Smallest sequence would be the first two characters
        pattern = str_num[0:i]
        # print(f"First subset: {pattern}. Repetition would be {len(str_num) // len(pattern)}")
        if str_num == (pattern * (len(str_num) // len(pattern))): 
            invalid_ids.append(num)
invalid_ids