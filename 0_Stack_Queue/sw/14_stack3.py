TEST_CASE = int(input())

def DFS(S):
    visited[S] = True
    for next in graph[S]:
        if visited[next] == False:
            DFS(next)

for test in range(1, TEST_CASE + 1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]  # 노드의 숫자는 정수이기에 0이 안들어옴 인덱스 편리화를 위해 v+1
    visited = [False for _ in range(V + 1)] # 방문여부 확인

    for j in range(E):
        A, B = map(int, input().split())
        graph[A].append(B) # 각 노드별 간선을 추가

    S, E = map(int, input().split())  # 출발, 도착 노드 정보
    DFS(S)
    if visited[E] == False:
        answer = 0
    else:
        answer = 1
    print(f"#{test} {answer}")
