import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))

MAXIMUM = -1e9  # 최댓값 비교를 위해 문제 범위에서 가장 작은수
MINIMUM = 1e9   # 최솟값 비교를 위해 문제 범위에서 가장 작은수


def dfs(depth, total, plus, minus, multiply, divide):
    global MAXIMUM, MINIMUM
    if depth == N:
        MAXIMUM = max(total, MAXIMUM)
        MINIMUM = min(total, MINIMUM)

    if plus:
        dfs(depth + 1, total + A[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - A[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * A[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / A[depth]), plus, minus, multiply, divide - 1)


dfs(1, A[0], O[0], O[1], O[2], O[3])
print(MAXIMUM)
print(MINIMUM)
