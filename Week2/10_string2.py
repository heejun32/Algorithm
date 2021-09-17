TEST_CASE = int(input())

for test in range(1, TEST_CASE + 1):
    row, col = map(int, input().strip().split())
    matrix = [[0 for c in range(col)] for r in range(row)]
    answer = []

    for r in range(row):
        matrix[r] = input()

    # 가로 회귀문 먼저 확인
    for r in range(row):
        if matrix[r] == matrix[r][-1::-1]:
            answer = matrix[r]

    # 세로 회귀문 확인
    for c in range(col):
        for r in range(row/2):
           if matrix[r][c] != matrix[-1][c]:
                continue


