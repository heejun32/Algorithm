import sys
input = sys.stdin.readline

# 변수 선언
N = int(input())
amswer = 0
SCHEDULE = []

# 입력값 처리
for n in range(N):
    SCHEDULE.append(list(map(int, input().split())))
SCHEDULE.sort(key=lambda x: (x[1], x[0]))

# 탐색 시작
answer = 1  # 문제의 최소 조건은 N >= 1이다.
next = SCHEDULE[0][1]
for n in range(1, N):
    if SCHEDULE[n][0] >= next:
        answer += 1
        next = SCHEDULE[n][1]

# 정답 출력
print(answer)
