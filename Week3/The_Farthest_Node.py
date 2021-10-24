def solution(n, edge):
    graph = [[] for _ in range(n)]          # 각 노드의 간선 정보를 저장하기 위한 그래프
    depts = [0 for _ in range(n)]           # 1번 노드 기준 각 노드까지의 경로 길이를 저장
    is_visit = [False for _ in range(n)]    # 각 노드별 방문 확인을 위한 리스트
    queue = [0]                             # 시작노드는 1번의 index값
    is_visit[0] = True                      # 1번 노드는 시작하자마자 방문

    for (a, b) in edge:                     # edge의 정보를 토대로 각 노드의 간선 정보를 저장
        graph[a - 1].append(b - 1)          # 인덱스 값이 0부터 시작하기 때문에 -1을 a, b 각각 실시
        graph[b - 1].append(a - 1)

    while queue:                            # BFS 탐색 시작.
        idx = queue.pop(0)

        for j in graph[idx]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)             # 그림을 통해 훨씬 잘 이해할 수 있음
                depts[j] = depts[idx] + 1   # 1번 노드부터 방문했기 때문에 이전 연결 노드의 길이에서 해당 노드까지의 경로 길이인 1을 더해줌

    answer = depts.count(max(depts))
    return answer

# feedback: 처음 bfs 문제라는 것은 이해했지만 그래프 구현에 대해 상당한 애를 먹어 결국 구글링함
# 그런데 의이한 점은 몇몇 코드를 작성한 이들이 의미없이 n+1 크기의 리스트를 만들어 메모리를 낭비하는 모습을 보임
# 리스트의 인덱싱을 1부터 시작하기 위해 그런것으로 처음에 이해했으나 이후 다른 리스트 크기는 다시 n
# 따라서 그냥 코드 복붙하다가 수정하기를 깜빡한 건가... 그러진 말자...
