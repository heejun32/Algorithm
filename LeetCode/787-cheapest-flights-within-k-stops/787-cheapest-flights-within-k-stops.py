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
        
        # 큐 연산: 소요시간이 제일 작은 경로를 계속해서 탐색한다.
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            # 비용이 적고(큐 연산), 이미 방문한 경로는 탐색에서 제외한다.
            if visited[node] >= k:
                continue
            # 그렇지 않다면 탐색 경로에 추가한다.(전체 최소 비용이 아닌 k 경로 횟수 내에서의 최소 비용을 탐색하는 것이다.)

            visited[node] = k
            # print(visited)
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
        
        return -1