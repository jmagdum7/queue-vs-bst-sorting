import unittest
from tree_sort import sortTree
from timeit import default_timer as timer
import random


class TreeSortTest(unittest.TestCase):

    def setUp(self):
        self.tree = [random.randint(1, 4000) for _ in range(1, 979)]

    def test_tree_already_sorted(self):
        copy_tree = self.tree
        self.tree.sort()
        copy_tree.sort()
        self.tree = sortTree(self.tree)
        self.assertListEqual(copy_tree, self.tree)

    def test_tree_reverse_sorted(self):
        copy_tree = self.tree[:]
        copy_tree.sort()
        self.tree.sort(reverse=True)
        self.tree = sortTree(self.tree)
        self.assertListEqual(copy_tree, self.tree)

    def test_tree_sort(self):
        copy_tree = self.tree
        sortTree(self.tree)
        copy_tree.sort()
        self.assertListEqual(copy_tree, self.tree)


if __name__ == '__main__':
    unittest.main()
