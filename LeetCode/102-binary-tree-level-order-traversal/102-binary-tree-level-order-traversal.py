import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([root])
        order = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:  
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)
            
            if level:
                order.append(level)
            
        return order