"""
Report Generation Functions for Flight Operations

This module contains functions for reading, processing, and reporting on
military flight operations data. Students will implement these functions
to practice file I/O, data manipulation, and report generation.
"""

import csv
import io

def read_csv_file(filepath):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    """
    try:
        with io.open(filepath, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print (f"Error: The file at '{filepath} was not found.")
        return [] # if I put None will be type error. and could crash so it completes the code ran with an excepted same time return.
    except PermissionError:
        print (f"Permission denied when accessing '{filepath}'.")
        return []

def count_records(data_list):
    return len(data_list)


def get_unique_values(data_list, field_name):
    """Gets all unique values for a specific field in the dataset."""
    unique_vals = set()
    for values in data_list:
        if field_name in values:
            val = values[field_name]
            unique_vals.add(val)
            return sorted(list(unique_vals))
    #unique_values = {record[field_name] for record in data_list if field_name in record}
    #return sorted(list(unique_values))



def filter_by_field(data_list, field_name, field_value):
    """Filters records where a specific field matches a given value."""
    filtered_records = []
    for record in data_list:
        if record.get(field_name) == field_value:
            filtered_records.append(record)
        return filtered_records

    # TODO: Your code here
    # Hint: Use a list comprehension to filter or a loop!
    # see here for more info: https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions


def calculate_total(data_list, field_name):
    """Calculates the sum of a numeric field across all records."""
    # TODO: Your code here
    # Hint: Initialize a total variable to 0
    total = 0.0
    for record in data_list:
        total+= float(record[field_name])
    return total

    # Hint: Loop through each record and add float(record[field_name]) to total
    # Hint: Remember to convert string values to float!



def calculate_average(data_list, field_name):
    """Calculates the average value of a numeric field."""
    # TODO: Your code here
    count = count_records(data_list)  #utilizing function defined above for total length
    if count == 0:
        return 0.0

    return calculate_total(data_list, field_name) / count
    #function just above this one is using the data we inserted to find total and then dividing it by the amount of rows of data we have which is a new list called count
    # Hint: Use calculate_total() and count_records() functions functions I just made above
    # Hint: Average = total / count



def find_record_by_id(data_list, id_field, id_value):
    """Finds a specific record by its ID field."""
    # TODO: Your code here
    for record in data_list:
        if record.get[id_field] == id_value:
            return record
        else:
            return None
    # Hint: Loop through data_list
    # Hint: Return the record when record[id_field] == id_value



def join_data(primary_list, secondary_list, primary_key, foreign_key):
    """
    Joins two datasets together based on matching key fields.
    Similar to a SQL JOIN.
    """
    # TODO: Your code here
    # Hint: Create a dictionary mapping secondary_list IDs to records
    secondary_map = {}
    for record in secondary_list:
        if foreign_key in record:
            key_value = record[foreign_key]
            secondary_map[key_value] = record
    joined_list = []
    for prim_record in primary_list:
        merge_record = prim_record.copy()
        prim_key = prim_record.get(primary_key)
    # Hint: For each record in primary_list, look up the matching secondary record
        if prim_key in secondary_map:
            merge_record.update(secondary_map[prim_key])
        joined_list.append(merge_record)
    return joined_list
    # Hint: Use dict.update() to merge dictionaries
    pass


def write_report_to_file(filepath, content):
    """Writes a text report to a file."""
    # TODO: Your code here
    with io.open(filepath, 'w', encoding='utf-8') as new_file:
        new_file.write(content)
    # Hint: Use 'with open(filepath, 'w')' to open file for writing



def format_header(title):
    """Creates a formatted header for reports."""
    # TODO: Your code here
    # Hint: Use "=" * 60 to create a line of equals signs
    line = "=" * 60
    centered_title = title.center(60)
    # Hint: Use .center(60) to center the title
    return f"{line}\n{centered_title}\n{line}\n"



# Testing functions
if __name__ == '__main__':
    print("Testing report functions...")
    print("Implement functions above, then uncomment test code below")

    # # Test read_csv_file
    # pilots = read_csv_file('../data/pilots.csv')
    # print(f"Loaded {len(pilots)} pilots")
