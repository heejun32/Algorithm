import collections


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
        
        queue = collections.deque([node])
        clones = {node.val : Node(node.val, [])}
        
        while queue:
            cur = queue.popleft()
            cur_clone = clones[cur.val]
            
            for neighbor in cur.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                    
                cur_clone.neighbors.append(clones[neighbor.val])
                
        return clones[node.val]