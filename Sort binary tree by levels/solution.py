"""Sort binary tree by levels"""
from collections import deque
def tree_by_levels(node):
    """tree by levels"""
    result = []
    queue = deque([node]) if node else None

    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result
