from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
GRAPH = [[] for _ in range(N)]

# 그래프의 인덱스는 1부터 시작하기에 들어오는 값들을 -1 계산해서 넣기
for m in range(M):
    start, end = map(int, input().split())
    GRAPH[start-1].append(end-1)
    GRAPH[end-1].append(start-1)


# bfs 탐색으로 순차적으로 목표 노드까지의 path를 구함
def bfs(start, end):
    queue = deque()
    queue.append(GRAPH[start])
    path = 0

    while queue:
        path += 1
        # 순차적으로 같은 레벨에 있는 노드를 방문해야 한다.
        # 따라서 처음 같은 레벨에 있는 노드의 정보만큼 edge를 탐색해야됨.
        for _ in range(len(queue)):
            edges = queue.popleft()

            for edge in edges:
                if not visit[edge]:
                    visit[edge] = True
                    if edge == end:
                        return path
                    else:
                        queue.append(GRAPH[edge])


# 탐색 시작
answer = []
for i in range(N):
    temp = 0
    for j in range(N):
        if i == j:
            continue
        else:
            visit = [False] * N
            temp += bfs(i, j)
    answer.append(temp)


# 정답 출력
minimum = min(answer)
for i in range(N):
    if answer[i] == minimum:
        print(i+1)
        break
