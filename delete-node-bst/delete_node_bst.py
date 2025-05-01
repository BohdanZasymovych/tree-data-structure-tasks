# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_node(self, key: int, root, prev=None):
        if root is None:
            raise KeyError
        
        if root.val == key:
            return root, prev
        
        if root.val > key:
            root, prev = self.find_node(key, root.left, root)
        
        else:
            root, prev = self.find_node(key, root.right, root)
        
        return root, prev
    
    def find_min_node(self, root, prev):
        if root.left is None:
            return root, prev
        
        root, prev = self.find_min_node(root.left, root)

        return root, prev

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None or (root.left is None and root.right is None and root.val == key):
            return None

        try:
            node, prev = self.find_node(key, root)
            a = -1 if prev is None else prev.val
            print(node.val, a)
        except KeyError:
            return root
            
        if node.left is None and node.right is None:
            if node.val < prev.val:
                prev.left = None
            else:
                prev.right = None
        
        elif node.left is None:
            if prev is None:
                return node.right
            if node.val < prev.val:
                prev.left = node.right
            else:
                prev.right = node.right
        
        elif node.right is None:
            if prev is None:
                return node.left
            if node.val < prev.val:
                prev.left = node.left
            else:
                prev.right = node.left

        else:
            min_right_node, prev_min_node = self.find_min_node(node.right, node)
            print(min_right_node.val, prev_min_node.val)
            node.val = min_right_node.val

            if min_right_node.val < prev_min_node.val:
                prev_min_node.left = min_right_node.right
            else:
                prev_min_node.right = min_right_node.right
        
        return root
