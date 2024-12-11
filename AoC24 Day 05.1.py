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

def parse_rules(unparsed_rules):
    #Initialize temporary list of rules
    rules_list = {}

    #Loop over unparsed rules
    for rule in unparsed_rules:
        
        #Split the rules into left and right parts and convert into int values
        l_num = int(rule[:2])
        r_num = int(rule[-2:])
        #print(l_num, r_num)

        #Add the left number as a key to the list if it doesn't exist
        if l_num not in rules_list:
            rules_list[l_num] = [r_num]
            
        #Otherwise update its value list
        else:
            rules_list[l_num].append(r_num)

            
    return rules_list

    

csv_file_path = 'AoC24 Day 05.csv'
data = read_csv_file(csv_file_path)
empty_row_index = data.index('')
data_rules = data[:empty_row_index]
data_pages = data[empty_row_index + 1:]
for i, page in enumerate(data_pages):
    #print(page)
    page = page.split(",")
    #print(page)
    data_pages[i] = [int(num) for num in page]
    #print(data_pages[i])

test_data = ["47|53","97|13", "97|61",
              "97|47","75|29","61|13",
              "75|53","29|13","97|29",
              "53|29","61|53","97|53",
              "61|29","47|13","75|47",
              "97|75","47|61","75|61",
              "47|29","75|13","53|13"]

test_pages = [[75,47,61,53,29],
              [97,61,53,29,13],
              [75,29,13],
              [75,97,47,61,53],
              [61,13,29],
              [97,13,75,29,47]]

test_rules = {}

test_rules = parse_rules(test_data)


#print(test_rules)
#print(test_pages)

for pages in test_pages:
    valid = True
    for i, current in enumerate(pages):
        remaining_keys = pages[i + 1:]
        #print(i, current, remaining_keys)
        for key in remaining_keys:
            if key in test_rules:
                if current in test_rules[key]:
                    #print(current, "Invalid", test_rules[key])
                    valid = False
                #else:
                    #print(current, "Valid", test_rules[key])
    #print(pages, valid)    


                  
#Part 1

rules = {}
rules = parse_rules(data_rules)

#print(rules)

mid_sum = 0
for pages in data_pages:
    valid = True
    for i, current in enumerate(pages):
        remaining_keys = pages[i + 1:]
        #print(i, current, remaining_keys)
        for key in remaining_keys:
            if key in rules:
                if current in rules[key]:
                    valid = False
    #print(pages, valid)
    if valid:
        print(pages, pages[int((len(pages)-1)/2)])
        mid_sum += pages[int((len(pages)-1)/2)]

print(mid_sum)

#Print Performance Time
print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)
