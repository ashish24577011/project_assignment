
library(ggplot2)


args <- commandArgs(trailingOnly = TRUE)
output_file <- args[1]   # e.g., "different_clusters.png"
x_label <- args[2]       # e.g., "Relative from center [bp]"
y_label <- args[3]       # e.g., "Enrichment over Mean"
plot_title <- args[4]    # e.g., "MNase fragment profile"

# Load the dataset
data_file <- "q2_data.tsv"  # Change the filename as needed
data <- read.table(data_file, header = FALSE, col.names = c("X", "Y", "Category"))

plot <- ggplot(data, aes(x = X, y = Y, color = Category, group = Category)) +
  geom_line(size = 1) +                # Adjust line thickness
  labs(
    title = plot_title,                # Title from command-line argument
    x = x_label,                       # x-axis label
    y = y_label                        # y-axis label
  ) +
  theme_minimal()                       # Apply a minimal theme for clarity


ggsave(output_file, plot = plot, width = 8, height = 6)

