N, M = map(int, input().split())
BOARD = [[] for _ in range(N)]
answers = []

for row in range(N):
    BOARD[row] = input()

for row1 in range(N - 7):
    for col1 in range(M - 7):
        white = 0
        black = 0
        for row2 in range(row1, row1 + 8):
            for col2 in range(col1, col1 + 8):
                if (row2 + col2) % 2 == 0:
                    if BOARD[row2][col2] != 'W':
                        white += 1
                    if BOARD[row2][col2] != 'B':
                        black += 1
                else:
                    if BOARD[row2][col2] != 'B':
                        white += 1
                    if BOARD[row2][col2] != 'W':
                        black += 1

        answers.append(white)
        answers.append(black)

print(min(answers))


# 00 01 02 03 04 05 06 07
# 10 11 12 13 14 15 16 17
# 20 21 22 23 24 25 26 27
# 30 31 32 33 34 35 37 37 