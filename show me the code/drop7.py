import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]
num = int(sys.stdin.readline())

print(board, num)

# 공은 항상 위에서 아래로 떨어 뜨린다.