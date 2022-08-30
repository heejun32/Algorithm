import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 그래프 인접 리스트로 구현
        graph = collections.defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        # 방문 기록
        visited = [-1] * n
        
        # (가격, 정점, 경유지 횟수)
        Q = [(0, src, k)]
        
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if visited[node] >= k:
                continue
            visited[node] = k
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
        
        return -1