import sys

def DFS(graph, visit, start):
    if visit[start] == True:
        return 0
    stack = [graph[start]]
    visit[start] = True

    while stack:
        nodes = stack.pop()

        for node in nodes:
            if visit[node] == False:
                visit[node] = True
                stack.append(graph[node])
    return 1

input = sys.stdin.readline
N, M = map(int, input().split())
visit = [False for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
connected = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for start in range(1, N + 1):
    if DFS(graph, visit, start):
        connected += 1

print(connected)