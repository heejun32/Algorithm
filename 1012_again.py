from collections import deque
import sys

def traversal(board, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append([x, y])
    board[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            m_x = x + dx[i]
            m_y = y + dy[i]

            if m_x < 0 or m_x > len(board) - 1 or m_y < 0 or m_y > len(board[0]) - 1:
                continue
            if board[m_x][m_y] == 1:
                board[m_x][m_y] = 0
                queue.append([m_x, m_y])
    return 0

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M, N, l = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(l):
        x, y = map(int, input().split())
        board[x][y] = 1

    bugs = 0
    for x in range(M):
        for y in range(N):
            if board[x][y] == 1:
                traversal(board, x, y)
                bugs += 1

    print(bugs)