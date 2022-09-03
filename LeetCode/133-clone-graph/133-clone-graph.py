"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 중복 탐색 방지
        seen = {}
        
        def clone(node):
            if not node:
                return None
            
            if node.val in seen:
                return seen[node.val]
            
            seen[node.val] = Node(node.val)
            
            for neighbor in node.neighbors:
                seen[node.val].neighbors.append(clone(neighbor))
            
            return seen[node.val]
        
        return clone(node)