import unittest
from queue_sort import sortQueue
from timeit import default_timer as timer
import random


class QueueSortTest(unittest.TestCase):

    def setUp(self):
        self.queue = [random.randint(1, 4000) for _ in range(1, 2500)]

    def test_queue_already_sorted(self):
        self.queue.sort()
        start = timer()
        sortQueue(self.queue)
        end = timer()
        self.assertListEqual(copy_queue, self.queue)

    def test_queue_reverse_sorted(self):
        self.queue.sort(reverse=True)
        start = timer()
        sortQueue(self.queue)
        end = timer()
        self.assertListEqual(copy_queue, self.queue)

    def test_queue_sort(self):
        copy_queue = self.queue
        sortQueue(self.queue)
        copy_queue.sort()
        self.assertListEqual(copy_queue, self.queue)


if __name__ == '__main__':
    unittest.main()
