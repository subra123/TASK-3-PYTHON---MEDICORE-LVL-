import re
import csv

# Open the input file
with open('onelinefile.txt', 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Use a regular expression to split the contents of the file into groups
groups = re.findall(r'(\d+)(\w+)(\d+\.\d+)(\w+)', contents)

# Open the output file
with open('Filename2.csv', 'w') as file:
    # Write each group as a line in the output file
    for group in groups:
        file.write(",".join(group) + "\n")