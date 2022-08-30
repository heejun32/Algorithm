import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        dist = collections.defaultdict(int)
        
        # 소요 시간, 정점
        Q = [(0, k)]

        # 그래프 인접 리스트 구현
        for u, v, w in times:
            graph[u].append((v, w))

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, ((alt, v)))

        # 결과 확인
        if len(dist) == n:
            return max(dist.values())
        return -1