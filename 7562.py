from collections import deque
import sys
input = sys.stdin.readline


def bfs(start_x, start_y, end_x, end_y):
    queue = deque()
    queue.append([start_x, start_y])
    visit[start_x][start_y] = 1

    dx = [2, 2, -2, -2, 1, -1, 1, -1]
    dy = [1, -1, 1, -1, 2, 2, -2, -2]

    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            return visit[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                queue.append([nx, ny])


T = int(input())
for _ in range(T):
    l = int(input())
    visit = [[0] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(bfs(start_x, start_y, end_x, end_y))
