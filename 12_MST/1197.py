import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
visit = [False for _ in range(V + 1)]
weight = [-10e6 for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append([B, C])
    graph[B].append([A, C])

for i in range(1, V + 1):
    