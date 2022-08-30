import collections
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        # 그래프 인접 리스트로 구현
        for f, t, p in flights:
            graph[f].append((t, p))
        
        vis = [0] * n
        
        # (가격, 정점, 남은 경유지 횟수)
        Q = [(0, src, k + 1)]
        
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if vis[node] >= k:
                continue
            vis[node ] = k    
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
        
        return -1