class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, k):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            
            if board[x][y] == '#':
                return False
            
            if board[x][y] != word[k]:
                return False
            
            if k == w:
                return True
            
            tmp = board[x][y]
            board[x][y] = '#'
            k += 1
            
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if dfs(x + dx, y + dy, k):
                    return True
            
            board[x][y] = tmp
            return False
        
        m, n, w = len(board), len(board[0]), len(word) - 1
        visited = set()
        
        for row in range(m):
            for col in range(n):
                if dfs(row, col, 0):
                    return True
                            
        return False