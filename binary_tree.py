"""
Define a binary tree
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "pre_order":
            return self.pre_order_print(tree.root, "")
        elif traversal_type == "in_order":
            return self.in_order_print(tree.root, "")
        elif traversal_type == "post_order":
            return self.post_order_print(tree.root, "")
        else:
            print(f"Traversal Type {traversal_type} not supported!")

    def pre_order_print(self, start, traversal):
        "Root -> Left -> Right"
        if start:
            traversal += (str(start.value)+ "-")
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal

    def in_order_print(self, start, traversal):
        "Left -> Root -> Right"
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.value)+ "-")
            traversal = self.in_order_print(start.right, traversal)
        return traversal

    def post_order_print(self, start, traversal):
        "Left -> Right -> Root"
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal += (str(start.value)+ "-")
        return traversal
#            1
#           / \
#          2   3
#          /\  / \
#         4 5  6  7
#                  \
#                   8
if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.right = Node(8)
    print(tree.print_tree("pre_order"))
    print(tree.print_tree("in_order"))
    print(tree.print_tree("post_order"))
