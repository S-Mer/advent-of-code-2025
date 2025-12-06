with open("input.txt", "r") as file:
    input_file = file.read()

input_lines = input_file.split("\n")
input_lines

# Ensure the only characters in input_lines are @ or .

def check_neighbors(line_num, char_num):
    num_rolls = 0

    neighbor_list = []

    assert input_lines[line_num][char_num] == "@"
    
    # print(f"line range: {line_num-1} - {line_num+2}")

    for line in range(line_num-1, line_num+2):
        for char in range(char_num-1, char_num+2):
            try:
                if (char >= 0) and (line >= 0): # forgot that if you negative index a string, it will return the index at the back rather than an error. capture this in an "if"
                    # neighbor_list.append(input_lines[line][char])
                    # print(f"checking line {line} and char num {char}")
                    if input_lines[line][char] == "@":
                        num_rolls += 1

            except:
                pass

    # print(neighbor_list)
    
    # if num_rolls - 1 < 4:
    #     print(f"roll added. {num_rolls-1} @s\n")

    return num_rolls - 1 # Subtract 1 because it checks itself, and this will only run when it's a roll.

line_tracker = -1
eligible_rolls = 0

for line in input_lines: # Can avoid first and last row assuming these edge cases aren't allowed.
    line_tracker += 1

    for char in range(0, len(line)): # should rolls update after a roll is removed? Maybe that's part 2. We won't assume that for now.
        # print(f"char {char} = {line[char]}")
        assert line[char] == "@" or line[char] == "."
        if line[char] == "@":
            # print(f"Checking char # {char} on line {line_tracker}")
            # Naive way to do it here, search all 9 each time and add up.- what are the obvious improvements? remember your last number and rows and always store that so you don't have to re-search each time? And once you lookup a future value, you store that too until used?
            # TODO: add a stop condition if 4 is reached. should make it faster.
            # print(f"Inputting function values: line number {line_tracker}, char number {char}")
            if check_neighbors(line_tracker, char) < 4:
                # print("Roll added")
                eligible_rolls += 1

eligible_rolls

#####################
##### PART TWO: #####
#####################
# As suspected, we now will iterate on removal until no more can be removed.
# Updates which would need to be made to accommodate this: 
#                                               -copy the beginning matrix (probably optional)
#                                               - make a step function which iterates on it, or else maybe (while) loops while eligible_rolls > 0

with open("input.txt", "r") as file:
    input_file = file.read()

input_lines = input_file.split("\n")

print(f"Total lines: {len(input_lines)}")
print(f"First few lines: {input_lines[:3]}")
print(f"Total @ characters: {sum(line.count('@') for line in input_lines)}")

def check_neighbors(line_num, char_num):
    num_rolls = 0

    for line in range(line_num-1, line_num+2):
        for char in range(char_num-1, char_num+2):
            try:
                if (char >= 0) and (line >= 0): 
                    if input_lines_copy[line][char] == "@":
                        num_rolls += 1

            except:
                pass

    return num_rolls - 1 # Subtract 1 because it checks itself, and this will only run when it's a roll.

line_tracker = -1
eligible_rolls = 0
eligible_rolls_iterated = 0

# Make removable list a list, not dictionary. have it store the i,j values csv'ed, and then can access them easily with a loop to update the matrix copy. then we iterate until eligible rolls is 0
removable_set = set()

# Create a live editable copy of the original matrix, and update this live as we find the rolls which can be removed at the end of a line? Otherwise use our dictionary of the removables and reset it after each full matrix run. 
input_lines_copy = input_lines.copy()

run = 1
#
# Where to reinitialize the line tracker and eligible rolls between runs?
while True:

    print(f"on run {run}")
# 
    for line in input_lines_copy:
        line_tracker += 1

        for char in range(0, len(line)):
            assert line[char] == "@" or line[char] == "."
            if line[char] == "@":
                if check_neighbors(line_tracker, char) < 4:
                    eligible_rolls += 1
                    removable_set.add(str(line_tracker) + "," + str(char))
    
        if eligible_rolls == 0:
            print("Iterations finished. Breaking here!")
            break
        else: # Add to the eligible roll counter and recreate the new input lines for the next run. Reinitialize the line tracker and eligible rolls
            eligible_rolls_iterated += eligible_rolls

            print(f"Finished run {run}. Added eligible rolls {eligible_rolls}")

            # Reinitialize for next run
            eligible_rolls = 0
            line_tracker = -1
            
            run += 1

            for roll in removable_set:
                linenum = int(roll.split(",")[0])
                charnum = int(roll.split(",")[1])

                print(f"replacing line {linenum} char {charnum}")
                # Repopulate the new input_lines with the rolls removed
                assert input_lines_copy[linenum][charnum] == "@", "Character was already not @"

                input_lines_copy[linenum] = input_lines_copy[linenum][:charnum] + "." + input_lines_copy[linenum][charnum+1:] # This can't be the best way to change one character of a string

            removable_set = set()
                

eligible_rolls

eligible_rolls_iterated # showing 61, but we know it should be multiple thousands

# len(removable_list) # actually 140x140, so the dictionary stops at 140 since it doesnt accept any other unique entries in these value ranges. it will just think i'm accessing line 140 140x rather than doing 140x140 (potential) entries

# TODO: how to make it endlessly iterable until eligible_rolls is 0 at the end of a run?. make it check at the end somehow?

print("foo,bar".split(","))