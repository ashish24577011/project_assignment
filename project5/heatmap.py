import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("new_data.tsv", delimiter="\t")


plt.figure(figsize=(3, 10),facecolor='lightgray')  # Adjust the figure size as needed for better visualization.


plt.imshow(data, cmap='hot', interpolation='nearest', aspect='auto')


plt.colorbar(orientation='vertical')

plt.title("CTCF ChIP Peaks with Motif")
plt.xlabel("MNase Fragment Profile")
plt.ylabel("CTCF ChIP Peaks with Motif")


plt.xticks([0, 2000], [0, 2000])  # x-axis ticks and labels
plt.yticks([0, 20000, 40000, 60000, 80000, 100000], [0, 20000, 40000, 60000, 80000, 100000])  # y-axis ticks and labels


plt.gca().invert_yaxis()
plt.savefig("heatmap.png", dpi=300, bbox_inches="tight")

