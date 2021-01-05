def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)

from collections import deque

def InOrder(root):
    if root is None:
        return
    r = root
    s = deque()
    while s:
        pass
