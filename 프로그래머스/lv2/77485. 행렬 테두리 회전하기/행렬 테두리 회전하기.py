import sys


def solution(rows, columns, queries):
    answer = []
    # 매트릭스 작성
    matrix = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    num = 1
    for row in range(1, rows + 1):
        for col in range(1, columns + 1):
            matrix[row][col] = num
            num += 1
    
    for x1, y1, x2, y2 in queries:
        temp = matrix[x1][y1]
        mini = temp
        
        # left
        for row in range(x1, x2):
            nex = matrix[row + 1][y1]
            matrix[row][y1] = nex
            mini = min(mini, nex)
        
        # bottom
        for col in range(y1, y2):
            nex = matrix[x2][col + 1]
            matrix[x2][col] = nex
            mini = min(mini, nex)
        
        # right
        for row in range(x2, x1, -1):
            prv = matrix[row - 1][y2]
            matrix[row][y2] = prv
            mini = min(mini, prv)
            
        # top
        for col in range(y2, y1, -1):
            prv = matrix[x1][col - 1]
            matrix[x1][col] = prv
            mini = min(mini, prv)
        
        matrix[x1][y1 + 1] = temp
        answer.append(mini)
    return answer