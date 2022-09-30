from typing import List
import sys

N = int(sys.stdin.readline())
board = list()

for _ in range(N):
    lst = list(map(str, sys.stdin.readline().strip()))
    board.append(lst)


def solution(N: int, board: List[str]) -> int:
    def check():
        max_count = 0
        w_c = h_c = 1
        # 탐색
        for row in range(N):
            for col in range(N - 1):
                if board[row][col] == board[row][col + 1]:
                    w_c += 1
                    max_count = max(max_count, w_c)
                else:
                    w_c = 1
                if board[col][row] == board[col + 1][row]:
                    h_c += 1
                    max_count = max(max_count, h_c)
                else:
                    h_c = 1
            w_c = h_c = 1

        return max_count  
    
    answer = 0
    for row in range(N):
        for col in range(N - 1):
            # 가로 교환
            board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]
            answer = max(answer, check())
            board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]
            
            # 세로 교환
            board[col][row], board[col + 1][row] = board[col + 1][row], board[col][row]
            answer = max(answer, check())
            board[col][row], board[col + 1][row] = board[col + 1][row], board[col][row]
    
    return answer

print(solution(N, board))