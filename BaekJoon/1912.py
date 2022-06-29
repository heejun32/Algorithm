import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
answer = s[0]

for i in range(1, n):
    s[i] = max(s[i], s[i-1] + s[i])
    answer = max(answer, s[i])

print(answer)
