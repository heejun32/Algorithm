class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # 그래프 설정
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 큐 변수: [(소요시간, 정점)]
        Q = [(0, k)]
        
        dist = collections.defaultdict(list)
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
                    
        if len(dist) == n:
            return max(dist.values())
        return -1