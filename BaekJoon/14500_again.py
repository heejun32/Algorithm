import sys
input = sys.stdin.readline

# 초기 변수 선언
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = 0

# 입력값 처리
N, M = map(int, input().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]


# 백트랙킹 정의
def dfs(x, y, temp, count):
    # 종료 조건
    global answer
    if count == 4:
        answer = max(answer, temp)
        return

    for i in range(4):
        nx = x + move[i][0]
        ny = y + move[i][1]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, temp + paper[nx][ny], count + 1)
            visited[nx][ny] = False


def t1(x, y):
    global answer
    for i in range(4):
        temp = paper[x][y]
        for j in range(3):
            t = (i + j) % 4
            nx = x + move[t][0]
            ny = y + move[t][1]

            if not (0 <= nx < N and 0 <= ny < M):
                temp = 0
                break
            temp += paper[nx][ny]
        answer = max(answer, temp)


for x in range(N):
    for y in range(M):
        visited[x][y] = True
        dfs(x, y, paper[x][y], 1)
        visited[x][y] = False
        t1(x, y)

print(answer)

# 참고사이트 :https://cijbest.tistory.com/87
