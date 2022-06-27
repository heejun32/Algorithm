import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * M for _ in range(N)]

# 반시계 이동 연산
def reverse_rotate(up, down, left, right):
    # 위 계산
    for i in len(board[up]):
        board[up][i]







    # 왼쪽 오른쪽 계산







# 결과 출력
for row in range(N):
    for col in range(M):
        print(board[row][col], end=' ')
    print()