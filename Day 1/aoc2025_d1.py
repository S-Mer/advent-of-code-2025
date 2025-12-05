# Password is the number of times this sequence passes 0.

# Assume a starting point of 50.

import re
import math

file_name = "puzzle_input.txt"

# Puzzle one: Lands EXACTLY on 0
current_point = 50
last_point = 50
cross_0_counter = 0

with open(file_name, 'r') as file:
    for line_number, line in enumerate(file, 1):
        # print(f"Line {line_number}: {line.strip()}")
        
        assert re.match("^[LR]\\d+$",line.strip())

        direction = line.strip()[0]
        distance = int(line.strip()[1:])
        
        print(f"line number: {line_number}. current_point: {current_point}. Moving {direction} {distance}.")

        last_point = current_point

        if direction == "L":
            current_point = (current_point - distance) % 100
        else: 
            current_point = (current_point + distance) % 100
        if current_point == 0:
            cross_0_counter += 1
        print(f"Now at {current_point}")

cross_0_counter

#############################################
##### Puzzle 2: Lands on 0 at any point #####
#############################################
current_point = 50
last_point = 50
cross_0_counter = 0

with open(file_name, 'r') as file:
    for line_number, line in enumerate(file, 1):
        # print(f"Line {line_number}: {line.strip()}")
        
        assert re.match("^[LR]\\d+$",line.strip())

        direction = line.strip()[0]
        distance = int(line.strip()[1:])

        # Double-checking it's never 0
        assert distance != 0
        
        print(f"line number: {line_number}. current_point: {current_point}. Moving {direction} {distance}.")

        last_point = current_point

        # Create a separate increment for distances > 100, then all following conditions can deal with <100 cases
        if distance > 100: 
            print(f"Distance {distance} is over 100! incrementing 0 cross by {distance % 100} ")
            cross_0_counter += math.floor(distance / 100)
            distance = distance % 100

        if direction == "L":
            current_point = (current_point - distance) % 100
            if (current_point == 0) | ((last_point != 0) & ((last_point - distance) < 0)): 
                cross_0_counter+=1
                print("We crossed 0 1 time!")
        else: 
            current_point = (current_point + distance) % 100
            if (current_point == 0) | ((last_point != 0) & ((last_point + distance) > 100)): 
                cross_0_counter+=1
                print("We crossed 0 1 time!")
        print(f"Now at {current_point}")

cross_0_counter


if ((current_point - distance) != current_point & distance%100 != 0)