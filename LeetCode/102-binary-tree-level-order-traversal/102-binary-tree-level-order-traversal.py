import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # exception
        if not root:
            return []
        
        queue = collections.deque([root])
        results = []
        while queue:
            levels = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                # 같은 레벨의 노드 저장
                levels.append(node.val)
            results.append(levels)
        
        return results