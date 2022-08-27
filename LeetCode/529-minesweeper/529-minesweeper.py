class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(x, y):
            if board[x][y] != "E":
                return None
        
            # search near mine        
            count = 0
            for dx, dy in((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)):
                if 0 <= dx <= len(board) - 1 and 0 <= dy <= len(board[0]) - 1 and board[dx][dy] == "M":
                    count += 1

            if count:
                board[x][y] = str(count)
            else:
                board[x][y] = "B"
                for dx, dy in((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)):
                    if 0 <= dx <= len(board) - 1 and 0 <= dy <= len(board[0]) - 1 and board[dx][dy] == "E":
                        dfs(dx, dy)
            
            return None
        
        # exception
        x, y = click[0], click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        
        dfs(x, y)
        return board