import pandas as pd
import sys

# Define file paths via command line arguments
input_file = sys.argv[1]  # The TSV file with the pattern
output_file = sys.argv[2]  # The destination file to write the filtered lines

# Read the TSV file containing the pattern and convert it into a set
patterns = set(pd.read_csv(input_file, header=None).squeeze())

# Open the output file and write lines that contain any of the patterns
with open(output_file, 'w') as f_out:
    for line in sys.stdin:
        if any(pattern in line for pattern in patterns):
            f_out.write(line)

