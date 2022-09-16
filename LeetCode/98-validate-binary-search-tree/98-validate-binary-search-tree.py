# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_value = float('-inf'), max_value = float('inf') ) -> bool:
        if not root:
            return True
        
        if root.val <= min_value or root.val >= max_value:
            return False
        
        return self.isValidBST(root.left, min_value, root.val) and self.isValidBST(root.right, root.val, max_value)