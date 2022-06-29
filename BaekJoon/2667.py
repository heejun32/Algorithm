from collections import deque
import sys
input = sys.stdin.readline

# 입력값 받기
N = int(input())
answer = []
MAP = [list(map(int, input().strip())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]


# bfs 함수 선언
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visit[x][y] = True
    count = 1
    while queue:
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visit[nx][ny] and MAP[nx][ny] == 1:
                    queue.append([nx, ny])
                    visit[nx][ny] = True
                    count += 1
    return count


# bfs 탐색 시작
for x in range(N):
    for y in range(N):
        if not visit[x][y] and MAP[x][y] != 0:
            answer.append(bfs(x, y))

# 정답 출력
answer.sort()
print(len(answer))
for a in answer:
    print(a)
