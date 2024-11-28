import pandas as pd
import sys


num_quantiles = int(sys.argv[1])


numbers = [float(line.strip()) for line in sys.stdin]
df = pd.DataFrame(numbers, columns=["Value"])


labels = [f"q{i+1}" for i in range(num_quantiles)]
df["Quantile_Label"], bins = pd.qcut(df["Value"], q=num_quantiles, labels=labels, retbins=True)


df["Quantile_Interval"] = pd.cut(df["Value"], bins=bins)


for _, row in df.iterrows():
    print(f"{row['Value']}\t{row['Quantile_Label']}\t{row['Quantile_Label']} {row['Quantile_Interval']}")

