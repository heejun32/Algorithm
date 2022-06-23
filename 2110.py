import sys
input = sys.stdin.readline

N, C = map(int, input().split())
X = []
for _ in range(N):
    X.append(int(input()))
X.sort()

start = 1
end = X[-1] - X[0]
answer = 0

while start <= end:
    middle = (start + end) // 2
    now = X[0]
    count = 1
    for i in range(1, N):
        if X[i] >= now + middle:
            count += 1
            now = X[i]
    
    if count >= C:
        start = middle + 1
        answer = middle
    else:
        end = middle - 1

print(answer)
