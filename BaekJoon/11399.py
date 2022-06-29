import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.sort()

answer = 0
pre = 0

for i in range(N):
    # i번째 사람이 지금까지 기다린 시간
    wait = pre + P[i]
    # 지금까지 기다린 사람들의 총 시간합
    answer += wait
    # 이전 사람이 기다린 시간
    pre += P[i]

print(answer)
