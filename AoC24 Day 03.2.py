import csv
import time
import sys
import re

#Start Performance Counter
startTime = time.perf_counter()

def read_csv_file(file_path):
    data_list = []

    try:
        with open(file_path, mode = 'r', encoding = 'utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                data_list.append(str(row)[2:-2])

        return data_list

    except FileNoteFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def parse_memory(memory, pattern, do_dont):
    mem_length = len(memory)
    #Add padding to the end of the string to deal with out of bound errors
    padded_memory = memory + "...."
    product_sum = 0
    #do_dont = 1
    iter_count = 0
    i = 0
    while i <= mem_length:
        left_part = 0
        right_part = 0
        iter_count += 1
        if re.match(pattern, padded_memory[i:i+12]):
            left_part = int("".join(filter(str.isdigit, padded_memory[i:i+12].split(",")[0])))
            right_part = int("".join(filter(str.isdigit, padded_memory[i:i+12].split(",")[1])))
            product_sum += left_part * right_part * do_dont
            i = i + 12
        elif re.match(pattern, padded_memory[i:i+11]):
            left_part = int("".join(filter(str.isdigit, padded_memory[i:i+11].split(",")[0])))
            right_part = int("".join(filter(str.isdigit, padded_memory[i:i+11].split(",")[1])))
            product_sum += left_part * right_part * do_dont
            i = i + 11    
        elif re.match(pattern, padded_memory[i:i+10]):
            left_part = int("".join(filter(str.isdigit, padded_memory[i:i+10].split(",")[0])))
            right_part = int("".join(filter(str.isdigit, padded_memory[i:i+10].split(",")[1])))
            product_sum += left_part * right_part * do_dont
            i = i + 10
        elif re.match(pattern, padded_memory[i:i+9]):
            left_part = int("".join(filter(str.isdigit, padded_memory[i:i+9].split(",")[0])))
            right_part = int("".join(filter(str.isdigit, padded_memory[i:i+9].split(",")[1])))
            product_sum += left_part * right_part * do_dont
            i = i + 9
        elif re.match(pattern, padded_memory[i:i+8]):
            left_part = int("".join(filter(str.isdigit, padded_memory[i:i+8].split(",")[0])))
            right_part = int("".join(filter(str.isdigit, padded_memory[i:i+8].split(",")[1])))
            product_sum += left_part * right_part * do_dont
            i = i + 8
        elif padded_memory[i:i+7] == "don't()":
            if do_dont == 1:
                do_dont = toggle_do_dont(do_dont)
            i = i + 7
        elif padded_memory[i:i+4] == "do()":
            if do_dont == 0:
                do_dont = toggle_do_dont(do_dont)
            i = i + 4
        else:
            i += 1

    print(iter_count, product_sum)
    print(f"Ending do_dont: {do_dont}")
    return product_sum

def toggle_do_dont(passed_do_dont):
    global do_dont
    do_dont = abs(passed_do_dont - 1)
    return do_dont

csv_file_path = 'AoC24 Day 03.csv'
data = read_csv_file(csv_file_path)

#Part 2

mem_pattern = r"^mul\(\d{1,3},\d{1,3}\)$"
total_product_sum = 0
do_dont = 1

test = "xmul(2,4)&mul[3,7]!^don't()do()don't()_mul(5,5)+mul(32,64](mul(11,8)undo()do()?mul(8,5))"
print(parse_memory(test, mem_pattern, do_dont))

for line in data:
    print(do_dont)
    total_product_sum += parse_memory(line, mem_pattern, do_dont)

print(f"The total sum of all valid memory instructions is {total_product_sum}")

#Print Performance Time
print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)
