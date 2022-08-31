import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
                                
        m, n = len(mat), len(mat[0])
        queue, seen = collections.deque(), set()
    
        for x in range(m):
            for y in range(n):
                if mat[x][y] == 0:
                    queue.append((x, y))
                    seen.add((x, y))
        
        dist = 1
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen:
                        mat[nx][ny] = dist
                        queue.append((nx, ny))
                        seen.add((nx, ny))
                                    
            dist += 1
        return mat