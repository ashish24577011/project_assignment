import pandas as pd
import sys

# Capture the number of quantiles from command line argument
num_quantiles = int(sys.argv[1])

# Read the list of numbers from stdin and convert to a DataFrame
numbers = [float(line.strip()) for line in sys.stdin]
df = pd.DataFrame(numbers, columns=["Value"])

# Calculate quantiles and assign labels
labels = [f"q{i+1}" for i in range(num_quantiles)]
df["Quantile_Label"], bins = pd.qcut(df["Value"], q=num_quantiles, labels=labels, retbins=True)

# Assign quantile intervals based on calculated bins
df["Quantile_Interval"] = pd.cut(df["Value"], bins=bins)

# Output each value with its quantile label and interval
for _, row in df.iterrows():
    print(f"{row['Value']}\t{row['Quantile_Label']}\t{row['Quantile_Label']} {row['Quantile_Interval']}")

