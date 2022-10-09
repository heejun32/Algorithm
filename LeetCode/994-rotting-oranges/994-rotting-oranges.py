import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(rotten_oranges, fresh_oranges):
            time = 0
            
            # bfs
            while rotten_oranges:
                
                # search the same level during 1 time
                time += 1
                for _ in range(len(rotten_oranges)):                
                    x, y = rotten_oranges.popleft()
                    
                    # dx, dy must be in grid and fresh
                    for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                            grid[dx][dy] = 2
                            fresh_oranges -= 1
                            rotten_oranges.append((dx, dy))
            
            if fresh_oranges:
                return -1
            return time - 1
            
        
        m, n = len(grid), len(grid[0])
        rotten_oranges = collections.deque()
        fresh_oranges = 0
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    rotten_oranges.append((x, y))
                if grid[x][y] == 1:
                    fresh_oranges += 1
        
        # Exception
        if not fresh_oranges:
            return 0
        
        return bfs(rotten_oranges, fresh_oranges)
        