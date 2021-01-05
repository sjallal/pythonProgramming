def Height(root):
    if root is None:
        return -1
    return max(Height(root.left), Height(root.right)) + 1