import sys
input = sys.stdin.readline

MAX = -10e9
MIN = 10e9
N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))


def bfs(depth, total, plus, minus, multiplication, division):
    global MAX, MIN
      
    if depth == N:
        MAX = max(MAX, total)
        MIN = min(MIN, total)
        return None
    if plus:
        bfs(depth + 1, total + A[depth], plus - 1, minus, multiplication, division)
    if minus:
        bfs(depth + 1, total - A[depth], plus, minus - 1, multiplication, division)
    if multiplication:
        bfs(depth + 1, total * A[depth], plus, minus, multiplication - 1, division)
    if division:
        bfs(depth + 1, int(total / A[depth]), plus, minus, multiplication, division - 1)


bfs(1, A[0], O[0], O[1], O[2], O[3])
print(MAX)
print(MIN)
