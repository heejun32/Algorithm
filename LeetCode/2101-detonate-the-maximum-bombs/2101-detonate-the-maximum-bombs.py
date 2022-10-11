class Solution:
    def dist(self, x, y):
        return sqrt((x[0]-y[0])*(x[0]-y[0]) + (x[1]-y[1])*(x[1]-y[1]))
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:        
        res = 1
        for i in range(len(bombs)):
            current_res = 1
            visited = set()
            visited.add(i)
            q = collections.deque([i])
            while q:
                node = q.popleft()
                for c in range(len(bombs)):
                    if c not in visited and self.dist(bombs[node], bombs[c]) <= bombs[node][2]:
                        q.append(c)
                        visited.add(c)
                        current_res += 1
                        
            res = max(res, current_res)
                
        return res