from itertools import permutations
import os

def is_diagonally_dominant(matrix):
    size = int(len(matrix) ** 0.5)
    for i in range(size):
        diagonal_element = matrix[i*size + i]
        row_sum = sum(abs(matrix[i*size + j]) for j in range(size) if j != i)
        if abs(diagonal_element) <= row_sum:
            return False
    return True

def count_diagonally_dominant_permutations(elements):
    element_permutations = set(permutations(elements))
    count = 0
    for perm in element_permutations:
        if is_diagonally_dominant(perm):
            count += 1
    return count

# Directory paths
input_folder = "inputs"
output_folder = "outputs"

# Define function to check if output matches the content of output files
def check_output(elements, output_file):
    result = count_diagonally_dominant_permutations(elements)
    # Open the output file and compare its content with the computed output
    with open(output_file, 'r') as file:
        expected_output = int(file.read())
    return result == expected_output

# Iterate through input files
for i in range(1, 13):
    input_file = os.path.join(input_folder, f"input{i}.txt")
    output_file = os.path.join(output_folder, f"output{i}.txt")

    # Read input from file
    with open(input_file, 'r') as file:
        elements_str = file.read()
    elements = tuple(map(int, elements_str.split()))

    # Execute the code and compare output with content of output files
    if os.path.exists(output_file):
        match = check_output(elements, output_file)
        print(match)
    else:
        print("False")  # If output file doesn't exist, it's automatically False
