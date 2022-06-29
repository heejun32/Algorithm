import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))
answer = 0


# 문제의 최대, 최소값의 기준을 명확히 확인할 것!
start = 1
end = max(lines)

while start <= end:
    middle = (start + end) // 2
    count = 0
    for line in lines:
        count += line // middle

    if count >= N:
        answer = max(answer, middle)
        start = middle + 1
    else:
        end = middle - 1

print(answer)
