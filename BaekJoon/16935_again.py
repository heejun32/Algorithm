import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
R_lst = list(map(int, input().split()))

for i in range(R):
    N = len(board)
    M = len(board[0])

    # 1번 연산
    if R_lst[i] == 1:
        board = board[::-1]
    # 2번 연산
    if R_lst[i] == 2:
        for row in range(N):
            for col in range(M // 2):
                temp = board[row][col]
                board[row][col] = board[row][M - col - 1]
                board[row][M - col - 1] = temp
    # 3번 연산
    if R_lst[i] == 3:
        temp = [[0] * N for _ in range(M)]
        for row in range(M):
            for col in range(N):
                temp[row][col] = board[N - 1 - col][row]
        board = temp
    # 4번 연산
    if R_lst[i] == 4:
        temp = [[0] * N for _ in range(M)]
        for row in range(M):
            for col in range(N):
                temp[row][col] = board[col][M - 1 - row]
        board = temp
    # 5번 연산
    if R_lst[i] == 5:
        temp = [[0] * M for _ in range(N)]
        # 1 -> 2
        for row in range(N // 2):
            for col in range(M // 2):
                temp[row][col + M // 2] = board[row][col]
        # 2 -> 3
        for row in range(N // 2):
            for col in range(M // 2, M):
                temp[row + N // 2][col] = board[row][col]
        # 3 -> 4
        for row in range(N // 2, N):
            for col in range(M // 2, M):
                temp[row][col - M // 2] = board[row][col]
        # 4 -> 1
        for row in range(N // 2, N):
            for col in range(M // 2):
                temp[row - N // 2][col] = board[row][col]
        board = temp
    # 6번 연산
    if R_lst[i] == 6:
        temp = [[0] * M for _ in range(N)]
        # 1 -> 4
        for row in range(N // 2):
            for col in range(M // 2):
                temp[row + N // 2][col] = board[row][col]
        # 2 -> 1
        for row in range(N // 2):
            for col in range(M // 2, M):
                temp[row][col - M // 2] = board[row][col]
        # 3 -> 2
        for row in range(N // 2, N):
            for col in range(M // 2, M):
                temp[row - N // 2][col] = board[row][col]
        # 4 -> 3
        for row in range(N // 2, N):
            for col in range(M // 2):
                temp[row][col + M // 2] = board[row][col]
        board = temp


# 결과 출력
for row in range(len(board)):
    for col in range(len(board[row])):
        print(board[row][col], end=' ')
    print()
