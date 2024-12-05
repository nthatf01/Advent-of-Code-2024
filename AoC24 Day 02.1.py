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
                data_list.append(str(row)[2:-2].split(" "))

        return data_list

    except FileNoteFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def check_if_safe(report):
    #Check if the report is sorted in ascending order and that 1 <= level <= 3
    is_safe_asc = all(
        (report[i] <= report[i + 1]) and
        (abs(report[i + 1] - report[i]) >= 1) and
        (abs(report[i + 1] - report[i]) <= 3)
        for i in range(len(report) - 1))
    #Check if the report is sorted in descending order and that 1 <= level <= 3
    is_safe_desc = all(
        (report[i] >= report[i + 1]) and
        (abs(report[i + 1] - report[i]) >= 1) and
        (abs(report[i + 1] - report[i]) <= 3)
        for i in range(len(report) - 1))
    if is_safe_asc or is_safe_desc:
        is_safe = True
    else:
        is_safe = False
    return is_safe

csv_file_path = 'AoC24 Day 02.csv'
data = read_csv_file(csv_file_path)

#Part 1
total_safe_reports = 0

for line in data:
    level = [int(str_num) for str_num in line]
    if check_if_safe(level) == True:
        total_safe_reports += 1
    
print(f"The total number of safe reports is: {total_safe_reports}")

#Print Performance Time
print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)
