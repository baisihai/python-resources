# Purpose: Read a text file, process its content, and write the results to a new file.
# This example demonstrates basic file handling in Python.
def process_line(line):
    # Example processing: Convert to uppercase and strip whitespace
    return line.strip().upper()

input_file_path = 'input.txt'
output_file_path = 'output.txt'

try:
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            processed_line = process_line(line)
            outfile.write(processed_line + '\n')
    print(f"Processing complete. Check '{output_file_path}' for results.")

except FileNotFoundError:
    # Ensure you have an 'input.txt' file in the same directory as this script to test it.
    print(f"Error: The file '{input_file_path}' was not found.")    
except Exception as e:
    print(f"An error occurred: {e}")
