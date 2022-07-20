from collections import defaultdict


def solution(tickets):
    answer = []
    
    # 노드 정보 그래프화
    graph = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    
    
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        answer.append(a)
    
    dfs('ICN')
    return answer[::-1]