from collections import deque
import sys

# 초기 변수 설정
input = sys.stdin.readline
queue = deque()
graph = []

# 입력값 처리
M, N, H = map(int, input().split())

for h in range(H):
    temp = []
    
    for n in range(N):
        temp.append(list(map(int, input().split())))
        for m in range(M):
            if temp[n][m] == 1:
                queue.append([h, n, m])
    graph.append(temp)


# bfs 구현
dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

while queue:
    z, y, x = queue.popleft()

    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        if nz > -1 and nz < H and ny > -1 and ny < N and nx > -1 and nx < M:
            if graph[nz][ny][nx] == 0:      # 안 익은 토마토가 있을때
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append([nz, ny, nx])  # 새롭게 익은 토마토의 위치를 저장

# 정답 확인
flag = 0
answer = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 0:
                flag = 1
                break
        answer = max(answer, max(graph[h][n]))

if flag == 1:
    print(-1)
elif answer == 1:
    print(0)
else:
    print(answer - 1)