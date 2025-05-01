# Pre-order traversal
def pre_order(node, visited=None):
    if node is None:
        return []

    if visited is None:
        visited = []

    visited.append(node.data)

    if node.left is not None:
        pre_order(node.left, visited)
        
    if node.right is not None:
        pre_order(node.right, visited)

    return visited

# In-order traversal
def in_order(node, visited=None):
    if node is None:
        return []

    if visited is None:
        visited = []


    if node.left is not None:
        in_order(node.left, visited)

    visited.append(node.data)
        
    if node.right is not None:
        in_order(node.right, visited)

    return visited

# Post-order traversal
def post_order(node, visited=None):
    if node is None:
        return []

    if visited is None:
        visited = []

    if node.left is not None:
        post_order(node.left, visited)
        
    if node.right is not None:
        post_order(node.right, visited)

    visited.append(node.data)

    return visited
