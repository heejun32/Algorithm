from collections import deque

def DFS(start):
    print(start, end =" ")
    visit[start] = True

    for i in graph[start]:
        if not visit[i]:
            DFS(i)

def BFS(start):
    visit[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

DFS(V)
visit = [False] * (N + 1)
print()
BFS(V)




