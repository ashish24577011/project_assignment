import matplotlib.pyplot as plt
import numpy as np

#Loading data from the TSV file into a NumPy array.
data = np.loadtxt("new_data.tsv", delimiter="\t")

#Setting up the figure dimensions.
plt.figure(figsize=(3, 10),facecolor='lightgray')  # Adjust the figure size as needed for better visualization.

#Creating the heatmap using the data, with a color map 'hot' and nearest interpolation.
plt.imshow(data, cmap='hot', interpolation='nearest', aspect='auto')

#Adding a color bar on the right to show the scale of intensity values.
plt.colorbar(orientation='vertical')

#Setting the plot title and axis labels for clarity.
plt.title("CTCF ChIP Peaks with Motif")
plt.xlabel("MNase Fragment Profile")
plt.ylabel("CTCF ChIP Peaks with Motif")

#Customizing x-axis and y-axis ticks to fit the data's range.
plt.xticks([0, 2000], [0, 2000])  # x-axis ticks and labels
plt.yticks([0, 20000, 40000, 60000, 80000, 100000], [0, 20000, 40000, 60000, 80000, 100000])  # y-axis ticks and labels

#Inverting the y-axis to match the preferred orientation.
plt.gca().invert_yaxis()
plt.savefig("heatmap.png", dpi=300, bbox_inches="tight")

