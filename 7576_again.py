from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

def traversal():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x < 0 or new_x > N - 1 or new_y < 0 or new_y > M - 1:
                continue
            if BOX[new_x][new_y] == -1:
                continue
            if BOX[new_x][new_y] == 0:
                BOX[new_x][new_y] = BOX[x][y] + 1
                queue.append([new_x, new_y])
    return 0

M, N = map(int, input().split())
BOX = [[] for _ in range(N)]
for n in range(N):
    BOX[n] = list(map(int, input().split()))

    for m in range(M):
        if BOX[n][m] == 1:
            queue.append([n, m])

traversal()
flag = 0
days = 0
for n in BOX:
    for m in n:
        if m == 0:
            flag = 1
    days = max(days, max(n))

if flag > 0:
    print(-1)
else:
    print(days - 1)
