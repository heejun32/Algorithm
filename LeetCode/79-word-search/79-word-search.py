import collections


class Solution:
    '''
    Time Complexity is O(MN3^L)
    Space Complexity is O(1)
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, k):
            # 종료 조건: 탐색 범위를 넘은 경우, word 글자수보다 더 탐색한 경우, 이미 방문한 지점의 경우, 탐색하는 문자가 다른 경우
            if x < 0 or x >= m or y < 0 or y >= n or k >= len(word) or board[x][y] == '#' or word[k] != board[x][y]:
                return False

            if k == len(word) - 1:
                return True
            
            mark = board[x][y]
            board[x][y] = '#'
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if dfs(dx, dy, k + 1):
                    return True
            board[x][y] = mark
            return False
        
        m, n = len(board), len(board[0])
        
        # Exception
        word_dict = collections.Counter(word)
        board_dict = collections.Counter()
        for row in range(m):
            for col in range(n):
                board_dict[board[row][col]] += 1
        
        for char in word_dict:
            if char not in board_dict or board_dict[char] < word_dict[char]:
                return False
        
        # 탐색 시작
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True
                    
        return False