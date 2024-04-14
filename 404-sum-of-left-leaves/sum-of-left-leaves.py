# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Helper function to recursively traverse the tree
        def traverse(node, is_left):
            if not node:
                return 0
            # If the node is a leaf and is a left child, add its value to the sum
            if not node.left and not node.right and is_left:
                return node.val
            # Recursively traverse the left and right subtrees
            return traverse(node.left, True) + traverse(node.right, False)
        
        # Start the traversal from the root node
        return traverse(root, False)
