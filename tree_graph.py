import matplotlib.pyplot as plt


def plot():
	# Plotting points as a scatter plot
	all_lengths = [338, 1673, 1920, 1124, 1171, 974, 1944, 1660, 143, 703, 814, 1718, 2262, 2081, 846, 2353, 949, 614, 1547, 654, 807, 2339, 2050, 1714, 1632, 1757, 478, 1428, 2289, 860, 1503, 865, 438, 695, 1812, 1316, 1293, 1888, 2339, 1334, 608, 1142, 2407, 2168, 1427, 1462, 1669, 1849, 976, 609, 72, 350, 230, 1026, 1105, 907, 1091, 560, 2422, 2485, 2460, 484, 341, 109, 2416, 1650, 1561, 1944, 1232, 2291, 2179, 213, 1732, 2423, 1733, 2342, 159, 1165, 2475, 1710, 1480, 485, 1107, 1350, 119, 10, 2098, 1973, 2144, 699, 1902, 1632, 143, 206, 1337, 2058, 2033, 1504, 1390, 1431]
	tree_time = [1, 10, 9, 6, 5, 5, 13, 8, 1, 3, 3, 8, 12, 10, 4, 14, 5, 3, 6, 17, 3, 11, 10, 8, 9, 9, 2, 6, 12, 4, 10, 3, 1, 3, 8, 5, 6, 10, 11, 6, 2, 6, 15, 11, 6, 8, 12, 10, 3, 3, 1, 2, 1, 5, 5, 4, 4, 2, 10, 12, 21, 2, 2, 1, 12, 8, 9, 9, 5, 9, 9, 1, 14, 22, 9, 13, 1, 6, 14, 9, 7, 2, 5, 12, 0, 0, 13, 17, 13, 3, 10, 9, 0, 0, 6, 10, 12, 8, 7, 12]

	plt.scatter(tree_time, all_lengths, label="tree points", color="blue", s=30)
	
	# Naming the x axis
	plt.xlabel('Time')
	
	# Naming the y axis
	plt.ylabel('Size of Datasets')
	
	# Giving a title to my graph
	plt.title('Sorting using a Binary Search Tree')
	
	# show a legend on the plot
	plt.legend()

	plt.show()


plot()
