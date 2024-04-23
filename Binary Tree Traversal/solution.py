"""Binary Tree Traversal"""
def pre_order(node, res=None):
    """Pre-order traversal"""
    if not res:
        res = []
    if node:
        res.append(node.data)
        pre_order(node.left, res)
        pre_order(node.right, res)
    return res

def in_order(node, res=None):
    """In-order traversal"""
    if not res:
        res = []
    if node:
        res =in_order(node.left, res)
        res.append(node.data)
        res = in_order(node.right, res)
    return res

def post_order(node, res=None):
    """Post-order traversal"""
    if not res:
        res = []
    if node:
        res=post_order(node.left, res)
        res = post_order(node.right, res)
        res.append(node.data)
    return res
