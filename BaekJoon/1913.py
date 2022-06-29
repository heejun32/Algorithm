N = int(input())
target = int(input())
board = [[0] * N for _ in range(N)]
dx = [1, 0, -1, 0]  # 아래 위
dy = [0, 1, 0, -1]  # 오른쪽 왼쪽
num = N ** 2
i = 0  # 방향 인덱스
x, y = 0, 0
answer = []

board[x][y] = num
while True:
    nx = x + dx[i]
    ny = y + dy[i]
    if not(0 <= nx < N) or not(0 <= ny < N) or board[nx][ny] != 0:
        i += 1
        if i == 4:  # 한바퀴 다 돌면 초기화
            i = 0
        continue
    x, y = nx, ny
    num -= 1
    board[x][y] = num
    if num == 1:
        break

# 결과 출력
for i in range(N):
    for j in range(N):
        print(board[i][j], end=' ')
    print()

for i in range(N):
    for j in range(N):
        if board[i][j] == target:
            print(i + 1, j + 1)
