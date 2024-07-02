import csv
import os
import re
import chardet
import sys

input_csv = sys.argv[1] + '/functions_list0.csv'
output_csv = 'functions_with_calls.csv'

def detect_encoding(file_path):
    """Detect the encoding of the file."""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def try_open(file_path):
    """Try to open the file with the detected encoding."""
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()

def get_called_functions(file_path, function_name, all_functions):
    """Get a set of functions called by the specified function."""
    called_functions = set()
    content = try_open(file_path)
    lines = content.splitlines()

    # Find the function definition line
    function_start = None
    for i, line in enumerate(lines):
        if re.match(r'\b{}\b'.format(re.escape(function_name)), line):
            function_start = i
            break

    if function_start is not None:
        # Search for function calls
        for line in lines[function_start:]:
            # Simple regex to match function calls
            matches = re.findall(r'\b(\w+)\s*\(', line)
            for match in matches:
                if match != function_name and match in all_functions:  # Exclude self-calls and check if in function list
                    called_functions.add(match)

    return called_functions

# Get all function names from the input CSV
all_functions = set()
with open(input_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        all_functions.add(row[0])

# Read the input CSV file and process each function
with open(input_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# Add called functions to each row
for row in rows:
    function_name = row[0]
    file_path = row[1]

    if os.path.exists(file_path):
        try:
            called_functions = get_called_functions(file_path, function_name, all_functions)
            row.append(' '.join(called_functions))  # Third column with called functions
            row.append(' '.join(called_functions))  # Fourth column with called functions
        except UnicodeDecodeError:
            row.append('')  # If the file cannot be decoded, add an empty column
            row.append('')
    else:
        row.append('')  # If the file does not exist, add an empty column
        row.append('')

# Write the results to the output CSV file
with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
