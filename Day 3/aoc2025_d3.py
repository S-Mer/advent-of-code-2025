# IT'S BATTERY TIME

# An initial thought: you can most likely just grab the largest digit you can find in the sequence, assuming it isnt the last digit (ex. 90>anything beginning with a lower digit, as with 80, so on.)

# don't actually even need to store the indices

joltage_list = []

with open("input.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"on line number {line_number}. current joltages: {len(joltage_list)}: {line}")

        # Find first battery. Highest number which isn't the very last character.
        for num1 in range(9, -1, -1):
            find_index = line[0:len(line)-2].find(str(num1)) # TODO: find why -1 didnt work as expected
            if find_index >= 0:
                print(f"Index: {find_index}")
                first_battery_val = num1
                
                print(f"First battery found: {first_battery_val}\nNew search substring: {line[find_index+1:]}")

                # Create new substring line to search through for second battery
                for num2 in range(9, -1, -1):
                    if line[find_index+1:].find(str(num2)) >= 0:
                        second_battery_val = num2
                        joltage_list.append(first_battery_val*10 + second_battery_val) # Or just recast them str and take the int of their summation
                        print(f"Optimal battery configuration found: {first_battery_val*10 + second_battery_val}")
                        break
                break

joltage_list
sum(joltage_list)


# PART TWO: Turn on twelve batteries; logic remains

# Initial thoughts: Current solution should be generalizable with a better loop. Take the substring twelve characters short to search for the largest. The next digit will be the largest in that substring + 1 more original length, etc. Should do a better job at generalizing and also appending the values now, though.

joltage_list = []

with open("input.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        # print(f"on line number {line_number}. current joltages: {len(joltage_list)}: {line}")

        line_batteries = ""
        found_batteries = 0
        line_substring = line

        # Find first battery. Highest number which isn't the very last character.
        while found_batteries < 12:
            for num in range(9, -1, -1):
                find_index = line_substring[0:len(line_substring)-12+found_batteries].find(str(num)) # Added 10 more characters of required space, and a metric which updates given that we found the previous battery
                if find_index >= 0:
                    line_batteries += str(num)
                    found_batteries += 1
                    line_substring = line_substring[find_index+1:]
                    
                    # print(f"Battery {found_batteries} found: {line_batteries[found_batteries-1:found_batteries]}\nNew search substring: {line_substring}")
                    break

        joltage_list.append(int(line_batteries))

joltage_list
sum(joltage_list)