"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # exception
        if not node:
            return node
        
        clones = dict()
        
        def dfs(node):
            if node not in clones:
                clones[node.val] = Node(node.val, [])
                
                for neighbor in node.neighbors:
                    if neighbor.val not in clones:
                        dfs(neighbor)
                    clones[node.val].neighbors.append(clones[neighbor.val])
            
            return None
        
        dfs(node)
        return clones[node.val]
            