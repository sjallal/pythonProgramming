from collections import deque
def levelOrder(root):
    if root is None:
        return
    s = deque()
    r = root
    s.append(r)
    while s:
        r = s.popleft()
        print(r.info, end=" ")
        if r.left:
            s.append(r.left)
        if r.right:
            s.append(r.right)