from collections import deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(deque)
        # 그래프 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].popleft())
            route.append(a)
            
        dfs('JFK')
        return route[::-1]