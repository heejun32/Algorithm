from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, rain):
    queue = deque()
    queue.append([x, y])
    visit[x][y] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if board[nx][ny] > rain:
                    visit[nx][ny] = True
                    queue.append([nx, ny])
    return None


N = int(input())
board = []
max_h = 0
for _ in range(N):
    lst = list(map(int, input().split()))
    max_h = max(max_h, max(lst))
    board.append(lst)

answer = 0
for rain in range(max_h + 1):
    visit = [[False] * N for _ in range(N)]
    count = 0
    for x in range(N):
        for y in range(N):
            if not visit[x][y] and board[x][y] > rain:
                bfs(x, y, rain)
                count += 1
    answer = max(answer, count)

print(answer)
    
