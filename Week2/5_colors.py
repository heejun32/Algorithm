test_cases = int(input().strip())

for test_case in range(test_cases):
    board = [[0 for col in range(10)] for row in range(10)]
    count = 0
    matrixs = int(input().strip())

    for matrix in range(matrixs):
        matrix_info = list(input().strip().split())
        for i in range(len(matrix_info)):
            matrix_info[i] = int(matrix_info[i])
        matrix_color = matrix_info[-1]

        for row in range(matrix_info[0], matrix_info[2] + 1):
            for col in range(matrix_info[1], matrix_info[3] + 1):
                board[row][col] = board[row][col] + matrix_color
                if board[row][col] >= 3:
                    count = count +1

    print("#{} {}".format(test_case + 1, count))
    
# 기존에 생각한 논리는 맞았음. 다만 입력값에 형태가 올바르지 않을때의 데이터 처리를 split()함수로 처리하지 않고 있었음 ㅠ