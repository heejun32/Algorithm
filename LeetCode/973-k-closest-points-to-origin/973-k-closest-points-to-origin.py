import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = (x - 0) ** 2 + (y - 0) ** 2
            # heapq.heappush(heap, (dist, x, y))
            heap.append((dist, x, y))
        
        heapq.heapify(heap)
        
        results = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            results.append([x, y])
            
        return results