import sys
input = sys.stdin.readline

N = int(input())
PAPER = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0, 0]


# 1사분면 ~ 9사분면 분할 탐색
def travel(x, y, N):
    check = PAPER[x][y]
    for row in range(x, x+N):
        for col in range(y, y+N):
            if check != PAPER[row][col]:
                # 1사분면
                travel(x, y, N // 3)
                # 2사분면
                travel(x, y + N // 3, N // 3)
                # 3사분면
                travel(x, y + 2 * (N // 3), N // 3)
                # 4사분면
                travel(x + N // 3, y, N // 3)
                # 5사분면
                travel(x + N // 3, y + N // 3, N // 3)
                # 6사분면
                travel(x + N // 3, y + 2 * (N // 3), N // 3)
                # 7시분면
                travel(x + 2 * (N // 3), y, N // 3)
                # 8사분면
                travel(x + 2 * (N // 3), y + N // 3, N // 3)
                # 9사분면
                travel(x + 2 * (N // 3), y + 2 * (N // 3), N // 3)
                return None

    if check == -1:
        answer[0] += 1
    elif check == 0:
        answer[1] += 1
    else:
        answer[2] += 1

    return None


travel(0, 0, N)
for i in range(3):
    print(answer[i])
