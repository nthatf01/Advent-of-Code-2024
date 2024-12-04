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

#Part 1

#Initialize the left and right lists
left_list = []
right_list = []

for line in data:
    left_list.append(int(line[0]))
    right_list.append(int(line[1]))

#Sort the lists
left_list.sort()
right_list.sort()

#Calculate the distance
total_distance = 0
for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

print(f"The total distance is: {total_distance}")

#Print Performance Time
print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)
