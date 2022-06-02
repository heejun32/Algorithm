from collections import deque
import sys
input = sys.stdin.readline

# 변수 선언
N = int(input())
RGB = [list(map(str, input().strip())) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]
answer = [0, 0]
queue = deque()


# bfs 선언
def bfs(x, y):
    queue.append([x, y])
    visit[x][y] = True
    color = RGB[x][y]

    while queue:
        x, y = queue.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 색깔이 같고, 방문하지 않았다면 다음 탐색 대상
                if color == RGB[nx][ny] and not visit[nx][ny]:
                    queue.append([nx, ny])
                    visit[nx][ny] = True
    return None


# 탐색 시작: 일반인일때
for x in range(N):
    for y in range(N):
        if not visit[x][y]:
            bfs(x, y)
            answer[0] += 1

# 적녹색약은 빨강과 그린을 구별할 수 없다. 따라서 R 또는 G를 둘 중 하나로 통일한다.
for x in range(N):
    for y in range(N):
        if RGB[x][y] == 'G':
            RGB[x][y] = 'R'

# 재탐색해야 되니 방문 기록을 초기화해주자
visit = [[False for _ in range(N)] for _ in range(N)]

# 탐색 시작: 적녹색약일때
for x in range(N):
    for y in range(N):
        if not visit[x][y]:
            bfs(x, y)
            answer[1] += 1

# 정답 출력
for i in range(2):
    print(answer[i], end=" ")
