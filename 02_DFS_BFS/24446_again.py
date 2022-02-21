from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

def bfs(V, E, R, D):
    V[R] = 1        # 방문 확인
    D[R] = 0
    depth = 0
    queue.append(E[R])
    
    while queue:
        depth += 1
        # i = 1
        # print(f'{i}회차')
        # print('depth : ', depth)
        # print('queue : ', queue)
        for _ in range(len(queue)):
            u = queue.popleft()
            for edge in u:
                if V[edge] == 0:
                    V[edge] = 1
                    D[edge] = depth
                    queue.append(E[edge])
        # i += 1

N, M, R = map(int, input().split())
E =[[] for _ in range(N + 1)]
V =[0 for _ in range(N + 1)]
D =[-1 for _ in range(N + 1)]

for i in range(1, M + 1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

bfs(V, E, R, D)

for i in range(1, len(D)):
    print(D[i])