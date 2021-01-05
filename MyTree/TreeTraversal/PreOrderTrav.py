from collections import deque
def preOrder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
def PreOrder(root):
    lis = []
    if root is None:
        return lis
    s = deque()
    s.append(root)
    while s:
        root = s.pop()
        lis.append(root.data)
        if root.right:
            s.append(root.right)
        if root.left:
            s.append(root.left)
    return lis