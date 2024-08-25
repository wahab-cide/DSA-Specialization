"""
A tree is:
- Empty, or
- A node with:
--- a key, amd
--- a list of child trees

Root: top node in the tree.
Leaf: Node with no children
Level: 1 + number of edges between
a root and the node
Height: length of the longest path 
from the root to a leaf.
Forest: Collection of trees

Binary Tree:(each node has at most two children)
-key
-left
-right
-(optional) parent

"""


#1st Implementation
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def Insert(self, value):
        if self.root is None:
            self.root = Node(value)  # If the tree is empty, set the root node.
        else:
            self.insert(value, self.root)  # Start the recursive insertion.

    def insert(self, value, current_node):
        if value < current_node.data:
            if current_node.left is None:
                current_node.left = Node(value)  # Insert here if the left child is empty.
            else:
                self.insert(value, current_node.left)  # Recurse on the left child.
        elif value > current_node.data:
            if current_node.right is None:
                current_node.right = Node(value)  # Insert here if the right child is empty.
            else:
                self.insert(value, current_node.right)  # Recurse on the right child.


#2nd Implementation
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:

            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

#inorder traversal

def inorder(self, root):
    res = []
    if root:  # Checks if root is not None
        res = self.inorder(root.left)  # Recursively traverses the left subtree
        res.append(root.data)  # Appends the data of the current node
        res = res + self.inorder(root.right)  # Recursively traverses the right subtree
    return res  # Returns the result list

def preorder(self, root):
    res = []
    if root:
        res.append(root.data)
        res = res + preorder(root.left)
        res = res + preorder(root.right)
    return res

def postorder(self, root):
    if root:
        res = self.postorder(root.left)
        res = res + self.postorder(root.right)
        res.append(root.data)
    return res