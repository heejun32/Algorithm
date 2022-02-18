from collections import deque
import sys
input = sys.stdin.readline
queue = deque()
graph = []
M, N, H = map(int,input().split())

for h in range(H):
    temp = []
    for n in range(N):
        temp.append(list(map(int, input().split())))
        for m in range(M):
            if temp[n][m] == 1:
                queue.append([h, m, n])
    graph.append(temp)


def bfs(z, x, y):
    dx = [-1,1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and graph[nx][ny][nz] == 0:
            queue.append([nx,ny,nz])
            graph[nx,ny,nz] = graph[x][y][z]+1

while queue:
    z, x, y = queue.popleft()
    bfs(z, x, y)

days = 0
flag = 0
for h in graph:
    for n in h:
        for m in m:
            if m == 0:
                flag = 1
                break
        days = max(days,max(m))
print(days-1)