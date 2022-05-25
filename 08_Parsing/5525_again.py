import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()
answer = 0

# 기본 시작은 IOI,
std = "IOI"
for i in range(N - 1):  # N이 1씩 늘어날때마다 + OI를 붙여주면 됨
    std += "OI"

length = len(std)
for j in range(M - length):
    if std == S[j: j + length]:
        answer += 1

print(answer)


N = int(input())
M = int(input())
S = input().strip()

count = 0
pattern = 0 # 패턴의 길이
i = 0

while i < M - 1:
    if S[i: i+3] == "IOI":
        i += 2
        pattern += 1
        if pattern == N:
            count += 1
            pattern -= 1
    else:
        i += 1
        pattern = 0

print(count)


# 참고 사이트: https://black-hair.tistory.com/135
