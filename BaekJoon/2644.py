def BFS(graph, visit, start, end):
    path = 1
    queue = [[graph[start], path]]
    visit[start] = True

    while queue:
        nodes, path = queue.pop(0)

        for node in nodes:
            if not visit[node]:
                visit[node] = True
                if node == end:
                    return path
                else:
                    queue.append([graph[node], path + 1])

    return -1   # end를 찾으면 항상 path를 리턴하기 때문에 이 단계까지 온 경우는 오직 BFS 탐색 했을 때 end를 못 찾은 경우 뿐이다.

Nodes = int(input())
start, end = map(int, input().split())
M = int(input())
graph = [[] for _ in range(Nodes + 1)]
visit = [False for _ in range(Nodes + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(BFS(graph, visit, start, end))