class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, node):
        if self.val > node.val:
            if not self.left:
                self.left = node
            else:
                self.left.insert(node)
        elif self.val <= node.val:
            if not self.right:
                self.right = node
            else:
                self.right.insert(node)

    def inorder(self, inorder_list):
        if self.left:
            self.left.inorder(inorder_list)
        inorder_list.append(self.val)
        if self.right:
            self.right.inorder(inorder_list)
        return inorder_list


class BSTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        inorder_list = []
        if self.root:
            inorder_list = self.root.inorder(inorder_list)
        return inorder_list

    def add(self, val):
        new_node = BSTNode(val)
        if not self.root:
            self.root = new_node
        else:
            self.root.insert(new_node)


def sortTree(input_list):
    tree = BSTree()
    for val in input_list:
        tree.add(val)
    return tree.inorder()
