import sys
input = sys.stdin.readline

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]

# 집의 개수는 무조건 2개 이상이다.
for i in range(1, N):
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]

# 정답 출력
print(min(RGB[-1]))
