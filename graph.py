import matplotlib.pyplot as plt


def plot(all_lengths, tree_time, queue_time):
	# Plotting points as a Scatter Plot
	plt.scatter(tree_time, all_lengths, label="tree points", color="blue", s=30)
	plt.scatter(queue_time, all_lengths, label="queue points", color="red", s=30)
	
	# Naming the X-Axis
	plt.xlabel('Time')
	
	# Naming the Y-Axis
	plt.ylabel('Size of Data sets')
	
	# Giving a title to the graph
	plt.title('Sorting using a Queue vs Sorting using a Binary Search Tree')
	
	# Show a legend on the plot
	plt.legend()

	plt.show()
