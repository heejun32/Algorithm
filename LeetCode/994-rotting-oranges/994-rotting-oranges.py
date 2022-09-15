import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Time Complexity is O(MN)
        Space Complexity is O(MN)

        '''
        
        def bfs(fo: int, ro: List[List[int]]) -> int:
            #exception
            if not fo:
                return 0
                
            time = -1
            while ro:
                for _ in range(len(ro)):
                    x, y = ro.popleft()
                    for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                            fo -= 1
                            grid[dx][dy] = 2
                            ro.append([dx, dy])
                time += 1
            return time if not fo else -1
        
        m, n = len(grid), len(grid[0])
        fo = 0
        ro = collections.deque()
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    fo += 1
                if grid[x][y] == 2:
                    ro.append([x, y])
        
        return bfs(fo, ro)