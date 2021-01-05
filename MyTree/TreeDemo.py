class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break
                else:
                    break

'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''

# Declaring a BinarySearchTree().
tree = BinarySearchTree()

# Assigning values to it.
arr = [int(i) for i in input().split()]
for i in arr:
    tree.insert(i)

# Calling functions.
# preOrder(tree.root)
# postOrder(tree.root)
# inOrder(tree.root)
# Height(tree.root)
# InOrder(tree.root)
