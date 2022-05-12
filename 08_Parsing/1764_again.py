import sys
input = sys.stdin.readline

set_n = set()
set_m = set()

N, M = map(int, input().split())

for i in range(N):
    set_n.add(input().strip())
for i in range(M):
    set_m.add(input().strip())

answer = list(set_n & set_m)
answer.sort()
print(len(answer))
for a in answer:
    print(a)
