def minIndex(queue, sorted_index):
	min_index = -1
	min_val = float('inf')
	n = len(queue)
	for i in range(n):
		curr = queue[0]
		queue.pop(0)
		if curr <= min_val and i <= sorted_index:
			min_index = i
			min_val = curr
		queue.append(curr)
	return min_index


def insertMinToRear(queue, min_index):
	min_val = None
	n = len(queue)
	for i in range(n):
		curr = queue[0]
		queue.pop(0)
		if i != min_index:
			queue.append(curr)
		else:
			min_val = curr
	queue.append(min_val)


def sortQueue(queue):
	n = len(queue)
	for i in range(1, n + 1):
		min_index = minIndex(queue, n - i)
		insertMinToRear(queue, min_index)
	return queue
