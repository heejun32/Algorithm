from collections import deque
from pickletools import long1, long4
import sys
input = sys.stdin.readline
queue = deque()

def bfs(V, E, R, O):
    V[R] = 0
    O[R] = 1
    depth = 0
    order = 1
    queue.append(E[R])
    
    while queue:
        u = queue.popleft()
        u.sort()
        depth += 1
        for edge in u:
            if V[edge] == -1:
                V[edge] = depth
                order += 1
                O[edge] = order
                queue.append(E[edge])

    # for i in range(1, len(V)):
    #     print(V[i])

N, M, R = map(int, input().split())
E = [[] for _ in range(N + 1)]  # 간선 정보
V = [-1 for _ in range(N + 1)]  # 노드 깊이
O = [0 for _ in range(N + 1)]   # 방문 순서

for i in range(1, M + 1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

bfs(V, E, R, O)

answer = 0
for i in range(1, N + 1):
    answer += V[i] * O[i]
print(answer)