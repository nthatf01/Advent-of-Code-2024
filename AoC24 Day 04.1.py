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

def add_vertical_padding(word_search):
    for i in range(len(word_search)):
        word_search[i] = "..." + word_search[i] + "..."
    return word_search

def add_horizontal_padding(word_search):
    padded_row = ""
    for i in range(len(word_search[0])):
        padded_row += "."
    for i in range(0, 3):
        word_search.insert(0, padded_row)
        word_search.append(padded_row)

    return word_search

def count_xmas(word_search):
    x_check = [""]

    for y in range(3, len(word_search) - 3):
        for x in range(3, len(word_search[y]) - 3):
            if word_search[y][x] == "X":
                #North
                x_check.append(word_search[y][x] + word_search[y-1][x] + word_search[y-2][x] + word_search[y-3][x])
                #Northeast
                x_check.append(word_search[y][x] + word_search[y-1][x+1] + word_search[y-2][x+2] + word_search[y-3][x+3])
                #East
                x_check.append(word_search[y][x] + word_search[y][x+1] + word_search[y][x+2] + word_search[y][x+3])
                #Southeast
                x_check.append(word_search[y][x] + word_search[y+1][x+1] + word_search[y+2][x+2] + word_search[y+3][x+3])
                #South
                x_check.append(word_search[y][x] + word_search[y+1][x] + word_search[y+2][x] + word_search[y+3][x])
                #Southwest
                x_check.append(word_search[y][x] + word_search[y+1][x-1] + word_search[y+2][x-2] + word_search[y+3][x-3])
                #West
                x_check.append(word_search[y][x] + word_search[y][x-1] + word_search[y][x-2] + word_search[y][x-3])
                #Northwest
                x_check.append(word_search[y][x] + word_search[y-1][x-1] + word_search[y-2][x-2] + word_search[y-3][x-3])
    
    return x_check.count("XMAS")

csv_file_path = 'AoC24 Day 04.csv'
data = read_csv_file(csv_file_path)

test_data = ["MMMSXXMASM","MSAMXMSMSA","AMXSXMAAMM","MSAMASMSMX","XMASAMXAMM","XXAMMXXAMA","SMSMSASXSS","SAXAMASAAA","MAMMMXMMMM","MXMXAXMASX"]

#Part 1

test_data = add_vertical_padding(test_data)
test_data = add_horizontal_padding(test_data)

data = add_vertical_padding(data)
data = add_horizontal_padding(data)

#for line in test_data:
#    print(line)

print(count_xmas(test_data))
print(f"The number of XMAS in the word search: {count_xmas(data)}")

#Print Performance Time
print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)
