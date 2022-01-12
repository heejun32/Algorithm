N = int(input())    # 컴퓨터(노드)의 수
K = int(input())    # 간선의 수

graph = [[] for _ in range(N + 1)]   # 노드의 정보를 담을 그래프 선언
visit = [False] * (N + 1)

def DFS(graph, visit):
    stack = []
    infected = 0

    stack.append(graph[1])
    visit[1] = True

    while stack:
        computers = stack.pop()

        for computer in computers:
            if not visit[computer]:
                visit[computer] = True
                stack.append(graph[computer])
                infected += 1
    return infected

for _ in range(1, K + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(DFS(graph, visit))