import sys
input = sys.stdin.readline

N, M = map(int, input().split())
LINE = list(map(int, input().split()))
low = 0  # 문제의 최소 조건 -> 길이가 1인 1개의 나무에서 1만큼의 나무를 베어야 할 때
high = max(LINE)
answer = 0

while low <= high:
    total = 0
    middle = (low + high) // 2
    for i in range(len(LINE)):
        rest = LINE[i] - middle
        if rest > 0:
            total += rest
            # 중간이 전부 탐색하기 전에 목표치를 채웠으면 멈춰야 한다.
            if total > M:
                break

    # 나무를 덜 잘라야한다.
    if total >= M:
        answer = middle
        low = middle + 1
    # 나무를 더 잘라야 한다.
    if total < M:
        high = middle - 1

print(answer)

# 왜 len(line)해야지 5% 통과?
