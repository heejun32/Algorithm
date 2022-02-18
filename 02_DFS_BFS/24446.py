from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

def bfs(V, E, R):
    V[R] = 0
    depth = 0
    queue.append(E[R])
    
    while queue:
        u = queue.popleft()
        depth += 1
        for edge in u:
            if V[edge] == -1:
                V[edge] = depth
                queue.append(E[edge])

    for i in range(1, len(V)):
        print(V[i])

N, M, R = map(int, input().split())
E =[[] for _ in range(N + 1)]
V =[-1 for _ in range(N + 1)]

for i in range(1, M + 1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

bfs(V, E, R)