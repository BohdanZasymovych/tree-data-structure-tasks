from queue import Queue

def tree_by_levels(node):
    if node is None:
        return []
    
    visit_queue = Queue()
    visit_queue.put(node)
    visited = []
    
    while not visit_queue.empty():
        cur_node = visit_queue.get()
        visited.append(cur_node.value)
        
        if cur_node.left is not None:
            visit_queue.put(cur_node.left)
        
        if cur_node.right is not None:
            visit_queue.put(cur_node.right)
    
    return visited
