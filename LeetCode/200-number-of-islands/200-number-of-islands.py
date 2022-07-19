class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or \
            i >= len(grid) or j >= len(grid[0]) or \
            grid[i][j] != "1":
                return
            
            # 방문 표시
            grid[i][j] = "0"
            
            
            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
        return count

             