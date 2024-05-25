from math import comb as c
import os

# Define function to check if output matches the content of output files
def check_output(input_num, output_file):
    Num = 0
    n = 3
    last_valid_num = 0

    while Num < input_num:
        Sum = 0
        for r in range(0, 4):
            Sum += c(n, r)
        n += 1
        Num = Sum
        if Num < input_num:
            last_valid_num = Num

    if last_valid_num > 0:
        # Open the output file and compare its content with the computed output
        with open(output_file, 'r') as file:
            expected_output = int(file.read())
        return last_valid_num == expected_output

# Directory paths
input_folder = "inputs"
output_folder = "outputs"

# Iterate through input files
for i in range(1, 9):
    input_file = os.path.join(input_folder, f"input{i}.txt")
    output_file = os.path.join(output_folder, f"output{i}.txt")

    # Read input from file
    with open(input_file, 'r') as file:
        input_num = int(file.read())

    # Execute the code and compare output with content of output files
    if os.path.exists(output_file):
        match = check_output(input_num, output_file)
        print(match)
    else:
        print("False")  # If output file doesn't exist, it's automatically False
