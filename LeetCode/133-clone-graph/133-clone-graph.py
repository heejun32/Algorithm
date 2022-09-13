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
        clone = {node.val: Node(node.val)}
        
        while queue:
            cur_node = queue.popleft()
            cur_clone = clone[cur_node.val]
            
            for neighbor in cur_node.neighbors:
                if neighbor.val not in clone:
                    clone[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                
                cur_clone.neighbors.append(clone[neighbor.val])
                
        return clone[node.val]
