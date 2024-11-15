# Load required libraries
library(dplyr)
library(readr)
library(purrr)

# Capture command-line arguments
args <- commandArgs(trailingOnly = TRUE)
input_file <- args[1]   # File containing paths to the data files
output_file <- args[2]  # File to save the merged data

# Read the list of file paths from the input file
file_paths <- read_tsv(input_file, col_names = FALSE, show_col_types = FALSE)$X1

# Process each file: Read data, rename columns, and store in a list
data_frames <- file_paths %>%
  map(~ {
    data <- read_tsv(.x, col_names = FALSE, show_col_types = FALSE)
    colnames(data) <- as.character(seq_len(ncol(data)))  # Rename columns to "1", "2", ...
    data
  })

# Merge all data frames by the first column (column "1")
merged_data <- reduce(data_frames, ~ inner_join(.x, .y, by = "1"))

# Write the merged data to the output file
write_tsv(merged_data, output_file)

