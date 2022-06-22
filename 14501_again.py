import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
MAX = -1


def bfs(T, P):
    global MAX
    if T == N + 1:
        MAX = max(MAX, P)
        return None

    next_day = S[T - 1][0]
    profit = S[T - 1][1]
    if T + next_day <= N + 1:
        bfs(T + next_day, P + profit)
    bfs(T + 1, P)


bfs(1, 0)
print(MAX)
     