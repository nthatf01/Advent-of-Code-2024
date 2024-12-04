import csv
import time
import sys

#Start Performance Counter
startTime = time.perf_counter()

def read_csv_file(file_path):
    data_list = []

    try:
        with open(file_path, mode = 'r', encoding = 'utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                data_list.append(str(row)[2:-2].split("   "))

        return data_list

    except FileNoteFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

csv_file_path = 'AoC24 Day 01.csv'
data = read_csv_file(csv_file_path)

#Part 2

#Initialize the left and right lists
left_list = []
right_list = []

for line in data:
    left_list.append(int(line[0]))
    right_list.append(int(line[1]))

#Create hashmaps from the lists
left_hash = {}
right_hash = {}

for num in left_list:
    if num in left_hash:
        left_hash[num] += 1
    else:
        left_hash[num] = 1

for num in right_list:
    if num in right_hash:
        right_hash[num] += 1
    else:
        right_hash[num] = 1

#Calculate the similarity
similarity = 0

for val, frequency in left_hash.items():
    if val in right_hash:
        similarity += val * frequency * right_hash[val]
    else:
        similarity += 0

print(f"The similarity score is: {similarity}")

#Print Performance Time
print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)
