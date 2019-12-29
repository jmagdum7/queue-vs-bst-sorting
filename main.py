from random import randint
from queue_sort import sortQueue
from tree_sort import sortTree
from graph import plot
import time


def current_milli_time():
	return int(round(time.time() * 1000))


def random_dataset(size):
	"""
	Function that generates a random data set.
	It takes size as input from main
	"""
	array_input = []
	for i in range(randint(0, size)):
		array_input.append(randint(0, size))
	return array_input


def main():
	"""
	Main function that initializes size for the random data set.
	Then calls sortTree and sortQueue by passing generated random dataset as input
	function also calculates final time for both operations
	these final times are available in different lists which will be given to graph as input
	"""
	size = 2500
	all_lengths = []
	tree_time = []
	queue_time = []

	for i in range(100):
		input_list = random_dataset(size)
		all_lengths.append(len(input_list))
		start_time_tree = current_milli_time()
		tree_list = sortTree(input_list)
		end_time_tree = current_milli_time()
		final_time_tree = end_time_tree - start_time_tree
		tree_time.append(final_time_tree)
		start_time_queue = current_milli_time()
		queue_list = sortQueue(input_list)
		end_time_queue = current_milli_time()
		final_time_queue = end_time_queue - start_time_queue
		queue_time.append(final_time_queue)

	print('Dataset sizes : ' + str(all_lengths))
	print('Tree time : ' + str(tree_time))
	print('Queue time : ' + str(queue_time))
	plot(all_lengths, tree_time, queue_time)


if __name__ == '__main__':
	main()
