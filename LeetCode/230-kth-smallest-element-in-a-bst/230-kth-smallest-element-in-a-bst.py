# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.array = list()
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)
            self.array.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return self.array[k - 1]